import fcntl
import json
import shelve
import threading
import traceback
import weakref
from collections.abc import MutableMapping
from pathlib import Path

import psycopg2.extensions
from psycopg2 import InterfaceError, OperationalError, connect
from wsgidav.lock_man.lock_storage import LockStorageDict  # type: ignore
from wsgidav.util import get_module_logger  # type: ignore

_logger = get_module_logger(__name__)


class ManabiTimeoutMixin:
    def set_timeout(self, lock):
        max_timeout = self.max_timeout
        timeout = lock.get("timeout")

        if not timeout:
            lock["timeout"] = max_timeout
        else:
            if timeout > max_timeout:
                lock["timeout"] = max_timeout


class ManabiContextLockMixin:
    def __enter__(self):
        self.acquire()

    def __exit__(self, exc_type, exc_value, traceback):
        self.release()


class ManabiShelfLock(ManabiContextLockMixin):
    def __init__(self, storage_path, storage_object):
        self._storage_path = storage_path
        self._storage_object = weakref.ref(storage_object)
        self._semaphore = 0
        self._lock_file = open(f"{storage_path}.lock", "wb+")
        self._fd = self._lock_file.fileno()
        self.acquire_write = self.acquire_read = self.acquire
        self._id = None

    def acquire(self):
        tid = threading.get_ident()
        if self._id and self._id != tid:
            _logger.error("Do not use from multiple threads")
        self._id = tid
        if self._semaphore == 0:
            fcntl.flock(self._fd, fcntl.LOCK_EX)
            self._storage_object()._dict = shelve.open(str(self._storage_path))
        self._semaphore += 1

    def release(self):
        tid = threading.get_ident()
        if self._semaphore == 0:
            _logger.error(
                f"Inconsistent use of lock. {''.join(traceback.format_stack())}"
            )
        if self._id and self._id != tid:
            _logger.error("Do not use from multiple threads")
        self._id = tid
        self._semaphore -= 1
        if self._semaphore == 0:
            storage_object = self._storage_object()
            storage_object._dict.close()
            storage_object._dict = None
            fcntl.flock(self._fd, fcntl.LOCK_UN)
        self._id = threading.get_ident()


class ManabiShelfLockLockStorage(LockStorageDict, ManabiTimeoutMixin):
    def __init__(self, refresh: float, storage: Path):
        super().__init__()
        self.max_timeout = refresh / 2
        self._storage = storage
        self._lock = ManabiShelfLock(storage, self)

    def open(self):
        pass

    def close(self):
        pass

    def create(self, path, lock):
        with self._lock:
            self.set_timeout(lock)
            super().create(path, lock)

    def clear(self):
        if self._dict:
            with self._lock:
                self._dict.clear()

    def refresh(self, token, *, timeout):
        with self._lock:
            return super().refresh(token, timeout=timeout)

    def get(self, token):
        with self._lock:
            return super().get(token)

    def delete(self, token):
        with self._lock:
            return super().delete(token)

    def get_lock_list(self, path, *, include_root, include_children, token_only):
        with self._lock:
            return super().get_lock_list(
                path,
                include_root=include_root,
                include_children=include_children,
                token_only=token_only,
            )


class ManabiPostgresLock(ManabiContextLockMixin):
    def __init__(self, storage):
        self._id = None
        self.storage = weakref.ref(storage)
        self.acquire_write = self.acquire_read = self.acquire
        self._semaphore = 0
        self._id = None

    def acquire(self):
        tid = threading.get_ident()
        if self._id and self._id != tid:
            _logger.error("Do not use from multiple threads")
        self._id = tid
        if self._semaphore == 0:
            _logger.info(f"{tid} acquire")
            self.storage().execute("LOCK TABLE manabi_lock IN ACCESS EXCLUSIVE MODE")
        self._semaphore += 1

    def release(self):
        tid = threading.get_ident()
        if self._semaphore == 0:
            _logger.error(
                f"Inconsistent use of lock. {''.join(traceback.format_stack())}"
            )
        if self._id and self._id != tid:
            _logger.error("Do not use from multiple threads")
        self._id = tid
        self._semaphore -= 1
        if self._semaphore == 0:
            _logger.info(f"{tid} release")
            self.storage()._connection.commit()


class ManabiPostgresDict(MutableMapping):
    def __init__(self, storage, lock):
        self.storage = weakref.ref(storage)
        self._lock = lock

    @staticmethod
    def decode_lock(lock):
        if "owner" in lock:
            owner = lock["owner"]
            if isinstance(owner, bytes):
                lock["owner"] = {"manabi_was_bytes": owner.decode("UTF-8")}

    @staticmethod
    def encode_lock(lock):
        if "owner" in lock:
            owner = lock["owner"]
            if "manabi_was_bytes" in owner:
                lock["owner"] = owner["manabi_was_bytes"].encode("UTF-8")

    def cleanup(self):
        with self._lock:
            self.storage().execute("DELETE FROM manabi_lock;")

    def __len__(self):
        with self._lock:
            cursor = self.storage().execute("SELECT count(*) FROM manabi_lock")
            return int(cursor.fetchone()[0])

    def __iter__(self):
        with self._lock:
            cursor = self.storage().execute("SELECT token FROM manabi_lock")
            for token in cursor.fetchall():
                yield token[0]

    def __delitem__(self, token):
        with self._lock:
            self.storage().execute(
                "DELETE FROM manabi_lock WHERE token = %s", (str(token),)
            )

    def __contains__(self, token):
        with self._lock:
            cursor = self.storage().execute(
                "SELECT 1 FROM manabi_lock WHERE token = %s", (str(token),)
            )
            if cursor.fetchone() is None:
                return False
            else:
                return True

    def __setitem__(self, token, lock):
        with self._lock:
            self.decode_lock(lock)
            json_lock = json.dumps(lock)
            self.storage().execute(
                """
                    INSERT INTO manabi_lock(token, data) VALUES (%(token)s, %(data)s)
                        ON CONFLICT(token) DO
                        UPDATE SET data = %(data)s WHERE manabi_lock.token = %(token)s
                """,
                {
                    "token": token,
                    "data": json_lock,
                },
            )

    def __getitem__(self, token):
        with self._lock:
            cursor = self.storage().execute(
                "SELECT data FROM manabi_lock WHERE token = %s", (str(token),)
            )
            lock = cursor.fetchone()
            if lock is None:
                raise KeyError(f"{token} not found")
            lock = lock[0]
            self.encode_lock(lock)
            return lock


class ManabiDbLockStorage(LockStorageDict, ManabiTimeoutMixin):
    def __init__(self, refresh: float, postgres_dsn: str):
        super().__init__()
        self._postgres_dsn = postgres_dsn
        self.max_timeout = refresh / 2
        self._connection = None
        self.connect()
        self._lock = ManabiPostgresLock(self)
        self._dict = ManabiPostgresDict(self, self._lock)

    def connect(self):
        try:
            if self._connection:
                # it the connecton failed, this might cause an exception, we do not care.
                self._connection.close()
        except Exception:
            pass
        self._connection = connect(self._postgres_dsn)
        self._connection.commit()
        self._connection.autocommit = False
        self._connection.set_session(
            isolation_level=psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE
        )
        self._cursor = self._connection.cursor()

    def open(self):
        pass

    def execute(self, *args, **kwargs):
        try:
            self._cursor.execute(*args, **kwargs)
        except (InterfaceError, OperationalError):
            _logger.error(
                f"Postgres connection lost, reconnecting. {''.join(traceback.format_stack())}"
            )

            self.connect()
            self._cursor.execute(*args, **kwargs)
        return self._cursor

    def close(self):
        pass

    def create(self, path, lock):
        with self._lock:
            self.set_timeout(lock)
            super().create(path, lock)

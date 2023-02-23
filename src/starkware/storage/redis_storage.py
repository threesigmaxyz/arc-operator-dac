import os
from typing import Optional

from redis import Redis, ConnectionPool
from starkware.storage.storage import Storage


# Method to parse and build Redis connection string in any format
def build_connection_pool(
        conn_str: str,
        db: int
) -> ConnectionPool:
    try:
        hostport, *options = conn_str.split(",")
        host, _, port = hostport.partition(":")
        arguments = {
            opt: int(value) if opt == "port" else value
            for opt, _, value in (option.partition("=") for option in options)
            if opt not in ("ssl", "abortConnect")
        }
    except (AttributeError, ValueError, TypeError):
        raise ValueError("Invalid connection string format")

    if not host:
        raise ValueError("Missing host in connection string")

    if not port:
        raise ValueError("Missing port in connection string")

    return ConnectionPool(host=host, port=int(port), db=db, **arguments)


class RedisStorage(Storage):
    """
    Redis storage.
    """

    def __init__(
        self,
        db: int
    ):
        self.connection_pool = build_connection_pool(os.getenv('REDIS_CONNSTR'), db)

    @classmethod
    async def create_from_config(
        cls, db: int
    ) -> "RedisStorage":
        return cls(
            db=db,
        )

    async def set_value(self, key: bytes, value: bytes):
        r = Redis(connection_pool=self.connection_pool)
        r.set(key, value)

    async def get_value(self, key: bytes) -> Optional[bytes]:
        r = Redis(connection_pool=self.connection_pool)

        return r.get(key)

    async def del_value(self, key: bytes):
        try:
            r = Redis(connection_pool=self.connection_pool)
            r.delete(key)
        except KeyError:
            pass

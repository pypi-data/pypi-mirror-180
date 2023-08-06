"""Dep redis module."""

import aioredis

from typing import Dict, Optional
from dataclasses import dataclass

from spec.types import Module, Environment # noqa


@dataclass
class Redis(Module):
    """redis module."""

    host: str = 'localhost'

    db: int = 0
    port: int = 6379
    username: Optional[str] = None
    password: Optional[str] = None

    encoding_errors: str = "strict"
    decode_responses: bool = False
    retry_on_timeout: bool = False
    max_connections: Optional[int] = None

    use_ssl: bool = False

    options: Optional[Dict] = None

    __store__: aioredis.Redis = None

    @property
    def store(self) -> aioredis.Redis:
        """Store."""
        return self.__store__

    def default_redis_kw(self) -> Dict:
        """Default redis kw."""
        options = {
            'port': self.port,
            'username': self.username,
            'password': self.password,
            'encoding_errors': self.encoding_errors,
            'decode_responses': self.decode_responses,
            'retry_on_timeout': self.retry_on_timeout,
            'max_connections': self.max_connections,
        }

        if self.options:
            options.update(self.options)

        return options

    def create_client(self, override_kw: Dict = None) -> aioredis.Redis:
        """Create redis client."""
        client_kw = self.default_redis_kw()
        if override_kw:
            client_kw.update(override_kw)

        client_kw.update({'db': self.db})

        redis_url = '{prefix}://{url}'.format(
            prefix='rediss' if self.use_ssl else 'redis',
            url=self.host,
        )

        return aioredis.from_url(url=redis_url, **client_kw)

    async def prepare(self, scope):
        """Prepare redis."""
        self.__store__ = self.create_client()

    async def health(self, scope) -> bool:
        """Health redis."""
        try:
            await self.__store__.ping()
            return True
        except aioredis.RedisError as _redis_exc:
            return False


__all__ = ('Redis', )

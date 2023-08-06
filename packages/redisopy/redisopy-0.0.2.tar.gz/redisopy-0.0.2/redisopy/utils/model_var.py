import random
from dataclasses import dataclass, field
from typing import Set, Any

from redis.client import StrictRedis

from redisopy.connection import DEFAULT_CONNECTION


@dataclass
class ModelClassVar:
    """Model class level var"""
    cls_name: str = ""
    meta: Any = None
    keys: Set[str] = field(default_factory=set)
    model_fields: dict = field(default_factory=dict)

    def __hash__(self):
        return hash(self.cls_name, random.randint(0, 100))

    def __eq__(self, other):
        return self.cls_name == other.cls_name

    @property
    def conn(self) -> StrictRedis:
        """Get alive redis connection by connect"""
        return DEFAULT_CONNECTION[0]

    @property
    def key_prefix(self) -> str:
        if self.meta:
            key_prefix = getattr(self.meta, "key_prefix", self.cls_name.lower())
        else:
            key_prefix = f"{self.cls_name.lower()}:"
        return key_prefix

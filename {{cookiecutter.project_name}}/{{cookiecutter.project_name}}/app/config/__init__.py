from .base import BaseConfig
from .database import DatabaseConfig
from .jwt import JWTConfig


class Config(BaseConfig, DatabaseConfig, JWTConfig):
    pass

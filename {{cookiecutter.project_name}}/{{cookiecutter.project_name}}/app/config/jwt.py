import os

from .provider import configuration


class JWTConfig:
    JWT_ACCESS_LIFESPAN = configuration.get_config(
        "jwt.lifespan.access", path_mode=True
    )
    JWT_REFRESH_LIFESPAN = configuration.get_config(
        "jwt.lifespan.refresh", path_mode=True
    )
    JWT_ALGORITHM = configuration.get_config("jwt.algorithm", path_mode=True)
    JWT_SECRET_KEY = os.urandom(128)

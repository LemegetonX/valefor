import os

from .provider import configuration
from .base import BaseConfig

class DatabaseConfig:
    MIGRATIONS_DIR = os.path.join(BaseConfig.APP_DIR, "migrations/")

    DB_NAME = configuration.get_credential("db_name")
    DB_HOST = configuration.get_credential("db_host")
    DB_PASSWORD = configuration.get_credential("db_password")
    DB_PORT = configuration.get_credential("db_port")
    DB_USER = configuration.get_credential("db_user")

    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

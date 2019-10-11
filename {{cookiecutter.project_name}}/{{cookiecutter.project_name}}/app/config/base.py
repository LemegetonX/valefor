import os


class BaseConfig:
    APP_DIR: str = os.path.abspath("./{{cookiecutter.project_name}}/app")

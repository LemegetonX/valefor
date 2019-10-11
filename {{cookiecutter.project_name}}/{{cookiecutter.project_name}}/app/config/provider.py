from sitri import Sitri
from sitri.contrib.system import SystemCredentialProvider
from sitri.contrib.yaml import YamlConfigProvider

configuration = Sitri(
    config_provider=YamlConfigProvider(yaml_path="./config.yaml"),
    credential_provider=SystemCredentialProvider(
        prefix="{{cookiecutter.project_name}}".lower()
    ),
)

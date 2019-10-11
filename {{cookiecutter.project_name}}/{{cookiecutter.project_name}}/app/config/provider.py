from sitri.contrib.yaml import YamlConfigProvider
from sitri.contrib.system import SystemCredentialProvider
from sitri import Sitri

configuration = Sitri(
    config_provider=YamlConfigProvider(yaml_path="./config.yaml"),
    credential_provider=SystemCredentialProvider(prefix="{{cookiecutter.project_name}}".lower())
)

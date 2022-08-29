{% if cookiecutter.use_api == "yes" -%}
import importlib.metadata


__TITLE__ = "{{cookiecutter.package_name}}"
__DESCRIPTION__ = "{{cookiecutter.package_description}}"

try:
    __VERSION__ = importlib.metadata.version(__package__)
except importlib.metadata.PackageNotFoundError:
    __VERSION__ = "0.0.1"
{% endif -%}

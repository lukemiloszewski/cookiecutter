#!/usr/bin/env python3
import os
import shutil
import subprocess
import pathlib


PROJECT_DIRECTORY = pathlib.Path(os.path.realpath(os.path.curdir))


def remove_file(filepath):
    full_path = PROJECT_DIRECTORY / filepath
    if (full_path.is_file()):
        os.remove(full_path)
    else:
        shutil.rmtree(full_path)


def rename_file(old, new):
    old_path = PROJECT_DIRECTORY / old
    new_path = PROJECT_DIRECTORY / new
    os.rename(old_path, new_path)


if __name__ == "__main__":
    if "{{ cookiecutter.use_api }}" == "no":
        remove_file("src/{{cookiecutter.package_name}}/routers")
        remove_file("src/{{cookiecutter.package_name}}/app.py")
        remove_file("src/{{cookiecutter.package_name}}/bootstrap.py")
        remove_file("src/{{cookiecutter.package_name}}/config.py")
        remove_file("src/{{cookiecutter.package_name}}/context.py")
        remove_file("src/{{cookiecutter.package_name}}/dependencies.py")
        remove_file("src/{{cookiecutter.package_name}}/logging.py")
        remove_file("src/{{cookiecutter.package_name}}/middleware.py")
        remove_file("tests/routers")
        remove_file("tests/test_bootstrap.py")
        remove_file("tests/test_context.py")
        remove_file("tests/test_dependencies.py")
        remove_file("tests/test_middleware.py")
        remove_file("scripts")
    else:
        remove_file("src/{{cookiecutter.package_name}}/py.typed")

    if "{{ cookiecutter.use_cli }}" == "no":
        remove_file("src/{{cookiecutter.package_name}}/__main__.py")
        remove_file("tests/test_main.py")

    if "{{ cookiecutter.use_auto_publish }}" == "no":
        remove_file(".github/workflows/publish.yml")

    if "{{ cookiecutter.use_github_actions }}" == "no":
        remove_file(".github")

    subprocess.call(['git', 'init'])
    subprocess.call(['make', 'init'])
    subprocess.call(['make', 'format'])

    if "{{ cookiecutter.use_git }}" == "yes":
        subprocess.call(['git', 'add', '*'])
        subprocess.call(['git', 'commit', '-m', 'Initial commit', '--no-verify'])
        subprocess.call(['git', 'branch', '-m', 'main'])

#!/usr/bin/env python3
import os
import pathlib
import shutil

PROJECT_DIRECTORY = pathlib.Path(os.path.realpath(os.path.curdir))


def remove_file(filepath):
    full_path: pathlib.Path = PROJECT_DIRECTORY / filepath
    if not full_path.exists():
        pass
    elif full_path.is_file():
        os.remove(full_path)
    else:
        shutil.rmtree(full_path)


if __name__ == "__main__":
    if "{{ cookiecutter.use_docs }}" == "no":
        remove_file("docs")
        remove_file("mkdocs.yml")
        remove_file(".github/workflows/deploy_docs.yml")

    if "{{ cookiecutter.use_github_actions }}" == "no":
        remove_file(".github")

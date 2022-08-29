import uvicorn

from {{cookiecutter.package_name}}.bootstrap import bootstrap_app
from {{cookiecutter.package_name}}.config import CONFIG

app = bootstrap_app(CONFIG)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        use_colors=True,
        host="localhost",
        port=7500,
        reload=True,
    )

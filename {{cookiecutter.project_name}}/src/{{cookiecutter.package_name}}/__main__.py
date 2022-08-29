import typer


app = typer.Typer()


@app.command()
def main() -> None:
    """{{cookiecutter.package_name}}."""


if __name__ == "__main__":
    app(prog_name="{{cookiecutter.project_name}}")  # pragma: no cover

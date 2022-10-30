import typer


app = typer.Typer()


@app.command()
def main() -> None:
    """{{cookiecutter.package_name}}."""

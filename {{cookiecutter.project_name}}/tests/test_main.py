from typer.testing import CliRunner

from {{cookiecutter.package_name}} import main


def test_main_runs(runner: CliRunner) -> None:
    result = runner.invoke(main.app)
    assert result.exit_code == 0

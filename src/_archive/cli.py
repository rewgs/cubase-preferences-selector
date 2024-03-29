import typer
from cb_prefs_select import __app_name__, __version__
from typing import Optional

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-V",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True
    ),
    cubase_version: Optional[bool] = typer.Option(
        None,
        "--cubase-version",
        "-v",
        help="Specifies which version of Cubase to return stock preferences for.",
    )
) -> None: return

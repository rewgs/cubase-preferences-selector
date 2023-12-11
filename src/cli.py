"""
--help:                 Displays this menu.
--version, -V:          Displays the version of this app.
--cubase-version, -v:   Optional argument used to specify which version of Cubase to find stock preferences for.
"""

import typer

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__}")

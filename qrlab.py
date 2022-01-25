from typing import Optional
from typer import Typer, style, colors, Option


app = Typer()


def __version_callback(value: bool):
    if value:
        name = style(text="QRLabs", fg=colors.GREEN, bold=True)
        typer.echo(message=f"{name} 1.0.0")


@app.callback()
def callback(
    version: Optional[bool] = Option(
        False, "--version", "-v", callback=__version_callback, is_eager=True,
        help="Afficher la version actuelle de l'application"
    )
):
    """
    Un outil CLI simple pour générer et décoder les codes qr.
    """

from commands.decode import *
from commands.generate import *

if __name__ == "__main__":
    app()

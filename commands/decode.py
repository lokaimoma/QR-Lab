from cgitb import text
from typing import Optional
from numpy import imag
import typer
from qrlab import app
from core.decoders import decode_qr_code, decode_qr_code_


@app.command()
def decode(
    image_file: str = typer.Argument(..., help="L'emplacement de l'image du code qr"),
    use_open_cv: Optional[bool] = typer.Option(
        False, 
        "--use-open-cv",
        help="Choisissez d'utiliser la bibliothèque open cv pour décoder l'image. La bibliothèque par défaut est pyzbar."
    )
):
    """
    Décode et affiche les données dans un code qr.
    La bibliothèque "open cv" fonctionne parfois et parfois non, d'où la raison de spécifier de l'utiliser.
    """
    if use_open_cv:
        __open_cv_decode(image_file)
        raise typer.Exit()
    data = decode_qr_code_(image_file_path=image_file)
    if len(data) <= 0:
        typer.secho(
            "Aucun code qr n'a été trouvé dans le fichier fourni.",
            fg=typer.colors.BRIGHT_WHITE,
            bg=typer.colors.RED
        )
        raise typer.Exit()
    for data_ in data:
        head = typer.style(
            text="QR code data =>",
            fg=typer.colors.GREEN,
            bold=True,
            underline=True
        )
        typer.echo(message=f"{head} {data_.data}")
        head = typer.style(
            text="Points =>",
            fg=typer.colors.GREEN,
            bold=True,
            underline=True
        )



def __open_cv_decode(image_file):
    result = decode_qr_code(image_file_path=image_file)
    if not result:
        typer.secho(
            "Aucun code qr n'a été trouvé dans le fichier fourni.",
            fg=typer.colors.BRIGHT_WHITE,
            bg=typer.colors.RED
        )
        raise typer.Exit()
    value = result[0]
    head = typer.style(
        text="QR code data =>",
        fg=typer.colors.GREEN,
        bold=True,
        underline=True
    )
    typer.echo(message=f"{head} {value}")
    head = typer.style(
        text="Points =>",
        fg=typer.colors.GREEN,
        bold=True,
        underline=True
    )

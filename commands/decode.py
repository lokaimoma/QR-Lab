from cgitb import text
from numpy import imag
import typer
from qrlab import app
from core.decoders import decode_qr_code


@app.command()
def decode(
    image_file: str = typer.Argument(..., help="L'emplacement de l'image du code qr")
):
    """
    Décode et affiche les données dans un code qr.
    """
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
        text="Data =>", 
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

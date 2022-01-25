from tkinter.font import BOLD
import typer


from qrlab import app
from core.generators import generate_default


@app.command()
def generate(
    nom: str = typer.Argument(..., help="Nom du fichier image final"),
    data: str = typer.Argument(...,
                               help="Le donnée ou texte à transformer en un code qr."),
):
    """
    Générer un code qr à partir d'une donnée donnée
    """
    image = generate_default(data=data)
    image.save(f"{nom}.png")
    typer.secho(message="Code QR généré avec succès", fg=typer.colors.GREEN, bold=True)
    location = typer.style(text="Location =>", fg=typer.colors.GREEN, underline=True, bold=True)
    typer.echo(message=f"{location} ./{nom}.png")

from typing import Type
from typer import Typer


app = Typer()


from commands.generate import *
from commands.decode import *

if __name__ == "__main__":
    app()

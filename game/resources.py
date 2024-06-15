""" Módulo dos recursos """

# Imports de pacotes BuiltIn
from os.path import join
from typing import Optional

# Imports de pacotes externos
from arcade import load_font

class Resources():
    """ Define as propriedades """

    def __init__(self, root_path: str) -> None:
        """ Inicializa os recursos """

        self._resources_path = join(root_path, "resources") if root_path else "resources"

        # Fontes
        self._fonts_path: str = join(self._resources_path, "fonts")
        self._fonts: dict[str, str] = {
            "title": "Dimitri Swank",
            "body": "Type Machine",
            "button": "Retro Gaming"
        }

        # Imagens
        self._images_path: str = join(self._resources_path, "images")

    @property
    def fonts(self) -> dict[str, str]:
        """ As fontes utilizadas """

        return self._fonts

    def images(self, name: str) -> str:
        """ As imagens utilizadas """

        return join(self._images_path, name + ".png")

    def setup(self) -> None:
        """ Configura todos os recursos """

        # Fontes
        self.load_all_fonts()

    def load_all_fonts(self) -> None:
        """ Carrega todas as fontes """

        for font in self._fonts:
            load_font(join(self._fonts_path, self._fonts[font] + ".ttf"))

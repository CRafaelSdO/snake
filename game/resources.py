""" Módulo dos recursos """

# Imports de pacotes BuiltIn
from dataclasses import dataclass
from os import getcwd
from os.path import join
from typing import NamedTuple, Optional

# Imports de pacotes externos
from arcade import load_font

class Resources():
    """ Define as propriedades """

    DEFAULT_RESOURCES_PATH: str = join(getcwd(), "resources")

    @dataclass
    class Font():
        """ Define uma fonte """

        name: str
        file_path: str

    # Fontes padrão
    DEFAULT_FONTS: dict[str, Font] = {
        "title": Font("Dimitri Swank", join(DEFAULT_RESOURCES_PATH, "fonts/Dimitri Swank.ttf")),
        "body": Font("Type Machine", join(DEFAULT_RESOURCES_PATH, "fonts/Type Machine.ttf")),
        "button": Font("Retro Gaming", join(DEFAULT_RESOURCES_PATH, "fonts/Retro Gaming.ttf"))
    }

    # Imagens padrão
    DEFAULT_IMAGES: dict[str, str] = {
        "sprites": join(DEFAULT_RESOURCES_PATH, "images/sprites.png"),
        "seta": join(DEFAULT_RESOURCES_PATH, "images/seta.png"),
        "esc": join(DEFAULT_RESOURCES_PATH, "images/esc.png")
    }

    def __init__(self, fonts: Optional[dict[str, Font]] = DEFAULT_FONTS, images: Optional[dict[str, str]] = DEFAULT_IMAGES) -> None:
        """ Inicializa os recursos """

        # Fontes
        self._fonts: dict[str, Resources.Font] = fonts
        self._images: dict[str, str] = images

    @property
    def fonts(self) -> dict[str, Font]:
        """ As fontes utilizadas """

        return self._fonts

    @property
    def images(self) -> dict[str, str]:
        """ As imagens utilizadas """

        return self._images

    def setup(self) -> None:
        """ Configura todos os recursos """

        # Fontes
        self.load_all_fonts()

    def load_all_fonts(self) -> None:
        """ Carrega todas as fontes """

        for font in self._fonts:
            load_font(self._fonts.get(font).file_path)

# Exportação padrão
__all__ = ["Resources"]

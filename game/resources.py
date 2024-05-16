""" Módulo dos recursos """

# Imports de pacotes BuiltIn
from os.path import normpath
from typing import NamedTuple, Optional

# Imports de pacotes externos
from arcade import load_font

class Resources():
    """ Define as propriedades """

    class Font(NamedTuple):
        """ Define uma fonte """

        name: str
        file_path: str

    # Fontes padrão
    DEFAULT_FONTS: dict[str, Font] = {
        "title": Font("Dimitri Swank", "game\\resources\\fonts\\Dimitri Swank.ttf"),
        "body": Font("Type Machine", "game\\resources\\fonts\\Type Machine.ttf"),
        "button": Font("Retro Gaming", "game\\resources\\fonts\\Retro Gaming.ttf")
    }

    def __init__(self, fonts: Optional[dict[str, Font]] = DEFAULT_FONTS) -> None:
        """ Inicializa os recursos """

        # Fontes
        self._fonts: dict[str, Resources.Font] = fonts

    @property
    def fonts(self) -> dict[str, Font]:
        """ As fontes utilizadas """

        return self._fonts

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

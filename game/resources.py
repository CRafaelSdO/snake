""" Módulo dos recursos """

# Imports de pacotes BuiltIn
from os import getcwd
from os.path import join

# Imports de pacotes externos
from arcade import load_font

# Pastas padrão
RESOURCES_PATH: str = join(getcwd(), "resources")
FONTS_PATH: str = join(RESOURCES_PATH, "fonts")
IMAGES_PATH: str = join(RESOURCES_PATH, "images")

# Fontes padrão
FONTS: dict[str, str] = {
    "title": "Dimitri Swank",
    "body": "Type Machine",
    "button": "Retro Gaming"
}

class Resources():
    """ Define as propriedades """

    def __init__(self) -> None:
        """ Inicializa os recursos """

        # Fontes
        self._fonts: dict[str, str] = FONTS
        self._images_path: str = IMAGES_PATH

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
            load_font(join(FONTS_PATH, self._fonts[font] + ".ttf"))

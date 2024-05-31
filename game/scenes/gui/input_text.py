""" Módulo do input de texto """

# Imports de pacotes externos
from arcade import Window
from arcade.gui import UIInputText

# Imports de pacotes locais
from .text_area import *

class InputText(UIInputText):
    """ Define um input de texto """

    def __init__(self, window: Window, font_name: str, font_size: float) -> None:
        """ Inicializa uma input de texto """

        # Área de texto para definir largura e altura do input
        aux = TextArea("A", font_name, font_size)
        width, height = aux.size

        width = window.properties.cell_size * 10

        super().__init__(width = width, height = height, font_name = font_name, font_size = font_size)

# Export padrão
__all__ = ["InputText"]

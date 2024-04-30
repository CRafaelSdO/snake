""" Módulo da área de texto """

# Imports de pacotes externos
from arcade import create_text_image, create_text_sprite
from arcade.arcade_types import Color
from arcade.gui import UITextArea

class TextArea(UITextArea):
    """ Define uma área de texto """

    def __init__(self, width: float, height: float, text: str, font_name: str, font_size: float, text_color: Color = (0, 0, 0), multiline: bool = False) -> None:
        """ Inicializa uma área de texto """

        super().__init__(width = width, height = height, text = text, font_name = font_name, font_size = font_size, text_color = text_color, multiline = multiline)

# Export padrão
__all__ = ["TextArea"]

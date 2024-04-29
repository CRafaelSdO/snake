""" Módulo da área de texto """

# Imports de pacotes externos
from arcade import Text
from arcade.gui import UITextArea
from arcade.arcade_types import Color

class TextArea(UITextArea):
    """ Define uma área de texto """

    def __init__(self, text: str, font_name: str, font_size: float, text_color: Color = Color(0, 0, 0), multiline: bool = False) -> None:
        """ Inicializa uma área de texto """

        # Objeto Text para pegar a altura e largura
        _text = Text(text, 0, 0, font_name = font_name, font_size = font_size, multiline = multiline)
        width, height = _text.size

        super().__init__(width = width, height = height, text = text, font_name = font_name, font_size = font_size, text_color = text_color, multiline = multiline)

__all__ = ["TextArea"]

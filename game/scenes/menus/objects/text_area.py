""" Módulo da área de texto """

# Imports de pacotes externos
from arcade.gui import UITextArea
from arcade.arcade_types import Color
from arcade import create_text_image

class TextArea(UITextArea):
    """ Define uma área de texto """

    def __init__(self, text: str, font_name: str, font_size: float, text_color: Color = (0, 0, 0), multiline: bool = False) -> None:
        """ Inicializa uma área de texto """

        # Imagem de texto para definir largura e altura da área de texto
        _ = create_text_image(text, (0, 0, 0), font_size, font_name = font_name)
        width, height = _.size

        super().__init__(width = width + font_size / 10, height = height + font_size / 10, text = text, font_name = font_name, font_size = font_size, text_color = text_color, multiline = multiline)

# Export padrão
__all__ = ["TextArea"]

""" Módulo da área de texto """

# Imports de pacotes externos
from arcade.gui import UITextArea

class TextArea(UITextArea):
    """ Define uma área de texto """

    def __init__(self, text: str, font_name: str, font_size: float) -> None:
        """ Inicializa uma área de texto """

        super().__init__(text = text, font_name = font_name, font_size = font_size, text_color = (0, 0, 0), multiline = False)

        self.fit_content()

# Export padrão
__all__ = ["TextArea"]

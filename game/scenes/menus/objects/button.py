""" Módulo do botão """

# Imports de pacotes BuiltIn
from typing import NamedTuple, Optional

# Imports de pacotes externos
from arcade.gui import UIFlatButton
from arcade.arcade_types import Color
from arcade import create_text_image

class Button(UIFlatButton):
    """ Define um botão """

    class ButtonStyle(NamedTuple):
        """ Define o estilo de um botão """

        font_name: str
        font_size: str
        font_color: Optional[Color] = (0, 0, 0)
        border_color: Optional[Color] = (127, 127, 127)
        border_width: Optional[float] = 2.5
        bg_color: Optional[Color] = (85, 85, 85)
        font_color_pressed: Optional[Color] = (85, 85, 85)
        border_color_pressed: Optional[Color] = (0, 0, 0)
        bg_color_pressed: Optional[Color] = (170, 170, 170)

    def __init__(self, text: str, style: ButtonStyle):
        """ Inicializa um botão """

        # Imagem de texto para definir largura e altura da área de texto
        _ = create_text_image(text, (0, 0, 0), style.font_size, font_name = style.font_name)
        width, height = _.size

        super().__init__(width = width + style.font_size * 3, height = height + style.font_size * 1.5, text = text, style = style._asdict())

# Export padrão
__all__ = ["Button"]

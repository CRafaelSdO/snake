""" Módulo do botão """

# Imports de pacotes BuiltIn
from typing import NamedTuple, Optional

# Imports de pacotes externos
from arcade import create_text_image, Window
from arcade.arcade_types import Color
from arcade.gui import UIFlatButton
from arcade.gui.events import UIOnClickEvent

# Imports de pacotes locais
from ..scenes import *
from ..speeds import *

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

    def __init__(self, text: str, style: ButtonStyle, window: Window, scene: Scene, speed: Optional[Speed] = None) -> None:
        """ Inicializa um botão """

        # Imagem de texto para definir largura e altura da área de texto
        _ = create_text_image(text, (0, 0, 0), style.font_size, font_name = style.font_name)
        width, height = _.size

        super().__init__(width = width * 2, height = height * 2, text = text, style = style._asdict())

        # Janela deste botão
        self._window: Window = window

        # Cena para a qual a janela vai ao clicar no botão
        self._scene: Scene = scene

        # Velocidade que sera configurada ao clicar nesse botão
        self._speed: Speed = speed

    def on_click(self, event: UIOnClickEvent) -> None:
        """ Chamado ao clicar no botão """

        # Configura a velocidade e muda a cena
        self._window.speed = self._speed
        self._window.switch_scene(self._scene)

# Export padrão
__all__ = ["Button"]

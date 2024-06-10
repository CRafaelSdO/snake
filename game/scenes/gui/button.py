""" Módulo do botão """

# Imports de pacotes BuiltIn
from typing import NamedTuple, Optional

# Imports de pacotes externos
from arcade import Window
from arcade.arcade_types import Color
from arcade.gui import UIFlatButton
from arcade.gui.events import UIOnClickEvent

# Imports de pacotes locais
from ..scenes import Scene
from ..speeds import Speed
from .text_area import TextArea

class Button(UIFlatButton):
    """ Define um botão """

    class ButtonStyle(NamedTuple):
        """ Define o estilo de um botão """

        font_name: str
        font_size: int
        font_color: Optional[Color] = (0, 0, 0)
        border_color: Optional[Color] = (127, 127, 127)
        border_width: Optional[float] = 2.5
        bg_color: Optional[Color] = (85, 85, 85)
        font_color_pressed: Optional[Color] = (85, 85, 85)
        border_color_pressed: Optional[Color] = (0, 0, 0)
        bg_color_pressed: Optional[Color] = (170, 170, 170)

    def __init__(self, text: str, style: ButtonStyle, window: Window, scene: Scene, speed: Optional[Speed] = None) -> None:
        """ Inicializa um botão """

        # Área de texto para definir largura e altura do botão
        aux = TextArea(text, style.font_name, style.font_size)
        width, height = aux.size
        margin = window.properties.cell_size

        super().__init__(width = width + margin, height = height + margin, text = text, style = style._asdict())

        # Janela deste botão
        self._window: Window = window

        # Cena para a qual a janela vai ao clicar no botão
        self._scene: Scene = scene

        # Velocidade que sera configurada ao clicar nesse botão
        self._speed: Speed = speed

    def on_click(self, event: UIOnClickEvent) -> None:
        """ Chamado ao clicar no botão """

        # Configura muda a cena e passando a velocidade escolhida
        self._window.switch_scene(self._scene, self._speed)

    def set_text(self, text: str):
        """ Redefine o texto desse botão """

        # Área de texto para definir largura e altura do botão
        aux = TextArea(text, self._style.get("font_name"), self._style.get("font_size"))
        width, height = aux.size
        margin = self._window.properties.cell_size

        self.text = text
        self.rect = self.rect.resize(width + margin, height + margin)

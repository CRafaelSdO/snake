""" Módulo do menu jogar """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import View, Window
from arcade.gui import UIAnchorWidget, UIBoxLayout, UIManager

# Imports de pacotes locais
from .gui import *
from .scenes import *
from .speeds import *

class PlayMenu(View):
    """ Define um menu jogar """

    def __init__(self, window: Optional[Window]) -> None:
        """ Inicializa um menu jogar """

        super().__init__(window)

        # Gerenciador de UI
        self._ui_manager: UIManager = None

        # Controla se os objetos do menu já foram criados
        self._setup: bool = False

    def setup(self) -> None:
        """ Configura o menu jogar """

        if self._setup:
            return

        # Área de texto
        title_text = TextArea(470, 80, "Escolha a dificuldade:", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body"))

        # Estilo dos botões
        button_style = Button.ButtonStyle(self.window.resources.fonts.get("button").name, self.window.properties.fonts_sizes.get("button"))

        # Botões
        very_easy = Button("Muito Fácil", button_style, self.window, Scene.PLAYING, Speed.VERY_EASY)
        easy = Button("Fácil", button_style, self.window, Scene.PLAYING, Speed.EASY)
        medium = Button("Médio", button_style, self.window, Scene.PLAYING, Speed.MEDIUM)
        hard = Button("Difícil", button_style, self.window, Scene.PLAYING, Speed.HARD)
        extreme = Button("Extremo", button_style, self.window, Scene.PLAYING, Speed.EXTREME)
        back = Button("Voltar", button_style, self.window, self.window.last_scene)

        # Box layout para conter os botões
        box = UIBoxLayout(space_between = 10)
        box.add(title_text)
        box.add(very_easy)
        box.add(easy)
        box.add(medium)
        box.add(hard)
        box.add(extreme)
        box.add(UIAnchorWidget(child = back, anchor_x = "left", anchor_y = "bottom"))

        # Gerenciador de UI com elemento de ancoragem para centralizar tudo
        self._ui_manager = UIManager()
        self._ui_manager.add(UIAnchorWidget(child = box))

        self._setup = True

    def on_show_view(self) -> None:
        """ Chamada uma vez ao entrar nessa cena """

        # Ativa o gerenciador de UI
        self._ui_manager.enable()

    def on_hide_view(self) -> None:
        """ Chamada uma vez ao sair dessa cena """

        # Desativa o gerenciador de UI
        self._ui_manager.disable()

    def on_draw(self) -> None:
        """ Chamada sempre ao desenhar """

        # Desenha o plano de fundo
        self.window.draw_background()

        # Desenha a UI
        self._ui_manager.draw()

# Export padrão
__all__ = ["PlayMenu"]

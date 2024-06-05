""" Módulo do menu jogar """

# Imports de pacotes externos
from arcade import Window
from arcade.gui import UIAnchorWidget, UIBoxLayout

# Imports de pacotes locais
from .base_scene import *
from .gui import *
from .scenes import *
from .speeds import *

class PlayMenu(BaseScene):
    """ Define um menu jogar """

    def __init__(self, window: Window) -> None:
        """ Inicializa um menu jogar """

        super().__init__(window)

    def setup(self) -> None:
        """ Configura o menu jogar """

        if self.full_screen == self.window.fullscreen:
            return
        else:
            self.ui_manager.clear()

        # Box layout para alinhar e centralizar tudo
        box = UIBoxLayout(space_between = 10)
        self.ui_manager.add(UIAnchorWidget(child = box))

        # Título
        title_text = TextArea("Escolha a dificuldade:", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body"))
        box.add(title_text)

        # Botões
        ## Estilo
        button_style = Button.ButtonStyle(self.window.resources.fonts.get("button").name, self.window.properties.fonts_sizes.get("button"))

        ## Instâncias
        very_easy = Button("Muito Fácil", button_style, self.window, Scene.PLAYING, Speed.VERY_EASY)
        box.add(very_easy)

        easy = Button("Fácil", button_style, self.window, Scene.PLAYING, Speed.EASY)
        box.add(easy)

        medium = Button("Médio", button_style, self.window, Scene.PLAYING, Speed.MEDIUM)
        box.add(medium)

        hard = Button("Difícil", button_style, self.window, Scene.PLAYING, Speed.HARD)
        box.add(hard)

        extreme = Button("Extremo", button_style, self.window, Scene.PLAYING, Speed.EXTREME)
        box.add(extreme)

        back = Button("Voltar", button_style, self.window, self.window.last_scene)
        box.add(UIAnchorWidget(child = back, anchor_x = "left", anchor_y = "bottom"))

        # Define que os objetos de UI foram criados
        self.full_screen = self.window.fullscreen

# Export padrão
__all__ = ["PlayMenu"]

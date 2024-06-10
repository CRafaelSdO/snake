""" Módulo do menu jogar """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import Window
from arcade.gui import UIAnchorWidget, UIBoxLayout

# Imports de pacotes locais
from .base_scene import BaseScene
from .gui import TextArea, Button
from .scenes import Scene
from .speeds import Speed

class PlayMenu(BaseScene):
    """ Define um menu jogar """

    def __init__(self, window: Window) -> None:
        """ Inicializa um menu jogar """

        super().__init__(window)

    def setup(self, speed: Optional[Speed] = None, score: Optional[int] = None) -> None:
        """ Configura o menu jogar """

        super().setup()

        # Verifica se o modo de janela desta cena é o mesmo que o da janela
        if self.full_screen == self.window.fullscreen:
            return

        # Reinicia o gerenciador de UI
        self.ui_manager.clear()

        # Box layout para alinhar e centralizar tudo
        box = UIBoxLayout(space_between = 10)
        self.ui_manager.add(UIAnchorWidget(child = box))

        # Título
        title_text = TextArea("Escolha a dificuldade:", self.window.resources.fonts["body"], self.window.properties.fonts_sizes["body"])
        box.add(title_text)

        # Botões
        ## Estilo
        button_style = Button.ButtonStyle(self.window.resources.fonts["button"], self.window.properties.fonts_sizes["button"])

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

        # Configura o modo de janela desta cena
        self.full_screen = self.window.fullscreen

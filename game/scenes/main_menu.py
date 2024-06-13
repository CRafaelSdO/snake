""" Módulo do menu principal """

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

class MainMenu(BaseScene):
    """ Define um menu principal """

    def __init__(self, window: Window) -> None:
        """ Inicializa um menu principal """

        super().__init__(window)

        # Botão para mudar entre tela cheia e janela
        self._switch_full_screen: Button = None

    def setup(self, speed: Optional[Speed] = None, score: Optional[int] = None) -> None:
        """ Configura o menu principal """

        # Verifica se esta cena já foi configurada
        if self.setted:
            return

        # Reinicia o gerenciador de UI
        self.ui_manager.clear()

        # Box layout para alinhar e centralizar tudo
        box = UIBoxLayout(space_between = 10)
        self.ui_manager.add(UIAnchorWidget(child = box))

        # Título
        title_text = TextArea("Snake", self.window.resources.fonts["title"], self.window.properties.fonts_sizes["title"])
        box.add(title_text)

        # Botões
        ## Estilo
        button_style = Button.ButtonStyle(self.window.resources.fonts["button"], self.window.properties.fonts_sizes["button"])

        ## Instâncias
        play = Button("Jogar", button_style, self.window, Scene.PLAY_MENU)
        box.add(play)

        ranking = Button("Classificação", button_style, self.window, Scene.RANKING_MENU)
        box.add(ranking)

        switch_full_screen_text = "Janela" if self.window.fullscreen else "Tela Cheia"

        self._switch_full_screen = Button(switch_full_screen_text, button_style, self.window, Scene.SWITCH_FULL_SCREEN)
        box.add(self._switch_full_screen)

        close = Button("Fechar", button_style, self.window, Scene.CLOSE)
        box.add(close)

        # Define que esta cena foi configurada
        self.setted = True

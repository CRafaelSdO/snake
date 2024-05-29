""" Módulo do menu de fim de jogo """

# Imports de pacotes externos
from arcade import View, Window
from arcade.gui import UIAnchorWidget, UIBoxLayout, UIManager

# Imports de pacotes locais
from .gui import *
from .scenes import *

class GameOverMenu(View):
    """ Define um menu de fim de jogo """

    def __init__(self, window: Window) -> None:
        """ Inicializa um menu de fim de jogo """

        super().__init__(window)

        # Gerenciador de UI
        self._ui_manager: UIManager = None

        # Controla se os objetos da UI já foram criados
        self._setup: bool = False

    def setup(self, score: int = 0) -> None:
        """ Configura o menu de fim de jogo """

        if self._setup:
            return

        # Áreas de texto
        game = TextArea("Fim de", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("title"))
        over = TextArea("Jogo", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("title"))

        # Estilo dos botões
        button_style = Button.ButtonStyle(self.window.resources.fonts.get("button").name, self.window.properties.fonts_sizes.get("button"))

        # Botões
        main_menu = Button("Menu Principal", button_style, self.window, Scene.MAIN_MENU)
        restart = Button("Reiniciar", button_style, self.window, Scene.PLAYING)

        # Box layout para conter e alinhar os botões na horizontal
        buttons_box = UIBoxLayout(vertical = False, space_between = 10)
        buttons_box.add(main_menu)
        buttons_box.add(restart)

        # Box layout para conter e alinhar o texto e os botões na vertical
        box = UIBoxLayout(space_between = 10)
        box.add(game)
        box.add(over)
        box.add(buttons_box)

        # Gerenciador de UI com elemento de ancoragem para centralizar tudo
        self._ui_manager = UIManager()
        self._ui_manager.add(UIAnchorWidget(child = box))

        # Define que os objetos de UI foram criados
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
__all__ = ["GameOverMenu"]

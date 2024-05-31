""" Módulo do menu principal """

# Imports de pacotes externos
from arcade import View, Window
from arcade.gui import UIAnchorWidget, UIBoxLayout, UIManager

# Imports de pacotes locais
from .gui import *
from .scenes import *

class MainMenu(View):
    """ Define um menu principal """

    def __init__(self, window: Window) -> None:
        """ Inicializa um menu principal """

        super().__init__(window)

        # Gerenciador de UI
        self._ui_manager: UIManager = None

        # Controla se os objetos da UI já foram criados
        self._setup: bool = False

    def setup(self) -> None:
        """ Configura o menu principal """

        if self._setup:
            return

        # Gerenciador de UI
        self._ui_manager = UIManager()

        # Box layout para alinhar e centralizar tudo
        box = UIBoxLayout(space_between = 10)
        self._ui_manager.add(UIAnchorWidget(child = box))

        # Título
        title_text = TextArea("Snake", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("title"))
        box.add(title_text)

        # Botões
        ## Estilo
        button_style = Button.ButtonStyle(self.window.resources.fonts.get("button").name, self.window.properties.fonts_sizes.get("button"))

        ## Instâncias
        play = Button("Jogar", button_style, self.window, Scene.PLAY_MENU)
        box.add(play)

        ranking = Button("Classificação", button_style, self.window, Scene.RANKING_MENU)
        box.add(ranking)

        settings = Button("Configurações", button_style, self.window, Scene.SETTINGS_MENU)
        box.add(settings)

        close = Button("Fechar", button_style, self.window, Scene.CLOSE)
        box.add(close)

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
__all__ = ["MainMenu"]

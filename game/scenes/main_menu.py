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

        # Controla se os objetos do menu já foram criados
        self._setup: bool = False
    
    def setup(self) -> None:
        """ Configura o menu principal """

        if self._setup:
            return
        
        # Área de texto
        title_text = TextArea("Snake", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("title"))

        # Estilo dos botões
        button_style = Button.ButtonStyle(self.window.resources.fonts.get("button").name, self.window.properties.fonts_sizes.get("button"))

        # Botões
        play = Button("Jogar", button_style, self.window, Scene.PLAY_MENU)
        ranking = Button("Classificação", button_style, self.window, Scene.RANKING_MENU)
        settings = Button("Configurações", button_style, self.window, Scene.SETTINGS_MENU)
        close = Button("Fechar", button_style, self.window, Scene.CLOSE)
        
        # Box layout para conter o texto e os botões
        box = UIBoxLayout(space_between = 10)
        box.add(title_text)
        box.add(play)
        box.add(ranking)
        box.add(settings)
        box.add(close)

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
__all__ = ["MainMenu"]

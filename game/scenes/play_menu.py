""" Módulo do menu jogar """

# Imports de pacotes externos
from arcade import View, Window
from arcade.gui import UIAnchorWidget, UIBoxLayout, UIManager

# Imports de pacotes locais
from .gui import *
from .scenes import *
from .speeds import *

class PlayMenu(View):
    """ Define um menu jogar """

    def __init__(self, window: Window) -> None:
        """ Inicializa um menu jogar """

        super().__init__(window)

        # Gerenciador de UI
        self._ui_manager: UIManager = None

        # Controla se os objetos da UI já foram criados
        self._setup: bool = False

    def setup(self) -> None:
        """ Configura o menu jogar """

        if self._setup:
            return

        # Gerenciador de UI
        self._ui_manager = UIManager()

        # Box layout para alinhar e centralizar tudo
        box = UIBoxLayout(space_between = 10)
        self._ui_manager.add(UIAnchorWidget(child = box))

        # Título
        title_text = TextArea("Escolha a dificuldade:", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body"))
        box.add(UIAnchorWidget(child = title_text, anchor_y = "top"))

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

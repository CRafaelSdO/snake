""" Módulo do menu de fim de jogo """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import draw_rectangle_filled, draw_text, Window
from arcade.gui import UIAnchorWidget, UIBoxLayout

# Imports de pacotes locais
from .base_scene import *
from .gui import *
from .scenes import *
from .speeds import *

class GameOverMenu(BaseScene):
    """ Define um menu de fim de jogo """

    def __init__(self, window: Window) -> None:
        """ Inicializa um menu de fim de jogo """

        super().__init__(window)

        # Pontuação do jogo finalizado
        self._score: int = 0

        # Texto do score
        self._score_text: TextArea = None

        # Input de texto
        self._input_text: InputText = None

        # Controla se o score foi salvo
        self._saved: bool = False

    @property
    def score(self) -> tuple[str, int]:
        """ O nome do jogador e sua pontuação """

        return self._input_text.text, self._score

    @property
    def saved(self) -> bool:
        """ Informa se o score foi salvo """

        return self._saved

    @saved.setter
    def saved(self, value: bool) -> None:
        self._saved = value

    def setup(self, score: Optional[int] = None) -> None:
        """ Configura o menu de fim de jogo """

        # Define a pontuação
        self._score = score if score else self._score

        # Define se pode salvar o score
        self._saved = False if score else self._saved

        # Formata o texto do score
        score_text = f"{self._score:_}".replace("_", ".")

        if self.full_screen == self.window.fullscreen:
            self._score_text.text = f"Você fez {score_text} pontos"
            self._score_text.fit_content()

            self._input_text.text = ""
            return
        else:
            self.ui_manager.clear()

        # Box layout para alinhar e centralizar tudo
        box = UIBoxLayout(space_between = 10)
        self.ui_manager.add(UIAnchorWidget(child = box))

        # Título
        game = TextArea("Fim de", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("title") * 0.75)
        box.add(game)

        over = TextArea("Jogo", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("title") * 0.75)
        box.add(over)

        # Corpo
        self._score_text = TextArea(f"Você fez {score_text} pontos", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body"))
        box.add(self._score_text)

        # Input
        # Box layout para alinhar e centralizar o input
        input_box = UIBoxLayout(vertical = False, space_between = 10)
        box.add(input_box)

        ## Título
        digit_name = TextArea("Nome:", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.75)
        input_box.add(digit_name)

        ## Caixa de texto
        self._input_text = InputText(self.window, self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.75)
        input_box.add(self._input_text)

        # Botões
        ## Estilo
        button_style = Button.ButtonStyle(self.window.resources.fonts.get("button").name, self.window.properties.fonts_sizes.get("button"))

        ## Instâncias
        confirm = Button("Confirmar", button_style, self.window, Scene.SAVE_SCORE)
        input_box.add(confirm)

        # Box layout para conter e alinhar os botões de menu principal e reiniciar
        buttons_box = UIBoxLayout(vertical = False, space_between = 10)
        box.add(buttons_box)

        main_menu = Button("Menu Principal", button_style, self.window, Scene.MAIN_MENU)
        buttons_box.add(main_menu)

        restart = Button("Reiniciar", button_style, self.window, Scene.PLAYING)
        buttons_box.add(restart)

        # Define que os objetos de UI foram criados
        self.full_screen = self.window.fullscreen

    def on_draw(self) -> None:
        """ Chamada sempre ao desenhar """

        super().on_draw()

        x = self._input_text.center_x
        y = self._input_text.center_y
        width = self._input_text.width
        height = self._input_text.height

        # Retangulo para destacar o input de texto
        draw_rectangle_filled(x, y, width, height, (127, 127, 127, 127))

        # Texto do input de texto
        draw_text(self._input_text.text, x - width / 2, y, (0, 0, 0), self.window.properties.fonts_sizes.get("body") * 0.75, font_name = self.window.resources.fonts.get("body").name, anchor_y = "center")

# Export padrão
__all__ = ["GameOverMenu"]

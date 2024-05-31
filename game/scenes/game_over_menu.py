""" Módulo do menu de fim de jogo """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import draw_rectangle_filled, View, Window
from arcade.gui import UIAnchorWidget, UIBoxLayout, UIManager

# Imports de pacotes locais
from .gui import *
from .scenes import *
from .speeds import *

class GameOverMenu(View):
    """ Define um menu de fim de jogo """

    def __init__(self, window: Window) -> None:
        """ Inicializa um menu de fim de jogo """

        super().__init__(window)

        # Pontuação do jogo finalizado
        self._score: int = 0

        # Gerenciador de UI
        self._ui_manager: UIManager = None

        # Texto do score
        self._score_text: TextArea = None

        # Input de texto
        self._input_text: InputText = None

        # Controla se o score foi salvo
        self._saved: bool = False

        # Controla se os objetos da UI já foram criados
        self._setup: bool = False

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

        # Configura a velocidade jogada e a pontuação
        self._score = score if score else self._score

        # Define que pode salvar o score se for passado um novo
        self._saved = False if score else self._saved

        score_text = f"{self._score:_}".replace("_", ".")

        if self._setup:
            self._score_text.text = f"Você fez {score_text} pontos"
            self._score_text.fit_content()

            self._input_text.text = ""
            return

        # Áreas de texto
        game = TextArea("Fim de", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("title") * 0.75)
        over = TextArea("Jogo", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("title") * 0.75)
        self._score_text = TextArea(f"Você fez {score_text} pontos", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body"))
        digit_name = TextArea("Digite seu nome:", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.75)

        # Input de texto
        self._input_text = InputText(self.window, self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.75)

        # Estilo dos botões
        button_style = Button.ButtonStyle(self.window.resources.fonts.get("button").name, self.window.properties.fonts_sizes.get("button"))

        # Botões
        save_button = Button("Salvar", button_style, self.window, Scene.SAVE_SCORE)
        main_menu = Button("Menu Principal", button_style, self.window, Scene.MAIN_MENU)
        restart = Button("Reiniciar", button_style, self.window, Scene.PLAYING)

        # Box layout para conter e alinhar o input de texto e o botão de confirmação
        input_box = UIBoxLayout(vertical = False, space_between = 10)
        input_box.add(self._input_text)
        input_box.add(save_button)

        # Box layout para conter e alinhar os botões na horizontal
        buttons_box = UIBoxLayout(vertical = False, space_between = 10)
        buttons_box.add(main_menu)
        buttons_box.add(restart)

        # Box layout para conter tudo e alinhar na vertical
        box = UIBoxLayout(space_between = 10)
        box.add(game)
        box.add(over)
        box.add(self._score_text)
        box.add(digit_name)
        box.add(input_box)
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

        x = self._input_text.center_x
        y = self._input_text.center_y
        width = self._input_text.width
        height = self._input_text.height

        # Retangula para destacar o input de texto
        draw_rectangle_filled(x, y, width, height, (127, 127, 127, 127))

        # Desenha a UI
        self._ui_manager.draw()

# Export padrão
__all__ = ["GameOverMenu"]

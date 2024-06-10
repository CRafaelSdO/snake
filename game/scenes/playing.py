""" Módulo da tela de jogo """

# Imports de pacotes BuiltIn
from math import floor
from typing import Optional

# Imports de pacotes externos
from arcade import draw_rectangle_filled, draw_text, Sprite, SpriteList, Window
from arcade.gui import UIAnchorWidget, UIBoxLayout, UIManager
from arcade.key import ESCAPE

# Imports de pacotes locais
from .base_scene import BaseScene
from .entities import *
from .gui import TextArea, Button
from .scenes import Scene
from .speeds import Speed

class Playing(BaseScene):
    """ Define uma tela de jogo """

    def __init__(self, window: Window) -> None:
        """ Inicializa a tela de jogo """

        super().__init__(window, True)

        # Campo
        self._board: Board = None

        # Cobra
        self._snake: Snake = None

        # Comida
        self._food: Cell = None

        # Velocidade da cobra
        self._speed: Speed = None

        # Controla se o jogo já começou
        self._started: bool = None

        # Controla se o jogo está pausado
        self._paused: bool = None

        # Controla se conseguiu a pontuação máxima
        self._max_score: bool = None

        # Tempo decorrido desde a última atualização
        self._delta_time: float = None

        # Tempo com a pontuação máxima
        self._max_score_time: float = None

        # Gerenciador da UI de pausa
        self._pause_ui_manager: UIManager = UIManager()

        # Texto do Score
        self._score_text: TextArea = None

        # Lista de imagens
        self._images: SpriteList = SpriteList()

    def setup(self, speed: Optional[Speed] = None, score: Optional[int] = None) -> None:
        """ Configura a tela de jogo"""

        super().setup()

        # Configura o campo, a cobra e a primeira comida
        self._board = Board(self.window.properties)
        self._snake = Snake(self._board)
        self._food = self._board.generate_food()

        # Configura a velocidade de movimento da cobra
        self._speed = speed if speed else self._speed

        # Configura os campos de controle
        self._started = False
        self._paused = False
        self._max_score = False

        # Zera os contadores de tempo
        self._delta_time = 0
        self._max_score_time = 0

        # Verifica se o modo de janela desta cena é o mesmo que o da janela
        if self.full_screen == self.window.fullscreen:
            self._score_text.text = f"0"
            self._score_text.fit_content()
            return

        # Reinicia os gerenciadores de UI e a lista de sprites
        self.ui_manager.clear()
        self._pause_ui_manager.clear()
        self._images.clear()

        # Intruções iniciais
        width = self.window.properties.width
        height = self.window.properties.height
        cell_size = self.window.properties.cell_size
        scale = cell_size * 2 / 512

        ## Imagens
        up_arrow = Sprite(self.window.resources.images("seta"), scale = scale, center_x = width * 0.5 + cell_size * 3.5, center_y = height * 0.75 + cell_size * 1.05)
        self._images.append(up_arrow)

        down_arrow = Sprite(self.window.resources.images("seta"), scale = scale, center_x = width * 0.5 + cell_size * 3.5, center_y = height * 0.75 - cell_size * 1.05, angle = 180)
        self._images.append(down_arrow)

        left_arrow = Sprite(self.window.resources.images("seta"), scale = scale, center_x = width * 0.5 + cell_size * 1.4, center_y = height * 0.75 - cell_size * 1.05, angle = 90)
        self._images.append(left_arrow)

        right_arrow = Sprite(self.window.resources.images("seta"), scale = scale, center_x = width * 0.5 + cell_size * 5.6, center_y = height * 0.75 - cell_size * 1.05, angle = -90)
        self._images.append(right_arrow)

        escape = Sprite(self.window.resources.images("esc"), scale = scale, center_x = width * 0.5 + cell_size * 1.5, center_y = height * 0.25)
        self._images.append(escape)

        # UI do jogo
        ## Texto da pontuação
        self._score_text = TextArea("0", self.window.resources.fonts["body"], self.window.properties.fonts_sizes["button"])
        self.ui_manager.add(UIAnchorWidget(child = self._score_text, anchor_y = "top"))

        # UI do menu de pausa
        ## Box layout para alinhar e centralizar tudo
        box = UIBoxLayout(space_between = 10)
        self._pause_ui_manager.add(UIAnchorWidget(child = box))

        ## Título
        game = TextArea("Jogo", self.window.resources.fonts["title"], self.window.properties.fonts_sizes["title"] * 0.75)
        box.add(game)

        paused = TextArea("Pausado", self.window.resources.fonts["title"], self.window.properties.fonts_sizes["title"] * 0.75)
        box.add(paused)

        ## Box layout para alinhar e centralizar os botões
        buttons_box = UIBoxLayout(vertical = False, space_between = 10)
        box.add(buttons_box)

        ## Botões
        ### Estilo
        button_style = Button.ButtonStyle(self.window.resources.fonts["button"], self.window.properties.fonts_sizes["button"])

        ### Instâncias
        main_menu = Button("Menu Principal", button_style, self.window, Scene.MAIN_MENU)
        buttons_box.add(main_menu)

        restart = Button("Reiniciar", button_style, self.window, Scene.PLAYING)
        buttons_box.add(restart)

        # Configura o modo de janela desta cena
        self.full_screen = self.window.fullscreen

    def on_update(self, delta_time: float) -> None:
        """ Chama da ao atualizar """

        # Verifica se está pausado
        if not self._started or self._paused:
            return

        # Lógica para controlar a frequencia de atualização e a pontuação após preencher todo o campo
        self._delta_time += delta_time

        if self._max_score:
            self._max_score_time += delta_time

            self._score_text.text = f"{floor((self._snake.size - 2 + self._max_score_time) * self._speed.value * 10):_}".replace("_", ".")
            self._score_text.fit_content()

        if self._delta_time < 1 / self._speed.value:
            return

        self._delta_time = 0

        # Lógica principal do jogo
        next_cell = self._board.get_next_cell(self._snake.head, self._snake.direction)

        if not next_cell:
            return

        match(next_cell.content):
            case Content.FOOD:
                self._snake.eat(next_cell)

                self._score_text.text = f"{(self._snake.size - 2) * self._speed.value * 10:_}".replace("_", ".")
                self._score_text.fit_content()

                if self._snake.size < self._board.cells_count:
                    self._food = self._board.generate_food()
                else:
                    self._food = None
                    self._max_score = True
                pass

            case Content.BODY:
                self.window.switch_scene(Scene.GAME_OVER_MENU, score = floor((self._snake.size - 2 + self._max_score_time) * self._speed.value * 10))
                pass

            case _:
                self._snake.move(next_cell)
                pass

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        """ Chamada ao pressionar uma tecla """

        # Lógica para pausar e despausar
        if symbol == ESCAPE:
            self._paused = False if self._paused else True

            if self._paused:
                self._pause_ui_manager.enable()
            else:
                self._pause_ui_manager.disable()

        elif not self._paused:
            # Lógica para mudar a direção de movimento
            try:
                self._snake.direction = Direction(symbol)

                if not self._started:
                    self._started = True
            except:
                pass

    def on_draw(self) -> None:
        """ Chamada sempre ao desenhar """

        super().on_draw()

        # Desenha a comida e a cobra
        self._food.on_draw()
        self._snake.on_draw()

        # Desenha as intruções iniciais
        if not self._started and not self._paused:
            width = self.window.properties.width
            height = self.window.properties.height
            cell_size = self.window.properties.cell_size

            # Instruções para movimento
            draw_text("Use", width * 0.5 - cell_size * 3, height * 0.75, (0, 0, 0), self.window.properties.fonts_sizes["body"], font_name = self.window.resources.fonts["body"], anchor_x = "center", anchor_y = "center")
            draw_text("para se mover", width * 0.5, height * 0.75 - cell_size * 3, (0, 0, 0), self.window.properties.fonts_sizes["body"], font_name = self.window.resources.fonts["body"], anchor_x = "center", anchor_y = "center")

            # Instruções para pausar
            draw_text("Use", width * 0.5 - cell_size * 3, height * 0.25, (0, 0, 0), self.window.properties.fonts_sizes["body"], font_name = self.window.resources.fonts["body"], anchor_x = "center", anchor_y = "center")
            draw_text("para pausar o jogo", width * 0.5, height * 0.25 - cell_size * 3, (0, 0, 0), self.window.properties.fonts_sizes["body"], font_name = self.window.resources.fonts["body"], anchor_x = "center", anchor_y = "center")

            # Imagens
            self._images.draw()

        # Desenha o menu de pausa
        if self._paused:
            width = self.window.properties.width
            height = self.window.properties.height

            # UI de pausa com fundo acinzentado
            draw_rectangle_filled(width * 0.5, height * 0.5, width, height, (127, 127, 127, 127))

            self._pause_ui_manager.draw()
            pass

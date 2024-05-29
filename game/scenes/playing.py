""" Módulo da tela de jogo """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import draw_text, Sprite, SpriteList, View, Window
from arcade.gui import UIAnchorWidget, UIBoxLayout, UIManager
from arcade.key import ESCAPE

# Imports de pacotes locais
from .entities import *
from .gui import *
from .scenes import *
from .speeds import *

class Playing(View):
    """ Define uma tela de jogo """

    def __init__(self, window: Window) -> None:
        """ Inicializa a tela de jogo """

        super().__init__(window)

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

        # Tempo decorrido desde a última atualização
        self._delta_time: float = 0

        # Gerenciadores de UI
        self._ui_manager: UIManager = None
        self._pause_ui_manager: UIManager = None

        # Texto do Score
        self._score_text: TextArea = None

        # Lista de imagens
        self._images: SpriteList = None

        # Controla se os objetos da UI já foram criados
        self._setup: bool = False

    def setup(self, speed: Optional[Speed] = None) -> None:
        """ Configura a tela de jogo"""

        # Configura o campo, a cobra e a primeira comida
        self._board = Board(self.window.properties)
        self._snake = Snake(self._board)
        self._food = self._board.generate_food()

        # Configura a velocidade de movimento da cobra
        self._speed = speed if speed else self._speed

        # Configura os campos de controle
        self._started = False
        self._paused = False

        if self._setup:
            self._score_text.text = f"000"
            self._score_text.fit_content()
            return

        # Intruções iniciais
        width = self.window.properties.width
        height = self.window.properties.height
        cell_size = self.window.properties.cell_size
        scale = cell_size * 2 / 512

        ## Imagens
        up_arrow = Sprite(self.window.resources.images.get("seta"), scale = scale, center_x = width * 0.5 + cell_size * 3.5, center_y = height * 0.75 + cell_size * 1.05)
        down_arrow = Sprite(self.window.resources.images.get("seta"), scale = scale, center_x = width * 0.5 + cell_size * 3.5, center_y = height * 0.75 - cell_size * 1.05, angle = 180)
        left_arrow = Sprite(self.window.resources.images.get("seta"), scale = scale, center_x = width * 0.5 + cell_size * 1.4, center_y = height * 0.75 - cell_size * 1.05, angle = 90)
        right_arrow = Sprite(self.window.resources.images.get("seta"), scale = scale, center_x = width * 0.5 + cell_size * 5.6, center_y = height * 0.75 - cell_size * 1.05, angle = -90)
        escape = Sprite(self.window.resources.images.get("esc"), scale = scale, center_x = width * 0.5 + cell_size * 1.5, center_y = height * 0.25)

        ## Lista de imagens
        self._images = SpriteList()
        self._images.append(up_arrow)
        self._images.append(down_arrow)
        self._images.append(left_arrow)
        self._images.append(right_arrow)
        self._images.append(escape)

        # UI do jogo
        ## Área de texto do score
        self._score_text = TextArea("000", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("button"))

        ## Gerenciador de UI com elemento de ancoragem para centralizar no centro e acima
        self._ui_manager = UIManager()
        self._ui_manager.add(UIAnchorWidget(child = self._score_text, anchor_x = "center", anchor_y = "top"))

        # Menu de pausa
        ## Areas de texto
        game = TextArea("Jogo", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("title") * 0.75)
        paused = TextArea("Pausado", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("title") * 0.75)

        ## Estilo dos botões
        button_style = Button.ButtonStyle(self.window.resources.fonts.get("button").name, self.window.properties.fonts_sizes.get("button"))

        ## Botões
        main_menu = Button("Menu Principal", button_style, self.window, Scene.MAIN_MENU)
        restart = Button("Reiniciar", button_style, self.window, Scene.PLAYING)

        ## Box layout para conter e alinhar os botões na horizontal
        horizontal_box = UIBoxLayout(vertical = False, space_between = 10)
        horizontal_box.add(main_menu)
        horizontal_box.add(restart)

        ## Box layout para conter e alinhar o texto e os botões na vertical
        box = UIBoxLayout(space_between = 10)
        box.add(game)
        box.add(paused)
        box.add(horizontal_box)

        ## Gerenciador de UI com elemento de ancoragem para centralizar tudo
        self._pause_ui_manager = UIManager()
        self._pause_ui_manager.add(UIAnchorWidget(child = box))

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

    def on_update(self, delta_time: float):
        """ Chama da ao atualizar """

        # Verifica se está pausado
        if not self._started or self._paused:
            return

        # Lógica para testar se já deu o tempo de atualizar
        self._delta_time += delta_time

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

                self._score_text.text = f"{self._snake.size - 2}00"
                self._score_text.fit_content()

                if self._snake.size < self._board.cells_count:
                    self._food = self._board.generate_food()
                else:
                    self._food = None
                    self._paused = True # Gambiarra, retirar
                pass
            case Content.BODY:
                self._paused = True # Gambiarra, retirar
                self._snake._lock_direction = False # Gambiarra, retirar
                pass
            case _:
                self._snake.move(next_cell)
                pass

    def on_key_press(self, symbol: int, modifiers: int):
        """ Chamada ao pressionar uma tecla """

        # Lógica para pausar
        if self._started and symbol == ESCAPE:
            self._paused = False if self._paused else True

            if self._paused:
                self._pause_ui_manager.enable()
            else:
                self._pause_ui_manager.disable()

        # Lógica para mudar a direção de movimento
        try:
            self._snake.direction = Direction(symbol) if not self._paused else self._snake.direction
            self._started = True
        except:
            pass

    def on_draw(self) -> None:
        """ Chamada sempre ao desenhar """

        # Desenha o plano de fundo
        self.window.draw_background(True)

        # Desenha a comida e a cobra
        self._food.on_draw()
        self._snake.on_draw()

        # Denhea a UI na tela
        self._ui_manager.draw()

        # Desenha as intruções iniciais
        if not self._started:
            width = self.window.properties.width
            height = self.window.properties.height
            cell_size = self.window.properties.cell_size

            # Instruções para movimento
            draw_text("Use", width * 0.5 - cell_size * 3, height * 0.75, (0, 0, 0), self.window.properties.fonts_sizes.get("body"), font_name = self.window.resources.fonts.get("body").name, anchor_x = "center", anchor_y = "center")
            draw_text("para se mover", width * 0.5, height * 0.75 - cell_size * 3, (0, 0, 0), self.window.properties.fonts_sizes.get("body"), font_name = self.window.resources.fonts.get("body").name, anchor_x = "center", anchor_y = "center")

            # Instruções para pausar
            draw_text("Use", width * 0.5 - cell_size * 3, height * 0.25, (0, 0, 0), self.window.properties.fonts_sizes.get("body"), font_name = self.window.resources.fonts.get("body").name, anchor_x = "center", anchor_y = "center")
            draw_text("para pausar o jogo", width * 0.5, height * 0.25 - cell_size * 3, (0, 0, 0), self.window.properties.fonts_sizes.get("body"), font_name = self.window.resources.fonts.get("body").name, anchor_x = "center", anchor_y = "center")

            # Imagens
            self._images.draw()

        # Desenha o menu de pausa
        if self._paused:
            self._pause_ui_manager.draw()
            pass

# Export padrão
__all__ = ["Playing"]

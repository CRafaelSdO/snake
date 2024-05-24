""" Módulo da tela de jogo """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import Sprite, View, Window
from arcade.gui import UIAnchorWidget, UIBoxLayout, UIManager
from arcade.key import ESCAPE

# Imports de pacotes locais
from .entities import *
from .gui import *
from .scenes import *
from .speeds import *

class Playing(View):
    """ Define uma tela de jogo """

    def __init__(self, window: Optional[Window]) -> None:
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

        # Controle se o jogo está pausado
        self._paused: bool = True

        # Tempo decorrido desde a última atualização
        self._delta_time: float = 0

        # Gerenciador de UI
        self._ui_manager: UIManager = None

        # Controla se os objetos do menu já foram criados
        self._setup: bool = False

    def setup(self, speed: Speed) -> None:
        """ Configura a tela de jogo"""

        # Configura o campo, a cobra e a primeira comida
        self._board = Board(self.window.properties)
        self._snake = Snake(self._board)
        self._food = self._board.generate_food()

        # Configura a velocidade da cobra
        self._speed = speed if speed else self._speed

        if self._setup:
            return

        # Texto das instruções
        use = TextArea("Use", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body"))
        to_move = TextArea("para se mover", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body"))

        # Imagem
        directional = Sprite(self.window.resources.images.get("directional"))

        # Box layout para conter os objetos
        box = UIBoxLayout(space_between = 10)
        box.add(use)
        #box.add(directional)
        box.add(to_move)

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

    def on_update(self, delta_time: float):
        """ Chama da ao atualizar """

        # Verifica se está pausado
        if self._paused:
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

                if self._snake.size < self._board.cells_count:
                    self._food = self._board.generate_food()
                else:
                    self._food = None
                    self._paused = True
                pass
            case Content.BODY:
                self._paused = True
                self._snake._lock_direction = False # Gambiarra, retirar
                pass
            case _:
                self._snake.move(next_cell)
                pass

    def on_key_press(self, symbol: int, modifiers: int):
        """ Chamada ao pressionar uma tecla """

        try:
            self._snake.direction = Direction(symbol)
            self._paused = False
        except:
            if symbol == ESCAPE:
                self._paused = False if self._paused else True

    def on_draw(self) -> None:
        """ Chamada sempre ao desenhar """

        # Desenha o plano de fundo
        self.window.draw_background(True)

        # Desenha a comida e a cobra
        self._food.on_draw()
        self._snake.on_draw()

        # Desenha o menu de pausa
        if self._paused:
            self._ui_manager.draw()
            pass


# Export padrão
__all__ = ["Playing"]

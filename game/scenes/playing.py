""" Módulo da tela de jogo """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import draw_rectangle_filled, View, Window
from arcade.key import ESCAPE

# Imports de pacotes locais
from .entities import *
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

    def setup(self) -> None:
        """ Configura a tela de jogo"""

        # Configura o campo, a cobra e a primeira comida
        self._board = Board(self.window.properties)
        self._snake = Snake(self._board)
        self._food = self._board.generate_food()

        # Configura a velocidade da cobra
        self._speed = self.window.speed

    def on_show_view(self) -> None:
        """ Chamada uma vez ao entrar nessa cena """

        # Muda a cor de fundo
        self.window.background_color = (148, 202, 73)

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
                self._snake.grow(next_cell)

                if self._snake.size < self._board.cells_count:
                    self._food = self._board.generate_food()
                else:
                    self._food = None
                    self._snake.direction = None

                pass
            case Content.BODY:
                self._snake.direction = None
                pass
            case _:
                self._snake.move(next_cell)
                pass

    def on_key_press(self, symbol: int, modifiers: int):
        """ Chamada ao pressionar uma tecla """

        if Direction(symbol):
            self._paused = not self._paused if self._paused else self._paused
            self._snake.direction = Direction(symbol)
        elif symbol == ESCAPE:
            self._paused = self._paused if self._paused else not self._paused

    def on_draw(self) -> None:
        """ Chamada sempre ao desenhar """

        # Limpa a tela
        self.clear()

        # Lógica para desenhar um plano de fundo quadriculado
        cell_size = self.window.properties.cell_size
        rows = self.window.properties.height // cell_size
        columns = self.window.properties.width // cell_size

        for row in range(rows):
            start = 1 if not row & 1 else 0

            for column in range(start, columns, 2):
                draw_rectangle_filled(cell_size / 2 + column  * cell_size, cell_size / 2 + row * cell_size, cell_size, cell_size, (172, 215, 86))

        # Desenha a comida e a cobra
        self._food.on_draw()
        self._snake.on_draw()


# Export padrão
__all__ = ["Playing"]

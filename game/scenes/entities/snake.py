""" Módulo da cobra """

# Imports de pacotes locais
from .board import *
from .cell import *
from .cell_contents import *
from .directions import *

class Snake():
    """ Define um campo """

    def __init__(self, board: Board) -> None:
        """ Inicializa uma cobra """

        # Lógica do corpo inicial da cobrinha
        ## Cabeça
        head = board.center_cell
        head.content = CellContent.SNAKE

        ## Cauda
        tail = board.get_next_cell(head, Direction.RIGHT)
        tail.content = CellContent.SNAKE

        # Corpo da cobrinha
        self._cells: list[Cell] = [head, tail]

        # Direção do movimento da cobrinha
        self._direction: Direction = None

# Export padrão
__all__ = ["Snake"]

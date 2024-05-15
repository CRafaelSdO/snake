""" Módulo do campo de jogo """

# Imports de pacotes locais
from ...properties import *
from .cell import *
from .directions import *

class Board():
    """ Define um campo """

    def __init__(self, properties: GameProperties) -> None:
        """ Inicializa um campo """

        # Total de linhas e colunas no campo
        self._rows: int = properties.height // properties.cell_size
        self._columns: int = properties.width // properties.cell_size

        # Células do campo
        self._cells: list[list[Cell]] = [[Cell(row, column, properties.cell_size) for column in range(self._columns)] for row in range(self._rows)]

    @property
    def center_cell(self) -> Cell:
        """ Celula no centro deste campo """

        row = self._rows // 2
        column = self._columns // 2

        if not self._rows & 1:
            row -= 1

        if not self._columns & 1:
            column -= 1

        return self._cells[row][column]

    def get_next_cell(self, cell: Cell, direcction: Direction) -> Cell:
        """ Retorna a célula vizinha em uma direção"""

        row, column = cell.position

        match(direcction):
            case Direction.UP:
                row = (row + 1) % self._rows
                pass
            case Direction.DOWN:
                row = self._rows - 1 if row - 1 < 0 else row - 1
                pass
            case Direction.LEFT:
                column = self._columns - 1 if column - 1 < 0 else column - 1
                pass
            case Direction.RIGHT:
                column = (column + 1) % self._columns
                pass
            case _:
                pass

        return self._cells[row][column]

# Export padrão
__all__ = ["Board"]

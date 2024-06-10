""" Módulo do campo de jogo """

# Imports de pacotes BuiltIn
from random import randrange

# Imports de pacotes locais
from ...properties import Properties
from .cell import Cell
from .contents import Content
from .directions import Direction

class Board():
    """ Define um campo """

    def __init__(self, properties: Properties) -> None:
        """ Inicializa um campo """

        # Total de linhas e colunas no campo
        self._rows: int = 30
        self._columns: int = 30

        cell_size = properties.cell_size
        margin = properties.margin

        # Células do campo
        self._cells: list[list[Cell]] = [[Cell(row, column, cell_size, margin) for column in range(self._columns)] for row in range(self._rows)]

    @property
    def center_cell(self) -> Cell:
        """ Celula no centro deste campo """

        row = self._rows // 2
        column = self._columns // 2

        # Caso não exista uma célula central será escolhida a célula a esquerda e abaixo
        if not self._rows & 1:
            row -= 1

        if not self._columns & 1:
            column -= 1

        return self._cells[row][column]

    @property
    def cells_count(self) -> int:
        """ Quantidade total de células neste campo """

        return self._rows * self._columns

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
                return None

        return self._cells[row][column]

    def generate_food(self) -> Cell:
        """ Gera comida em uma célula vazia """

        # Lógica para asegurar que está escolhendo uma célula vazia
        row = randrange(self._rows)
        column = randrange(self._columns)

        while self._cells[row][column].content != Content.EMPTY:
            row = randrange(self._rows)
            column = randrange(self._columns)

        # Configura o conteúdo
        self._cells[row][column].content = Content.FOOD

        return self._cells[row][column]

""" Módulo das células do campo de jogo """

# Imports de pacotes locais
from .cell_contents import *

class Cell():
    """ Define uma célula do tabuleiro """

    def __init__(self, x: float, y: float, row: int, column: int) -> None:
        """ Inicializa uma célula """

        self._x = x
        self._y = y
        self._row = row
        self._column = column

# Export padrão
__all__ = ["Cell"]

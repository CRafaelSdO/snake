""" Módulo dos conteúdos das células """

# Imports de pacotes BuiltIn
from enum import Enum

class CellContent(Enum):
    """ Enumera os conteúdos das células """

    EMPTY = 0
    FOOD = 1
    SNAKE = 2

# Export padrão
__all__ = ["CellContent"]

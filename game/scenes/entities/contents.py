""" Módulo dos conteúdos das células """

# Imports de pacotes BuiltIn
from enum import Enum

class Content(Enum):
    """ Enumera os conteúdos das células """

    EMPTY = 0
    FOOD = 1
    HEAD = 2
    BODY = 3
    TAIL = 4

# Export padrão
__all__ = ["Content"]

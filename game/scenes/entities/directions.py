""" Módulo das direções da cobra """

# Imports de pacotes BuiltIn
from enum import Enum

class Direction(Enum):
    """ Enumera as direções da cobra """

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

# Export padrão
__all__ = ["Direction"]

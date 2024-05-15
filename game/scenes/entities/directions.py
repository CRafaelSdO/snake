""" Módulo das direções da cobra """

# Imports de pacotes externos
from arcade.key import UP, DOWN, LEFT, RIGHT

# Imports de pacotes BuiltIn
from enum import Enum

class Direction(Enum):
    """ Enumera as direções da cobra """

    UP = UP
    DOWN = DOWN
    LEFT = LEFT
    RIGHT = RIGHT

# Export padrão
__all__ = ["Direction"]

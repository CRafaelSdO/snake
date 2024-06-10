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

def opposite(direction: Direction) -> Direction:
    match(direction):
        case Direction.UP:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.UP
        case Direction.LEFT:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.LEFT
        case _:
            return None

""" Módulo dos indexes das sprites """

# Imports de pacotes BuiltIn
from enum import Enum
from typing import Optional

# Imports de pacotes locais
from .contents import Content
from .directions import Direction

class SpriteIndex(Enum):
        """ Enumeração dos índices das sprites """

        HEAD_LEFT = 0
        HEAD_UP = 1
        HEAD_RIGHT = 2
        HEAD_DOWN = 3
        TAIL_LEFT = 4
        TAIL_UP = 5
        TAIL_RIGHT = 6
        TAIL_DOWN = 7
        BODY_000_090 = 8
        BODY_090_180 = 9
        BODY_180_270 = 10
        BODY_270_360 = 11
        BODY_HORIZONTAL = 12
        BODY_VERTICAL = 13
        FOOD = 14

def get_texture_index(content: Content, front: Optional[Direction] = None, back: Optional[Direction] = None) -> SpriteIndex:
    """ Retorna o índice da textura com base no conteúdo, fernte e costas """

    match(content):
        case Content.FOOD:
            texture_index = SpriteIndex.FOOD
            pass
        case Content.HEAD:
            match(front):
                case Direction.UP:
                    texture_index = SpriteIndex.HEAD_UP
                    pass
                case Direction.DOWN:
                    texture_index = SpriteIndex.HEAD_DOWN
                    pass
                case Direction.LEFT:
                    texture_index = SpriteIndex.HEAD_LEFT
                    pass
                case Direction.RIGHT:
                    texture_index = SpriteIndex.HEAD_RIGHT
                    pass
            pass
        case Content.BODY:
            match(front, back):
                case (Direction.UP, Direction.DOWN) | (Direction.DOWN, Direction.UP):
                    texture_index = SpriteIndex.BODY_VERTICAL
                    pass
                case (Direction.UP, Direction.LEFT) | (Direction.LEFT, Direction.UP):
                    texture_index = SpriteIndex.BODY_270_360
                    pass
                case (Direction.UP, Direction.RIGHT) | (Direction.RIGHT, Direction.UP):
                    texture_index = SpriteIndex.BODY_180_270
                    pass
                case (Direction.DOWN, Direction.LEFT) | (Direction.LEFT, Direction.DOWN):
                    texture_index = SpriteIndex.BODY_000_090
                    pass
                case (Direction.DOWN, Direction.RIGHT) | (Direction.RIGHT, Direction.DOWN):
                    texture_index = SpriteIndex.BODY_090_180
                    pass
                case (Direction.LEFT, Direction.RIGHT) | (Direction.RIGHT, Direction.LEFT):
                    texture_index = SpriteIndex.BODY_HORIZONTAL
                    pass
            pass
        case Content.TAIL:
            match(front):
                case Direction.UP:
                    texture_index = SpriteIndex.TAIL_UP
                    pass
                case Direction.DOWN:
                    texture_index = SpriteIndex.TAIL_DOWN
                    pass
                case Direction.LEFT:
                    texture_index = SpriteIndex.TAIL_LEFT
                    pass
                case Direction.RIGHT:
                    texture_index = SpriteIndex.TAIL_RIGHT
                    pass
            pass

    return texture_index

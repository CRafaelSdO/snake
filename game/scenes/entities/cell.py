""" Módulo das células do campo """

# Imports de pacotes externos
from arcade import draw_circle_filled, draw_rectangle_filled, SpriteList

# Imports de pacotes locais
from .contents import Content
from .directions import Direction
from .game_sprite import GameSprite
from .sprite_index import get_texture_index

class Cell():
    """ Define uma célula do campo """

    def __init__(self, row: int, column: int, size: int, margin: float) -> None:
        """ Inicializa uma célula """

        # Posição desta célula no campo
        self._row: int = row
        self._column: int = column

        # Conteúdo desta célula
        self._content: Content = Content.EMPTY

        # Direções nesta célula
        self._front: Direction = None
        self._back: Direction = None

        # Centro de desenho desta célula
        self._x: float = size / 2 + column * size + margin
        self._y: float = size / 2 + row * size + (size / 2 if margin != 0 else 0)

        # Tamanho de desenho da célula
        self._size: float = size

        # Sprite desta célula
        self._sprite: GameSprite = None

    @property
    def position(self) -> tuple[int, int]:
        """ Posição desta célula no campo """

        return self._row, self._column

    @property
    def front(self) -> Direction:
        """ Frente desta célula """

        return self._front

    @front.setter
    def front(self, direction: Direction) -> None:

        self._front = direction

    @property
    def back(self) -> Direction:
        """ Costas desta célula """

        return self._front, self._back

    @back.setter
    def back(self, direction: Direction) -> None:

        self._back = direction

    @property
    def content(self) -> Content:
        """ O conteúdo desta célula """

        return self._content

    @content.setter
    def content(self, content: Content) -> None:
        if content == Content.EMPTY:
            self._sprite.visible = False
        else:
            self._sprite.visible = True
            self._sprite.set_texture(get_texture_index(content, self._front, self._back).value)

        self._content = content

    def setup(self, sprite_list: SpriteList, sprites_file: str) -> None:
        """ Carrega a sprite para esta célula """

        self._sprite = GameSprite(sprites_file, self._size, self._x, self._y)

        sprite_list.append(self._sprite)

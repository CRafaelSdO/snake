""" Módulo das células do campo """

# Imports de pacotes externos
from arcade import draw_circle_filled, draw_rectangle_filled

# Imports de pacotes locais
from .contents import *

class Cell():
    """ Define uma célula do campo """

    def __init__(self, row: int, column: int, size: int) -> None:
        """ Inicializa uma célula """

        # Posição desta célula no campo
        self._row: int = row
        self._column: int = column

        # Conteúdo desta célula
        self._content: Content = Content.EMPTY

        # Centro de desenho desta célula
        self._x: float = size / 2 + column * size
        self._y: float = size / 2 + row * size

        # Tamanho de desenho da célula
        self._size: float = size

    @property
    def position(self) -> tuple[int, int]:
        """ Posição desta célula no campo """

        return self._row, self._column

    @property
    def content(self) -> Content:
        """ O conteúdo desta célula """

        return self._content
    
    @content.setter
    def content(self, content: Content) -> None:
        self._content = content

    def on_draw(self) -> None:
        """ Chamada quando está célula deve ser desenhada """

        match(self.content):
            case Content.EMPTY:
                pass
            case Content.FOOD:
                draw_circle_filled(self._x, self._y, self._size / 2, (255, 0, 0))
                pass
            case _:
                draw_rectangle_filled(self._x, self._y, self._size, self._size, (255, 121, 0))

# Export padrão
__all__ = ["Cell"]

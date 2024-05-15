""" Módulo da cobra """

# Imports de pacotes locais
from .board import *
from .cell import *
from .contents import *
from .directions import *

class Snake():
    """ Define um campo """

    def __init__(self, board: Board) -> None:
        """ Inicializa uma cobra """

        # Lógica do corpo inicial da cobrinha
        ## Cabeça
        head = board.center_cell
        head.content = Content.HEAD

        ## Cauda
        tail = board.get_next_cell(head, Direction.RIGHT)
        tail.content = Content.TAIL

        # Corpo da cobrinha
        self._body: list[Cell] = [head, tail]

        # Direção do movimento da cobrinha
        self._direction: Direction = None

    @property
    def head(self) -> Cell:
        """ A cabeça da cobra """

        return self._body[0]
    
    @property
    def tail(self) -> Cell:
        """ A cabeça da cobra """

        return self._body[-1]

    @property
    def direction(self) -> Direction:
        """ A cabeça da cobra """

        return self._direction

    @direction.setter
    def direction(self, direction: Direction) -> None:
        self._direction = direction

    def grow(self, food: Cell) -> None:
        """ Chamada quando a cobra deve crescer (comer) """

        # Incorpora a célula com comida como cabeça
        self.head.content = Content.BODY
        food.content = Content.HEAD
        self._body.insert(0, food)

    def move(self, next_cell: Cell) -> None:
        """ Chamada quando a cobra deve se mover """

        # Move a cabeça
        self.head.content = Content.BODY
        next_cell.content = Content.HEAD
        self._body.insert(0, next_cell)

        # Move a cauda
        self.tail.content = Content.EMPTY
        self._body.pop()
        self.tail.content = Content.TAIL

    def on_draw(self) -> None:
        """ Chamada quando está cobra deve ser desenhada """

        for cell in self._body:
            cell.on_draw()

# Export padrão
__all__ = ["Snake"]

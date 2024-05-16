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

        # Controle se pode mudar a direção do movimento
        self._lock_direction: bool = False

    @property
    def head(self) -> Cell:
        """ A cabeça da cobra """

        return self._body[0]
    
    @property
    def tail(self) -> Cell:
        """ A cabeça da cobra """

        return self._body[-1]

    @property
    def size(self) -> int:
        """ O tamanho desta cobra """

        return len(self._body)

    @property
    def direction(self) -> Direction:
        """ A cabeça da cobra """

        return self._direction

    @direction.setter
    def direction(self, direction: Direction) -> None:
        if self._lock_direction or direction == opposite(self._direction):
            return
        
        self._direction = direction

        # Não podemos mudar de direção antes de se mover ou comer
        self._lock_direction = True

    def eat(self, food: Cell) -> None:
        """ Chamada quando a cobra deve crescer (comer) """

        # Incorpora a célula com comida como cabeça
        self.head.content = Content.BODY
        food.content = Content.HEAD
        self._body.insert(0, food)

        # Agora podemos mudar de direção novamente
        self._lock_direction = False

    def move(self, next_cell: Cell) -> None:
        """ Chamada quando a cobra deve se mover """

        # Move a cabeça
        self.head.content = Content.BODY
        next_cell.content = Content.HEAD
        self._body.insert(0, next_cell)

        # Move a cauda
        self.tail.content = Content.EMPTY if self.tail.content == Content.TAIL else self.tail.content
        self._body.pop()
        self.tail.content = Content.TAIL

        # Agora podemos mudar de direção novamente
        self._lock_direction = False

    def on_draw(self) -> None:
        """ Chamada quando está cobra deve ser desenhada """

        for cell in self._body:
            cell.on_draw()

# Export padrão
__all__ = ["Snake"]

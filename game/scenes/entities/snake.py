""" Módulo da cobra """

# Imports de pacotes locais
from .board import Board
from .cell import Cell
from .contents import Content
from .directions import Direction, opposite

class Snake():
    """ Define um campo """

    def __init__(self) -> None:
        """ Inicializa uma cobra """

        # Corpo da cobrinha
        self._body: list[Cell] = None

        # Direção do movimento da cobrinha
        self._direction: Direction = None

        # Controle se pode mudar a direção do movimento
        self._lock_direction: bool = None

    @property
    def head(self) -> Cell:
        """ A cabeça desta cobra """

        return self._body[0]

    @property
    def neck(self) -> Cell:
        """ A celula logo apos a cabeça desta cobra """

        return self._body[1]

    @property
    def tail(self) -> Cell:
        """ A cauda desta cobra """

        return self._body[-1]

    @property
    def size(self) -> int:
        """ O tamanho desta cobra """

        return len(self._body)

    @property
    def direction(self) -> Direction:
        """ A direção do movimento desta cobra """

        return self._direction

    @direction.setter
    def direction(self, direction: Direction) -> None:
        if self._lock_direction or direction == opposite(self._direction):
            return

        # Muda a direção do movimento
        self._direction = direction

        # Não podemos mudar de direção antes de se mover ou comer
        self._lock_direction = True

    def _set_head_directions(self) -> None:
        """ Define as direções na cabeça da cobra """

        self.head.front = self._direction
        self.head.back = opposite(self.neck.front)

    def setup(self, board: Board) -> None:
        """ Configura esta cobra """

        # Lógica do corpo inicial da cobrinha
        ## Cabeça
        head = board.center_cell
        head.front = Direction.LEFT
        head.content = Content.HEAD

        ## Cauda
        tail = board.get_next_cell(head, Direction.RIGHT)
        tail.front = Direction.LEFT
        tail.content = Content.TAIL

        # Corpo da cobrinha
        self._body = [head, tail]

        # Define que pode mudar a direção do movimento
        self._lock_direction: bool = False

    def eat(self, food: Cell) -> None:
        """ Chamada quando a cobra deve crescer (comer) """

        # Lógica para incluir a comida no corpo
        ## Transforma a cabeça atual em corpo
        self._set_head_directions()
        self.head.content = Content.BODY

        ## Insere e configura a comida na frente da cabeça
        self._body.insert(0, food)
        self._set_head_directions()
        food.content = Content.HEAD

        # Agora podemos mudar de direção novamente
        self._lock_direction = False

    def move(self, next_cell: Cell) -> None:
        """ Chamada quando a cobra deve se mover """

        # Lógica para incluir a próxima celúla no corpo
        ## Transforma a cabeça atual em corpo
        self._set_head_directions()
        self.head.content = Content.BODY

        # Insere e configura a próxima célula na frente da cabeça
        self._body.insert(0, next_cell)
        self._set_head_directions()
        next_cell.content = Content.HEAD

        # Retira a cauda atual e configura a nova
        self.tail.content = Content.EMPTY if self.tail.content == Content.TAIL else self.tail.content
        self._body.pop()
        self.tail.content = Content.TAIL

        # Agora podemos mudar de direção novamente
        self._lock_direction = False

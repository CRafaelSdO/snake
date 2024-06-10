"""
Pacote das entidades do jogo

Export Padrão:
* Board
* Cell
* Content
* Direction
* Snake

Imports disponíveis:
* Board
* Cell
* Content
* Direction
* oposite
* Snake
"""

# Imports dos módulos
from .board import Board
from .cell import Cell
from .contents import Content
from .directions import Direction, opposite
from .snake import Snake

# Export padrão
__all__ = ["Board", "Cell" , "Content", "Direction", "Snake"]

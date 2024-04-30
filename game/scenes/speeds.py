""" Módulo das velocidades do jogo """

# Imports de pacotes BuiltIn
from enum import Enum

class GameSpeed(Enum):
    """ Enumera as velocidades do jogo """
    
    VERY_EASY = 2
    EASY = 4
    MEDIUM = 6
    HARD = 8
    EXTREME = 10

# Export padrão
__all__ = ["GameSpeed"]

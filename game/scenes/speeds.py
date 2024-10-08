""" Módulo das velocidades do jogo """

# Imports de pacotes BuiltIn
from enum import Enum

class Speed(Enum):
    """ Enumera as velocidades (dificuldades) do jogo """

    VERY_EASY = 2
    EASY = 4
    MEDIUM = 6
    HARD = 8
    EXTREME = 10

""" Módulo das cenas do jogo """

# Imports de pacotes BuiltIn
from enum import Enum

class Scene(Enum):
    """ Enumera as cenas do jogo """
    
    MAIN_MENU = 0
    PLAY_MENU = 1
    RANKING_MENU = 2
    SETTINGS_MENU = 3
    PLAYING = 4
    GAME_OVER_MENU = 5

# Export padrão
__all__ = ["Scene"]

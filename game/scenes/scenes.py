""" Módulo das cenas do jogo """

# Imports de pacotes BuiltIn
from enum import Enum

class GameScene(Enum):
    """ Enumera as cenas do jogo """
    
    MAIN_MENU = 0
    PLAY_MENU = 1
    RANKING_MENU = 2
    SETTINGS_MENU = 3
    PLAYING = 4

# Export padrão
__all__ = ["GameScene"]

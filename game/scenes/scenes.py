""" Módulo das cenas do jogo """

# Imports de pacotes BuiltIn
from enum import Enum

class GameScene(Enum):
    """ Enumera as cenas do jogo """
    
    MAIN_MENU = 0

# Export padrão
__all__ = ["GameScene"]

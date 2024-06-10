""" Módulo das cenas do jogo """

# Imports de pacotes BuiltIn
from enum import Enum

class Scene(Enum):
    """ Enumera as cenas do jogo """

    CLOSE = 0
    GAME_OVER_MENU = "GameOverMenu"
    MAIN_MENU = "MainMenu"
    PLAY_MENU = "PlayMenu"
    PLAYING = "Playing"
    RANKING_MENU = "RankingMenu"
    SAVE_SCORE = 1
    SWITCH_FULL_SCREEN = 2

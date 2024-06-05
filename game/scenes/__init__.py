""" Pacote das cenas do jogo """

# Imports dos módulos
from .base_scene import *
from .game_over_menu import *
from .main_menu import *
from .play_menu import *
from .playing import *
from .ranking_menu import *
from .scenes import *
from .speeds import *

# Export padrão
__all__ = ["GameOverMenu", "MainMenu", "PlayMenu", "Playing", "RankingMenu", "Scene", "Speed"]

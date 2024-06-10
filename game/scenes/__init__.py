"""
Pacote das cenas do jogo

Export Padrão:
* BaseScene
* Scene
* get_scene
* Speed

Imports disponíveis:
* BaseScene
* GameOverMenu
* MainMenu
* PlayMenu
* Playing
* RankingMenu
* Scene
* Speed
"""

# Imports dos módulos
from .base_scene import BaseScene
from .game_over_menu import GameOverMenu
from .main_menu import MainMenu
from .play_menu import PlayMenu
from .playing import Playing
from .ranking_menu import RankingMenu
from .scenes import Scene
from .speeds import Speed

def get_scene_class(name: Scene) -> BaseScene:
    """ Retorna uma cena pelo nome """

    match(name.value):
        case MainMenu.__name__:
            return MainMenu

        case PlayMenu.__name__:
            return PlayMenu

        case RankingMenu.__name__:
            return RankingMenu

        case Playing.__name__:
            return Playing

        case GameOverMenu.__name__:
            return GameOverMenu
        
        case _:
            return None

# Export padrão
__all__ = ["BaseScene", "Scene", "get_scene_class", "Speed"]

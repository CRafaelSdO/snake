""" Módulo da janela """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import Window

# Imports de pacotes locais
from .properties import *
from .resources import *
from .scenes import *
from .scenes.menus import *

class GameWindow(Window):
    """ Define uma janela """
    
    def __init__(self, properties: Optional[GameProperties] = GameProperties(), resources: Optional[GameResources] = GameResources()) -> None:
        """ Inicializa uma janela """
        
        super().__init__(properties.width, properties.height, properties.title, properties.fullscreen, center_window = properties.center_window)

        # Propriedades
        self._properties = properties
        
        # Recursos
        self._resources = resources

        # Última cena e cena atual
        self._last_scene: GameScene = None
        self._current_scene: GameScene = None

        # Cenas
        self._main_menu: MainMenu = None
    
    def setup(self) -> None:
        """ Configura a janela """

        # Carrega as fontes
        self._resources.load_all_fonts()

        # Inicializa as cenas
        self._main_menu = MainMenu(self)

        # Inicia o ciclo das cenas
        self.switch_scene(GameScene.MAIN_MENU)

    def switch_scene(self, next_scene: GameScene) -> None:
        """ Faz a mudança de cena """

        self._last_scene, self._current_scene = self._current_scene, next_scene

        match(self._current_scene):
            case GameScene.MAIN_MENU:
                pass
            case _:
                pass

# Exportação padrão
__all__ = ["GameWindow"]

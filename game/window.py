""" Módulo da janela """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import Window

# Imports de pacotes locais
from .properties import *
from .resources import *
from .scenes import *

class GameWindow(Window):
    """ Define uma janela """
    
    def __init__(self, properties: Optional[GameProperties] = GameProperties(), resources: Optional[GameResources] = GameResources()) -> None:
        """ Inicializa uma janela """
        
        super().__init__(properties.width, properties.height, properties.title, properties.fullscreen, center_window = properties.center_window)

        # Propriedades
        self._properties: GameProperties = properties
        
        # Recursos
        self._resources: GameResources = resources

        # Última cena e cena atual
        self._last_scene: GameScene = None
        self._current_scene: GameScene = None

        # Velocidade da cena de jogo
        self._speed: GameSpeed = None

        # Cenas
        self._main_menu: MainMenu = None
        self._play_menu: PlayMenu =None

    @property
    def properties(self) -> GameProperties:
        return self._properties
    
    @property
    def resources(self) -> GameResources:
        return self._resources
    
    @property
    def last_scene(self) -> GameScene:
        return self._last_scene
    
    @property
    def speed(self) -> GameSpeed:
        return self._speed
    
    @speed.setter
    def speed(self, speed: GameSpeed):
        self._speed = speed
    
    def setup(self) -> None:
        """ Configura a janela """

        # Carrega as fontes
        self._resources.load_all_fonts()

        # Inicializa as cenas
        self._main_menu = MainMenu(self)
        self._play_menu = PlayMenu(self)

        # Inicia o ciclo das cenas
        self.switch_scene(GameScene.MAIN_MENU)

    def switch_scene(self, next_scene: GameScene) -> None:
        """ Faz a mudança de cena """

        self._last_scene, self._current_scene = self._current_scene, next_scene

        print(f"scene: {self._current_scene}\nspeed: {self._speed}")

        match(self._current_scene):
            case GameScene.MAIN_MENU:
                self._main_menu.setup()
                self.show_view(self._main_menu)
                pass
            case GameScene.PLAY_MENU:
                self._play_menu.setup()
                self.show_view(self._play_menu)
                pass
            case GameScene.RANKING_MENU:
                self._last_scene, self._current_scene = self._current_scene, self._last_scene
                pass
            case GameScene.SETTINGS_MENU:
                self._last_scene, self._current_scene = self._current_scene, self._last_scene
                pass
            case GameScene.PLAYING:
                self._last_scene, self._current_scene = self._current_scene, self._last_scene
                pass
            case _:
                pass

# Exportação padrão
__all__ = ["GameWindow"]

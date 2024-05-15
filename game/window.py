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

    def __init__(self, properties: Optional[Properties] = Properties(), resources: Optional[Resources] = Resources()) -> None:
        """ Inicializa uma janela """

        super().__init__(properties.width, properties.height, properties.title, properties.fullscreen, center_window = properties.center_window)

        # Propriedades
        self._properties: Properties = properties

        # Recursos
        self._resources: Resources = resources

        # Última cena e cena atual
        self._last_scene: Scene = None
        self._current_scene: Scene = None

        # Velocidade da cena de jogo
        self._speed: Speed = None

        # Cenas
        self._main_menu: MainMenu = None
        self._play_menu: PlayMenu = None
        self._playing: Playing = None

    @property
    def properties(self) -> Properties:
        """ As propriedades desta janela """

        return self._properties

    @property
    def resources(self) -> Resources:
        """ Os recursos desta janela """

        return self._resources

    @property
    def last_scene(self) -> Scene:
        """ A última cena """

        return self._last_scene

    @property
    def speed(self) -> Speed:
        """ A velocidade do jogo """

        return self._speed

    @speed.setter
    def speed(self, speed: Speed) -> None:
        self._speed = speed

    def setup(self) -> None:
        """ Configura a janela """

        # Carrega as fontes
        self._resources.load_all_fonts()

        # Inicializa as cenas
        self._main_menu = MainMenu(self)
        self._play_menu = PlayMenu(self)
        self._playing = Playing(self)

        # Inicia o ciclo das cenas
        self.switch_scene(Scene.MAIN_MENU)

    def switch_scene(self, next_scene: Scene) -> None:
        """ Faz a mudança de cena """

        self._last_scene, self._current_scene = self._current_scene, next_scene

        print(f"scene: {self._current_scene}\nspeed: {self._speed}")

        match(self._current_scene):
            case Scene.MAIN_MENU:
                self._main_menu.setup()
                self.show_view(self._main_menu)
                pass
            case Scene.PLAY_MENU:
                self._play_menu.setup()
                self.show_view(self._play_menu)
                pass
            case Scene.RANKING_MENU:
                self._last_scene, self._current_scene = self._current_scene, self._last_scene
                pass
            case Scene.SETTINGS_MENU:
                self._last_scene, self._current_scene = self._current_scene, self._last_scene
                pass
            case Scene.PLAYING:
                self._playing.setup()
                self.show_view(self._playing)
                pass
            case _:
                pass

# Exportação padrão
__all__ = ["GameWindow"]

""" Módulo da janela """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import draw_rectangle_filled, Window

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

    def setup(self) -> None:
        """ Configura a janela """

        # Configura a cor de fundo
        self.background_color = (148, 202, 73)

        # Carrega as fontes
        self._resources.load_all_fonts()

        # Atualiza as propriedades
        self._properties = self._properties.update(self)

        # Inicializa as cenas
        self._main_menu = MainMenu(self)
        self._play_menu = PlayMenu(self)
        self._playing = Playing(self)

        # Inicia o ciclo das cenas
        self.switch_scene(Scene.MAIN_MENU)

    def switch_scene(self, next_scene: Scene, speed: Optional[Speed] = None) -> None:
        """ Faz a mudança de cena """

        self._last_scene, self._current_scene = self._current_scene, next_scene

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
                self._playing.setup(speed)
                self.show_view(self._playing)
                pass
            case Scene.GAME_OVER_MENU:
                self._last_scene, self._current_scene = self._current_scene, self._last_scene
                pass
            case Scene.CLOSE:
                self.close()
                pass
            case _:
                pass

    def draw_background(self) -> None:
        """ Desenha o plano de fundo da janela """

        # Limpa a tela
        self.clear()

        # Lógica para desenhar um plano de fundo quadriculado
        cell_size = self._properties.cell_size
        rows = self._properties.height // cell_size
        columns = self._properties.width // cell_size

        for row in range(rows):
            start = 1 if not row & 1 else 0

            for column in range(start, columns, 2):
                draw_rectangle_filled(cell_size / 2 + column  * cell_size, cell_size / 2 + row * cell_size, cell_size, cell_size, (172, 215, 86))

# Exportação padrão
__all__ = ["GameWindow"]

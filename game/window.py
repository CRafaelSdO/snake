""" Módulo da janela """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import draw_rectangle_filled, draw_rectangle_outline, Window

# Imports de pacotes locais
from .properties import *
from .ranking import *
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
        self._game_over_menu: GameOverMenu = None
        self._ranking_menu: RankingMenu = None

        # Ranking
        self._ranking: Ranking = None

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
    def ranking(self) -> Ranking:
        """ O ranking atual """

        return self._ranking

    def setup(self) -> None:
        """ Configura a janela """

        # Configura a cor de fundo
        self.background_color = (148, 202, 73)

        # Carrega os resursos
        self._resources.setup()

        # Atualiza as propriedades
        self._properties = self._properties.update(self)

        # Inicializa as cenas
        self._main_menu = MainMenu(self)
        self._play_menu = PlayMenu(self)
        self._playing = Playing(self)
        self._game_over_menu = GameOverMenu(self)
        self._ranking_menu = RankingMenu(self)

        # Carrega o Ranking
        self._ranking = Ranking()

        # Inicia o ciclo das cenas
        self.switch_scene(Scene.MAIN_MENU)
    

    def set_scenes_full_screen(self, full_screen: bool):
        """ Passa para as cenas se a janela está em tela cheia """

        self._main_menu.set_full_screen(full_screen)
        self._play_menu.set_full_screen(full_screen)
        self._ranking_menu.set_full_screen(full_screen)
        self._playing.set_full_screen(full_screen)
        self._game_over_menu.set_full_screen(full_screen)


    def switch_scene(self, next_scene: Scene, speed: Optional[Speed] = None, score: Optional[int] = None) -> None:
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
                self._ranking_menu.setup()
                self.show_view(self._ranking_menu)
                pass
            case Scene.SWITCH_FULL_SCREEN:
                self.set_scenes_full_screen(not self.fullscreen)
                self._properties = self._properties.update(self)
                self.switch_scene(self._last_scene)
                pass
            case Scene.PLAYING:
                self._playing.setup(speed)
                self.show_view(self._playing)
                pass
            case Scene.GAME_OVER_MENU:
                self._game_over_menu.setup(score)
                self.show_view(self._game_over_menu)
                pass
            case Scene.SAVE_SCORE:
                if not self._game_over_menu.saved:
                    name, score = self._game_over_menu.score

                    if name != "":
                        self._ranking.add(name, score)
                        self._game_over_menu.saved = True
                
                self.switch_scene(Scene.GAME_OVER_MENU)
                pass
            case Scene.CLOSE:
                self._ranking.save()
                self.close()
                pass
            case _:
                pass

    def draw_background(self, with_margin: Optional[bool] = False) -> None:
        """ Desenha o plano de fundo da janela """

        # Limpa a tela
        self.clear()

        # Lógica para desenhar um plano de fundo quadriculado
        cell_size = self._properties.cell_size
        margin = self._properties.margin

        rows = 30 if with_margin else self._properties.height // cell_size + 1
        columns = 30 if with_margin else self._properties.width // cell_size + 1

        horizontal_offset = margin if with_margin else (self._properties.width - columns * cell_size) / 2
        vertical_offset = (cell_size / 2 if margin != 0 else 0) if with_margin else (self._properties.height - rows * cell_size) / 2

        for row in range(rows):
            start = 1 if not row & 1 else 0

            for column in range(start, columns, 2):
                center_x = cell_size / 2 + column  * cell_size + horizontal_offset
                center_y = cell_size / 2 + row * cell_size + vertical_offset

                draw_rectangle_filled(center_x, center_y, cell_size, cell_size, (172, 215, 86))

        if with_margin:
            center_x = columns * cell_size / 2 + horizontal_offset
            center_y = rows * cell_size / 2 + vertical_offset
            width = columns * cell_size
            height = rows * cell_size

            draw_rectangle_outline(center_x, center_y, width, height, (172, 215, 86))

# Exportação padrão
__all__ = ["GameWindow"]

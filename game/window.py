""" Módulo da janela """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import draw_rectangle_filled, draw_rectangle_outline, Window

# Imports de pacotes locais
from .properties import Properties
from .ranking import Ranking
from .resources import Resources
from .scenes import *

class GameWindow(Window):
    """ Define uma janela """

    def __init__(self, root_path: str) -> None:
        """ Inicializa uma janela """

        # Propriedades
        self._properties: Properties = Properties(root_path)

        super().__init__(self._properties.windowed_width, self._properties.windowed_height, "Sanke Game", self._properties.fullscreen, center_window = True)

        # Recursos
        self._resources: Resources = Resources(root_path)

        # Ranking
        self._ranking: Ranking = Ranking(root_path)

        # Última cena e cena atual
        self._last_scene: Scene = None
        self._current_scene: Scene = None

        # Cenas
        self._scenes: dict[str, BaseScene] = None


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

        # Atualiza as propriedades
        self._properties.update(self)

        # Carrega os resursos
        self._resources.setup()

        # Cria as cenas desta janela
        self._create_scenes()

        # Inicia o ciclo das cenas
        self.switch_scene(Scene.MAIN_MENU)

    def _create_scenes(self) -> None:
        """ Cria as cenas desta janela """

        # Inicializa as cenas
        self._scenes = dict()

        for scene in Scene:
            scene_class = get_scene_class(scene)

            if scene_class:
                self._scenes[scene] = scene_class(self)
                self._scenes[scene].setup()

    def switch_scene(self, next_scene: Scene, speed: Optional[Speed] = None, score: Optional[int] = None) -> None:
        """ Faz a mudança de cena """

        self._last_scene, self._current_scene = self._current_scene, next_scene

        match(self._current_scene):
            case Scene.CLOSE:
                self._ranking.save()
                self._properties.save()
                self.close()
                pass

            case Scene.SAVE_SCORE:
                if not self._scenes[Scene.GAME_OVER_MENU].saved:
                    name, points = self._scenes[Scene.GAME_OVER_MENU].score

                    if name != "":
                        self._ranking.add(name, points)
                        self._scenes[Scene.GAME_OVER_MENU].saved = True

                self.switch_scene(Scene.GAME_OVER_MENU)
                pass

            case Scene.SWITCH_FULL_SCREEN:
                self.set_fullscreen(not self._fullscreen)

                if not self.fullscreen:
                    self.center_window()

                self._properties.update(self)
                self._create_scenes()

                self.switch_scene(self._last_scene)
                pass

            case _:
                if self._current_scene in self._scenes:
                    self._scenes[self._current_scene].setup(speed, score)
                    self.show_view(self._scenes[self._current_scene])
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

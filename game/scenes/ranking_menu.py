""" Módulo do menu de ranking """

# Imports de pacotes externos
from arcade import Window
from arcade.gui import UIAnchorWidget, UIBoxLayout

# Imports de pacotes locais
from .base_scene import *
from ..ranking import *
from .gui import *
from .scenes import *
from .speeds import *

class RankingMenu(BaseScene):
    """ Define um menu de ranking """

    def __init__(self, window: Window) -> None:
        """ Inicializa um menu de ranking """

        super().__init__(window)

        # Textos do ranking
        self._ranking_text: list[tuple[TextArea, TextArea]] = None

    def setup(self) -> None:
        """ Configura o menu jogar """

        if self.full_screen == self.window.fullscreen:
            for i in range(len(self.window.ranking)):
                self._ranking_text[i][0].text = self.window.ranking[i].name
                self._ranking_text[i][1].text = str(self.window.ranking[i].score)
                self._ranking_text.fit_content()
            return
        else:
            self.ui_manager.clear()

        # Box layout para alinhar e centralizar tudo
        box = UIBoxLayout(space_between = 10)
        self.ui_manager.add(UIAnchorWidget(child = box))

        # Título
        best_players = TextArea("Melhores Jogadores", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("body") * 1.25)
        box.add(best_players)

        # Ranking
        ranking_box = UIBoxLayout(vertical = False, space_between = 10)
        box.add(ranking_box)

        ## Esquerda, centro e diretia
        left_box = UIBoxLayout(space_between = 10)
        ranking_box.add(left_box)

        center_box = UIBoxLayout(space_between = 10)
        ranking_box.add(center_box)

        rigth_box = UIBoxLayout(space_between = 10)
        ranking_box.add(rigth_box)

        font_name = self.window.resources.fonts.get("body").name
        font_size = self.window.properties.fonts_sizes.get("body") * 0.5

        ## Cabeçalho
        position_text = TextArea("#", font_name, font_size)
        left_box.add(position_text)

        name_text = TextArea("Jogador", font_name, font_size)
        center_box.add(name_text)

        score_text = TextArea("Pontuação", font_name, font_size)
        rigth_box.add(score_text)

        self._ranking_text = []

        i = 0

        ## Itens do ranking
        for score in self.window.ranking:
            i = i + 1

            position_text = TextArea(f"{i}º", font_name, font_size)
            left_box.add(position_text)

            name_text = TextArea(score.name, font_name, font_size)
            center_box.add(name_text)

            score_text = TextArea(str(score.score), font_name, font_size)
            rigth_box.add(score_text)

            self._ranking_text.append((name_text, score_text))

        ## Posições vazias
        while len(self._ranking_text) < 10:
            i = i + 1

            position_text = TextArea(f"{i}º", font_name, font_size)
            left_box.add(position_text)

            name_text = TextArea("-", font_name, font_size)
            center_box.add(name_text)

            score_text = TextArea("0", font_name, font_size)
            rigth_box.add(score_text)

            self._ranking_text.append((name_text, score_text))

        # Botão
        ## Estilo
        button_style = Button.ButtonStyle(self.window.resources.fonts.get("button").name, self.window.properties.fonts_sizes.get("button"))

        # Instância
        back = Button("Voltar", button_style, self.window, self.window.last_scene)
        box.add(UIAnchorWidget(child = back, anchor_x = "left", anchor_y = "bottom"))

        # Define que os objetos de UI foram criados
        self.full_screen = self.window.fullscreen

# Export padrão
__all__ = ["RankingMenu"]

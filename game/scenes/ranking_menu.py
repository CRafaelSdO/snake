""" Módulo do menu de ranking """

# Imports de pacotes externos
from arcade import View, Window
from arcade.gui import UIAnchorWidget, UIBoxLayout, UIManager

# Imports de pacotes locais
from ..ranking import *
from .gui import *
from .scenes import *
from .speeds import *

class RankingMenu(View):
    """ Define um menu de ranking """

    def __init__(self, window: Window) -> None:
        """ Inicializa um menu de ranking """

        super().__init__(window)

        # Gerenciador de UI
        self._ui_manager: UIManager = None

        # Textos do ranking
        self._ranking_text: list[tuple[TextArea, TextArea]] = None

        # Controla se os objetos da UI já foram criados
        self._setup: bool = False

    def setup(self) -> None:
        """ Configura o menu jogar """

        if self._setup:
            return

        # Área de texto
        best_players = TextArea("Melhores Jogadores", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("body") * 1.25)

        # Box layout para conter e alinhar o texto e os botões
        box = UIBoxLayout(space_between = 10)
        box.add(UIAnchorWidget(child = best_players, anchor_y = "top"))

        # Ranking
        ranking_box = UIBoxLayout(vertical = False, space_between = 10)

        # Esquerda, centro e diretia
        left_box = UIBoxLayout(space_between = 10)
        center_box = UIBoxLayout(space_between = 10)
        rigth_box = UIBoxLayout(space_between = 10)

        ranking_box.add(left_box)
        ranking_box.add(center_box)
        ranking_box.add(rigth_box)

        # Cabeçalho
        position_text = TextArea("#", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.5)
        name_text = TextArea("Jogador", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.5)
        score_text = TextArea("Pontuação", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.5)

        left_box.add(position_text)
        center_box.add(name_text)
        rigth_box.add(score_text)

        self._ranking_text = []

        i = 0

        # Itens do ranking
        for score in self.window.ranking:
            i = i + 1

            position_text = TextArea(f"{i}º", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.5)
            name_text = TextArea(score.name, self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.5)
            score_text = TextArea(str(score.score), self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.5)

            self._ranking_text.append((name_text, score_text))

            left_box.add(position_text)
            center_box.add(name_text)
            rigth_box.add(score_text)

        # Posições sem pontuação
        while len(self._ranking_text) < 10:
            i = i + 1

            position_text = TextArea(f"{i}º", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.5)
            name_text = TextArea("-", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.5)
            score_text = TextArea("0", self.window.resources.fonts.get("body").name, self.window.properties.fonts_sizes.get("body") * 0.5)

            self._ranking_text.append((name_text, score_text))

            left_box.add(position_text)
            center_box.add(name_text)
            rigth_box.add(score_text)

        box.add(ranking_box)

        # Estilo dos botões
        button_style = Button.ButtonStyle(self.window.resources.fonts.get("button").name, self.window.properties.fonts_sizes.get("button"))

        # Botões
        back = Button("Voltar", button_style, self.window, self.window.last_scene)

        # Botão de voltar ficará alinhado no canto inferior esquerdo
        box.add(UIAnchorWidget(child = back, anchor_x = "left", anchor_y = "bottom"))

        # Gerenciador de UI com elemento de ancoragem para centralizar tudo
        self._ui_manager = UIManager()
        self._ui_manager.add(UIAnchorWidget(child = box))

        # Define que os objetos de UI foram criados
        self._setup = True

    def on_show_view(self) -> None:
        """ Chamada uma vez ao entrar nessa cena """

        # Ativa o gerenciador de UI
        self._ui_manager.enable()

    def on_hide_view(self) -> None:
        """ Chamada uma vez ao sair dessa cena """

        # Desativa o gerenciador de UI
        self._ui_manager.disable()

    def on_draw(self) -> None:
        """ Chamada sempre ao desenhar """

        # Desenha o plano de fundo
        self.window.draw_background()

        # Desenha a UI
        self._ui_manager.draw()

# Export padrão
__all__ = ["RankingMenu"]

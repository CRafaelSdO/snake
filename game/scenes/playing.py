""" Módulo da tela de jogo """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import draw_rectangle_filled, View, Window

# Imports de pacotes locais
from .entities import *
from .scenes import *

class Playing(View):
    """ Define uma tela de jogo """

    def __init__(self, window: Optional[Window]) -> None:
        """ Inicializa a tela de jogo """

        super().__init__(window)

    def setup(self) -> None:
        """ Configura a tela de jogo"""

        pass

    def on_show_view(self) -> None:
        """ Chamada uma vez ao entrar nessa cena """

        # Muda a cor de fundo
        self.window.background_color = (148, 202, 73)

    def on_hide_view(self) -> None:
        """ Chamada uma vez ao sair dessa cena """

        pass

    def on_draw(self) -> None:
        """ Chamada sempre ao desenhar """

        # Limpa a tela
        self.clear()

        # Lógica para desenhar um plano de fundo quadriculado
        cell_size = self.window.properties.cell_size
        rows = self.window.properties.height // cell_size
        columns = self.window.properties.width // cell_size

        for row in range(rows):
            start = 1 if row % 2 == 0 else 0

            for column in range(start, columns, 2):
                draw_rectangle_filled(cell_size / 2 + column  * cell_size, cell_size / 2 + row * cell_size, cell_size, cell_size, (172, 215, 86))

# Export padrão
__all__ = ["MainMenu"]

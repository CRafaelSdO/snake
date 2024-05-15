""" Módulo do menu principal """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import draw_rectangle_filled, View, Window
from arcade.gui import UIAnchorWidget, UIBoxLayout, UIManager

# Imports de pacotes locais
from .gui import *
from .scenes import *

class MainMenu(View):
    """ Define um menu principal """

    def __init__(self, window: Optional[Window]) -> None:
        """ Inicializa um menu principal """

        super().__init__(window)

        # Gerenciador de UI
        self._ui_manager: UIManager = None

        # Controla se os objetos do menu já foram criados
        self._setup: bool = False
    
    def setup(self) -> None:
        """ Configura o menu principal """

        if self._setup:
            return
        
        # Área de texto
        title_text = TextArea(550, 230, "Snake", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("title"))

        # Estilo dos botões
        button_style = Button.ButtonStyle(self.window.resources.fonts.get("button").name, self.window.properties.fonts_sizes.get("button"))

        # Botões
        play = Button("Jogar", button_style, self.window, GameScene.PLAY_MENU)
        ranking = Button("Classificação", button_style, self.window, GameScene.RANKING_MENU)
        settings = Button("Configurações", button_style, self.window, GameScene.SETTINGS_MENU)
        
        # Box layout para conter os botões
        box = UIBoxLayout(space_between = 10)
        box.add(title_text)
        box.add(play)
        box.add(ranking)
        box.add(settings)

        # Gerenciador de UI com elemento de ancoragem para centralizar tudo
        self._ui_manager = UIManager()
        self._ui_manager.add(UIAnchorWidget(child = box))

        self._setup = True
    
    def on_show_view(self) -> None:
        """ Chamada uma vez ao entrar nessa cena """
        
        # Muda a cor de fundo
        self.window.background_color = (148, 202, 73)

        # Ativa o gerenciador de UI
        self._ui_manager.enable()
    
    def on_hide_view(self) -> None:
        """ Chamada uma vez ao sair dessa cena """

        # Desativa o gerenciador de UI
        self._ui_manager.disable()
    
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

        # Desenha a UI
        self._ui_manager.draw()

# Export padrão
__all__ = ["MainMenu"]

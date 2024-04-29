""" Módulo do menu principal """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import View, Window
from arcade.gui import UIManager, UIAnchorWidget, UIBoxLayout

# Imports de pacotes locais
from .objects import *

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
        
        title_text = TextArea("Snake", self.window.resources.fonts.get("title").name, self.window.properties.fonts_sizes.get("title"))
        
        box = UIBoxLayout()
        box.add(title_text)

        anchor = UIAnchorWidget()
        anchor.add(box)

        self._ui_manager.add(anchor)

        self._setup = True
    
    def on_show_view(self):
        self._ui_manager.enable()
    
    def on_hide_view(self):
        self._ui_manager.disable()
    
    def on_draw(self):
        self._ui_manager.draw()

# Export padrão
__all__ = ["MainMenu"]

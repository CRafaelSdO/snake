""" Módulo do menu principal """

# Imports de pacotes BuiltIn
from typing import Optional

# Imports de pacotes externos
from arcade import View, Window
from arcade.gui import UIManager

# Imports de pacotes locais
from .objects import *

class MainMenu(View):
    """ Define um menu principal """

    def __init__(self, window: Optional[Window]):
        """ Inicializa um menu principal """

        super().__init__(window)

        # Gerenciador de UI
        self._ui_manager: UIManager = None

        # Controla se os objetos do menu já foram criados
        self._setup: bool = False
    
    def setup(self):
        """ Configura o menu principal """

        if self._setup:
            return
        
        title_text = None
        play_button = None

# Export padrão
__all__ = ["MainMenu"]

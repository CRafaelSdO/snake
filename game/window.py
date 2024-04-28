""" Módulo da janela """

# Importyação BuiltIn
from typing import Optional

# Importação externa
from arcade import Window

# Importação local
from .properties import *

class GameWindow(Window):
    """ Define uma janela """
    
    def __init__(self, prop: Optional[Properties] = Properties()) -> None:
        super().__init__(prop.width, prop.height, prop.title, prop.fullscreen, center_window = prop.center_window)

# Exportação padrão
__all__ = ["GameWindow"]

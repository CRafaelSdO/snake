""" Módulo das propriedadedes """

# Imports de pacotes BuiltIn
from typing import NamedTuple, Optional

class GameProperties(NamedTuple):
    """ Define as propriedades """
    
    width: Optional[int] = 800
    height: Optional[int] = 600
    title: Optional[str] = 'Snake Game'
    fullscreen: Optional[bool] = False
    center_window: Optional[bool] = True

# Exportação padrão
__all__ = ["GameProperties"]

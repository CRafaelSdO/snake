""" Módulo das propriedadedes """

# Importyação BuiltIn
from typing import NamedTuple, Optional

class Properties(NamedTuple):
    """ Define as propriedades """
    
    width: Optional[int] = 800
    height: Optional[int] = 600
    title: Optional[str] = 'Snake Game'
    fullscreen: Optional[bool] = False
    center_window: Optional[bool] = True

# Exportação padrão
__all__ = ["Properties"]

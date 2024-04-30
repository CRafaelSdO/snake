""" Módulo das propriedadedes """

# Imports de pacotes BuiltIn
from typing import NamedTuple, Optional

class GameProperties(NamedTuple):
    """ Define as propriedades """
    
    title: Optional[str] = 'Snake Game'
    fullscreen: Optional[bool] = False
    width: Optional[int] = 800
    height: Optional[int] = 600
    center_window: Optional[bool] = True
    cell_size: Optional[int] = 20
    fonts_sizes: Optional[dict[str, float]] = {
        "title": 3 * min(width, height) / 16,
        "body": 3 * min(width, height) / 32,
        "button": 3 * min(width, height) / 80
    }

# Exportação padrão
__all__ = ["GameProperties"]

""" Módulo das propriedadedes """

# Imports de pacotes BuiltIn
from typing import NamedTuple, Optional

# Imports de pacotes externos
from arcade import Window

class Properties(NamedTuple):
    """ Define as propriedades """

    title: Optional[str] = 'Snake Game'
    fullscreen: Optional[bool] = False
    center_window: Optional[bool] = True
    width: Optional[int] = 900
    height: Optional[int] = 960
    cell_size: Optional[int] = 30
    margin: Optional[float] = 0
    fonts_sizes: Optional[dict[str, float]] = {
        "title": 200,
        "body": 50,
        "button": 30
    }

    def update(self, window: Window) -> NamedTuple:
        """ Atualiza width, height e cell_size de forma proporcional aos atuais caso fullscreen de window seja true"""

        # Novas largura e altura
        width, height = window.size
        size = min(width, height)

        # Novos tamanho e margem horizontal para desenho 
        if size == width:
            cell_size = size // 30
            margin = 0
        else:
            cell_size = size // 32
            margin = (width - cell_size * 30) / 2

        # Tamanhos das fontes
        self.fonts_sizes["title"] = size * 2 / 9
        self.fonts_sizes["body"] = size * 1 / 18
        self.fonts_sizes["button"] = size * 1 / 30

        return self._replace(width = width, height = height, cell_size = cell_size, margin = margin)

# Exportação padrão
__all__ = ["Properties"]

""" Módulo das propriedadedes """

# Imports de pacotes BuiltIn
from collections.abc import Iterator
from dataclasses import dataclass
from math import floor, log
from os import getcwd
from os.path import join
from pathlib import Path
from typing import Optional, Union

# Imports de pacotes externos
from arcade import Window

class Properties(Iterator):
    """ Define o conjunto das propriedades """

    DEFAULT_PROPERTIES_PATH = join(getcwd(), "data")
    DEFAULT_PROPERTIES_FILE = "ranking"
    DEFAULT_ENCODING = "ascii"

    @dataclass
    class Propertie:
        """ Define uma propriedade """

        name: str
        value: Union[bool, int, str, dict[str, int]]

        def encode(self, encoding: str) -> bytes:
            """ Transfoma essa propriedade em bytes """

            encoded = self.name.encode(encoding) + ",".encode(encoding)

            if isinstance(self.value, bool):
                encoded += self.value.to_bytes() + ",".encode(encoding)
            elif isinstance(self.value, int):
                byte_count = floor(log(self.value, 256)) + 1
                encoded += self.value.to_bytes(byte_count) + ",".encode(encoding)
            elif isinstance(self.value, str):
                encoded += self.value.encode(encoding) + ",".encode(encoding)
            elif isinstance(self.value, dict[str, int]):
                for key in self.value:
                    prefix = encoded + ".".encode(encoding)
                    value = self.value.get(key)

                    byte_count = floor(log(value, 256)) + 1

                    encoded += prefix + key.encode(encoding) + ",".encode(encoding) + value.to_bytes(byte_count) + ",\n".encode(encoding)

            return encoded

    DEFAULT_PROPERTIES: dict[str, Union[bool, int, str, dict[str, int]]] = {
        "title": "Snake Game",
        "fullscreen": False,
        "width": 900,
        "height": 960,
        "cell_size": 30,
        "margin": 0,
        "fonts_sizes": {
            "title": 200,
            "body": 50,
            "button": 30
        }
    }

    def __init__(self, /, properties: Optional[dict[str, Union[bool, int, str, dict[str, int]]]] = DEFAULT_PROPERTIES, propesties_path: Optional[str] = DEFAULT_PROPERTIES_PATH, propesties_file: Optional[str] = DEFAULT_PROPERTIES_FILE, encoding: Optional[str] = DEFAULT_ENCODING) -> None:
        """ Inicializa o conjunto de propriedades """

        self._properties_path: str = propesties_path
        self._propesties_file: str = propesties_file
        self._encoding: str = encoding
        self._properties: dict[str, Union[bool, int, str, dict[str, int]]] = properties

        pass

    def update(self, window: Window) -> Iterator:
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
            margin = (width - cell_size * 30) * 0.5

        # Tamanhos das fontes
        self.fonts_sizes["title"] = size * 2 / 9
        self.fonts_sizes["body"] = size / 18
        self.fonts_sizes["button"] = size / 30

        return self._replace(width = width, height = height, cell_size = cell_size, margin = margin)

# Exportação padrão
__all__ = ["Properties"]

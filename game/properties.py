""" Módulo das propriedadedes """

# Imports de pacotes BuiltIn
from dataclasses import dataclass
from math import floor, log
from os import getcwd
from os.path import join
from pathlib import Path
from typing import Optional, Union

# Imports de pacotes externos
from arcade import Window

# Imports de pacotes locais
from .properties_data_types import from_bytes, from_str, PropertiesDataTypes

# Pasta, arquivo e codificação padrão
DEFAULT_PROPERTIES_PATH: str = join(getcwd(), "data")
DEFAULT_PROPERTIES_FILE: str = "properties"
DEFAULT_ENCODING: str = "ascii"

# Propriedades padrão
DEFAULT_PROPERTIES: dict[str, Union[bool, int]] = {
    "fullscreen": False,
    "windowed_width": 900,
    "windowed_height": 960,
}

class Properties():
    """ Define o conjunto das propriedades """

    @dataclass
    class Property:
        """ Define uma propriedade """

        value: Union[int, bool]

        def encode(self, name: str, encoding: str) -> bytes:
            """ Transfoma essa propriedade em bytes """

            # Define a quantidade de bytes a serem usados para o valor desta propriedade
            byte_count = 1

            if isinstance(self.value, int) and not isinstance(self.value, bool):
                byte_count += floor(log(self.value, 256))

            return from_str(type(self.value).__name__).to_bytes(name.encode(encoding), self.value.to_bytes(byte_count), ",".encode(encoding))

    def __init__(self, properties_path: Optional[str] = DEFAULT_PROPERTIES_PATH, properties_file: Optional[str] = DEFAULT_PROPERTIES_FILE, encoding: Optional[str] = DEFAULT_ENCODING) -> None:
        """ Inicializa o conjunto de propriedades """

        self._properties_path: str = properties_path
        self._properties_file: str = properties_file
        self._encoding: str = encoding
        self._properties: dict[str, self.Property] = dict()

        try:
            with open(join(properties_path, properties_file), "rb") as file:
                for line in file.readlines():
                    self.add(line)
        except:
            Path(properties_path).mkdir(parents = True, exist_ok = True)

            with open(join(properties_path, properties_file), "wb"):
                pass

            for item in DEFAULT_PROPERTIES:
                self.add(item, DEFAULT_PROPERTIES[item])

    def __getattr__(self, name: str) -> Optional[Union[int, bool]]:
        if name not in self._properties:
            return None

        return self._properties[name].value

    def add(self, *args: Union[bytes, tuple[str, int], tuple[str, bool]]) -> None:
        """ Adiciona uma propriedade ao conjunto de propriedades """

        # Lógica para garantir que os parametros estão corretos
        if len(args) == 1:
            args = args[0]

        if isinstance(args, bytes):
            splitted = args.split(",".encode(self._encoding))

            if len(splitted) < 3:
                raise TypeError(f"Os bytes {args} não estão no formato 'name,value,data_type,' como esperado")

            name = splitted[0].decode(self._encoding)
            data_type = from_bytes(splitted[2])

            if data_type == PropertiesDataTypes.BOOL:
                value = bool.from_bytes(splitted[1])
            else:
                value = int.from_bytes(splitted[1])

        elif len(args) >= 2 and isinstance(args[0], str):
            try:
                data_type = from_str(type(args[1]).__name__)
            except:
                raise TypeError(f"Properties.add() aceita Union[bytes, tuple[str, int], tuple[str, bool]] mas foi fornecido tuple[str, {type(args[1]).__name__}]")

            name = args[0]
            value = args[1]

        else:
            raise TypeError(f"Properties.add() aceita Union[bytes, tuple[str, int], tuple[str, bool]] mas foi fornecido {type(args).__name__}")

        # Adiciona a propriedade
        self._properties[name] = self.Property(value)

    def save(self) -> None:
        """ Salva o arquivo com as propriedades """

        content = b""

        content += self._properties["fullscreen"].encode("fullscreen", self._encoding) + "\n".encode(self._encoding)
        content += self._properties["windowed_width"].encode("windowed_width", self._encoding) + "\n".encode(self._encoding)
        content += self._properties["windowed_height"].encode("windowed_height", self._encoding) + "\n".encode(self._encoding)

        with open(join(self._properties_path, self._properties_file), "wb") as file:
            file.write(content)

    def update(self, window: Window) -> None:
        """ Atualiza width, height e cell_size de forma proporcional aos atuais caso fullscreen de window seja true"""

        # Configura fullscreen, largura e altura
        self._properties["fullscreen"].value = window.fullscreen

        if "width" in self._properties and "height" in self._properties:
            self._properties["width"].value, self._properties["height"].value = window.size
        else:
            width, height = window.size

            self.add("width", width)
            self.add("height", height)

        size = min(self._properties["width"].value, self._properties["height"].value)

        # Novos tamanho e margem horizontal para desenho 
        if size == self._properties["width"].value:
            cell_size = size // 30
            margin = 0
        else:
            cell_size = size // 32
            margin = (self._properties["width"].value - cell_size * 30) * 0.5

        if "cell_size" in self._properties:
            self._properties["cell_size"].value = cell_size
        else:
            self._properties["cell_size"] = self.Property(cell_size)

        if "margin" in self._properties:
            self._properties["margin"].value = margin
        else:
            self._properties["margin"] = self.Property(margin)

        # Tamanhos das fontes
        if "fonts_sizes" in self._properties:
            self._properties["fonts_sizes"].value["title"] = size * 2 / 9
            self._properties["fonts_sizes"].value["body"] = size / 18
            self._properties["fonts_sizes"].value["button"] = size / 30
        else:
            self._properties["fonts_sizes"] = self.Property({
                "title": size * 2 / 9,
                "body": size / 18,
                "button": size / 30
            })

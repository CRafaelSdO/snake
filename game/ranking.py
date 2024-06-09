""" Módulo do ranking """

# Imports de pacotes BuiltIn
from collections.abc import Iterator
from dataclasses import dataclass
from math import floor, log
from os import getcwd
from os.path import join
from pathlib import Path
from typing import Optional, Union

# Pasta, arquivo e codificação padrão
DEFAULT_RANKING_PATH: str = join(getcwd(), "data")
DEFAULT_RANKING_FILE: str = "ranking"
DEFAULT_ENCODING: str = "ascii"

class Ranking(Iterator):
    """ Define o ranking """

    @dataclass
    class Score:
        """ Define um score """

        name: str
        score: int

        def encode(self, encoding: str) -> bytes:
            """ Transforma esse score em bytes """

            byte_count = floor(log(self.score, 256)) + 1
            separator = ",".encode(encoding)

            return self.name.encode(encoding) + separator + self.score.to_bytes(byte_count) + separator

    def __init__(self, ranking_path: Optional[str] = DEFAULT_RANKING_PATH, ranking_file: Optional[str] = DEFAULT_RANKING_FILE, encoding: Optional[str] = DEFAULT_ENCODING) -> None:
        """ Inicializa um ranking """

        self._ranking_path: str = ranking_path
        self._ranking_file: str = ranking_file
        self._encoding: str = encoding
        self._ranking_list: list[self.Score] = []
        self._current_index = -1

        # Carrega o ranking salvo anteriormente, cria o arquivo caso não exista
        try:
            with open(join(ranking_path, ranking_file), "rb") as file:
                for line in file.readlines():
                    self.add(line)
        except:
            Path(ranking_path).mkdir(parents = True, exist_ok = True)

            with open(join(ranking_path, ranking_file), "wb"):
                pass

    def __len__(self) -> int:
        return len(self._ranking_list)

    def __getitem__(self, index) -> Score:
        if index >= len(self._ranking_list):
            raise IndexError

        return self._ranking_list[index]

    def __iter__(self) -> Iterator:
        self._current_index = -1

        return self

    def __next__(self) -> Score:
        self._current_index += 1

        if self._current_index >= len(self._ranking_list):
            raise StopIteration

        return self._ranking_list[self._current_index]

    def add(self, *args: Union[bytes, tuple[str, int]]) -> None:
        """ Adiciona um score ao ranking"""

        # Lógica para garantir que os argumentos estão corretos
        if len(args) == 1:
            args = args[0]

        if isinstance(args, bytes):
            splitted = args.split(",".encode(self._encoding))

            if len(splitted) < 2:
                raise TypeError(f"Os bytes {args} não estão no formato 'name,score,' como esperado")

            name = splitted[0].decode(self._encoding)
            score = int.from_bytes(splitted[1])
        elif len(args) == 2:
            if not isinstance(args[0], str) or not isinstance(args[1], int):
                raise TypeError(f"Ranking.add() aceita Union[bytes, tuple[str, int]] mas foi fornecido {type(args).__name__}")

            name = args[0]
            score = args[1]
        else:
            raise TypeError(f"Ranking.add() aceita Union[bytes, tuple[str, int]] mas foi fornecido {type(args).__name__}")

        # Salva o score novo e organiza a lista
        self._ranking_list.append(self.Score(name, score))
        self._ranking_list.sort(key = lambda item: item.score, reverse = True)

        # Se tiver mais que 10 scores no ranking retira o último
        if len(self._ranking_list) > 10:
            self._ranking_list.pop()

    def save(self) -> None:
        """ Salva o arquivo com o ranking de scores """

        content = b""

        for item in self._ranking_list:
            content += item.encode(self._encoding) + "\n".encode(self._encoding)

        with open(join(self._ranking_path, self._ranking_file), "wb") as file:
            file.write(content)

# Export padrão
__all__ = ["Ranking"]

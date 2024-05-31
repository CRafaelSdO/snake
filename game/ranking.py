""" Módulo do ranking """

# Imports de pacotes BuiltIn
from collections.abc import Iterator
from dataclasses import dataclass
from math import floor, log
from os import getcwd
from os.path import join
from typing import Optional, Union

class Ranking(Iterator):
    """ Define o ranking """

    RANKING_FILE = join(getcwd(), "data/ranking")
    ENCODING = "ascii"

    @dataclass
    class Score:
        """ Define um score """

        name: str
        score: int

        def encode(self, encoding: str) -> bytes:
            """ Transforma esse Score em bytes """

            score_byte_count = floor(log(self.score, 256)) + 1

            return self.name.encode(encoding) + ",".encode(encoding) + self.score.to_bytes(score_byte_count) + ",".encode(encoding)

    def __init__(self, ranking_file: Optional[str] = RANKING_FILE, encoding: Optional[str] = ENCODING) -> None:
        """ Inicializa um ranking """

        self._ranking_file: str = ranking_file
        self._encoding: str = encoding
        self._ranking_list: list[self.Score] = []
        self._current_index = -1

        # Carrega o ranking salvo anteriormente, cria o arquivo caso não exista
        try:
            with open(ranking_file, "rb") as file:
                for line in file.readlines():
                    self.add(line)
        except:
            with open(ranking_file, "wb") as file:
                pass

    def __iter__(self) -> Iterator:
        self._current_index = -1

        return self

    def __next__(self) -> Score:
        self._current_index += 1

        if self._current_index >= len(self._ranking_list):
            raise StopIteration

        return self._ranking_list[self._current_index]

    def add(self, *args: Union[bytes, tuple[str, int], tuple[str, str]]) -> None:
        """ Adiciona um score ao ranking"""

        # Lógica para garantir que os argumentos estão corretos
        if len(args) == 1:
            args = args[0]

        if isinstance(args, bytes):
            splitted = args.split(",".encode(self._encoding))

            if len(splitted) >= 2:
                name = splitted[0].decode(self._encoding)
                score = int.from_bytes(splitted[1])
            else:
                raise TypeError(f"Os bytes {args} não estão no formato 'name,score' como esperado")
        elif len(args) == 2:
            if not isinstance(args[0], str):
                name = str(args[0])
            else:
                name = args[0]

            if not isinstance(args[1], int):
                score = int(args[1])
            else:
                score = args[1]
        else:
            raise TypeError(f"Ranking.add() aceita Union[bytes, tuple[str, int], tuple[str, str]] mas foi fornecido {type(args)}")
        
        new = self.Score(name, score)

        # Salva o score novo e organiza a lista
        self._ranking_list.append(new)
        self._ranking_list.sort(key = lambda item: item.score, reverse = True)

        # Se tiver mais que 10 scores no ranking retira o último
        if len(self._ranking_list) > 10:
            self._ranking_list.pop()

    def save(self) -> None:
        """ Salva o arquivo com o ranking de scores """

        content = b""

        for item in self._ranking_list:
            content += item.encode(self._encoding) + "\n".encode(self._encoding)

        with open(self._ranking_file, "wb") as file:
            file.write(content)

# Export padrão
__all__ = ["Ranking"]

""" Módulo do ranking """

# Imports de pacotes BuiltIn
from dataclasses import dataclass

# Imports de pacotes locais
from .scenes import Speed

class Ranking():
    """ Define o ranking """

    @dataclass
    class Score:
        name: str
        score: int

    def __init__(self) -> None:
        pass

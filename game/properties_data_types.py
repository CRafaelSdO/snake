""" Módulo dos tipos de dados das propriedades """

# Imports de pacotes BuiltIn
from enum import Enum

class PropertiesDataTypes(Enum):
    """ Enumera os tipos de dados das propriedades """

    BOOL = 0
    INT = 1

    def to_bytes(self, name: bytes, value: bytes, separator: bytes) -> bytes:
        """ O tipo de dados em bytes """

        return name + separator + value + separator + self.value.to_bytes() + separator

def from_bytes(bytes: bytes) -> PropertiesDataTypes:
    """ Instancia PropertiesDataTypes a partir de bytes """

    return PropertiesDataTypes(int.from_bytes(bytes))

def from_str(type: str) -> PropertiesDataTypes:
    """ Instancia PropertiesDataTypes a partir de str """

    return PropertiesDataTypes[type.upper()]

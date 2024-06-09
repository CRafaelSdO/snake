""" Módulo dos tipos de dados das propriedades """

# Imports de pacotes BuiltIn
from enum import Enum

class PropertiesDataTypes(Enum):
    """ Enumera os tipos de dados das propriedades """

    BOOL = 0
    INT = 1

    def to_bytes(self) -> bytes:
        """ O tipo de dados em bytes """

        return self.value.to_bytes()

    def from_bytes(bytes: bytes) -> Enum:
        """ Instancia PropertiesDataTypes a partir de bytes """

        try:
            propertie_data_type = PropertiesDataTypes(int.from_bytes(bytes))
        except:
            raise TypeError(f"Não é possível instanciar PropertiesDataTypes com {bytes}")

        return propertie_data_type

    def from_str(string: str) -> Enum:
        """ Instancia PropertiesDataTypes a partir de str """

        match(string):
            case "bool":
                new = PropertiesDataTypes.BOOL
                pass
            case "int":
                new = PropertiesDataTypes.INT
                pass
            case _:
                raise TypeError(f"Não é possível instanciar PropertiesDataTypes com {string}")

        return new

# Export padrão
__all__ = ["PropertiesDataTypes"]

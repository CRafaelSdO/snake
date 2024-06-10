"""
Pacote principal do jogo

Export Padrão:
* GameWindow

Imports disponíveis:
* Properties
* PropertiesDataTypes
* Ranking
* Resources
* GameWindow
"""

# Imports dos módulos
from .properties import Properties
from .properties_data_types import PropertiesDataTypes
from .ranking import Ranking
from .resources import Resources
from .window import GameWindow

# Export padrão
__all__ = ["GameWindow"]

""" Módulo da cena base """

# Imports de pacotes BuiltIn
from abc import abstractmethod
from typing import Optional

# Imports de pacotes externos
from arcade import View, Window
from arcade.gui import UIManager

# Imports de pacotes locais
from .speeds import Speed

class BaseScene(View):
    """ Define uma cena """

    def __init__(self, window: Window, with_margin: Optional[bool] = False) -> None:
        """ Inicializa uma cena """

        super().__init__(window)

        # Controle se deve ser usada margem ao desenhar o plano de fundo
        self._with_margin = with_margin

        # Gerenciador de UI
        self._ui_manager: UIManager = UIManager()

        # Controla se essa cena foi configurada
        self._setted: bool = None

    @property
    def ui_manager(self) -> UIManager:
        """ O gerenciador de UI desta cena"""

        return self._ui_manager

    @property
    def setted(self) -> bool:
        """ Informa se esta cena já foi configurada """

        return self._setted

    @setted.setter
    def setted(self, value: bool) -> None:
        self._setted = value

    @abstractmethod
    def setup(self, speed: Optional[Speed] = None, score: Optional[int] = None) -> None:
        """ Configura a cena """

    def on_show_view(self) -> None:
        """ Chamada uma vez ao entrar nessa cena """

        # Ativa o gerenciador de UI
        self._ui_manager.enable()

    def on_hide_view(self) -> None:
        """ Chamada uma vez ao sair dessa cena """

        # Desativa o gerenciador de UI
        self._ui_manager.disable()

    @abstractmethod
    def on_draw(self) -> None:
        """ Chamada sempre ao desenhar """

        # Desenha o plano de fundo
        self.window.draw_background(self._with_margin)

        # Desenha a UI
        self._ui_manager.draw()

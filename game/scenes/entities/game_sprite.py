""" Módulo das sprites do jogo """

# Imports de pacotes externos
from arcade import Sprite, load_spritesheet

class GameSprite(Sprite):
    """ Define uma sprite do jogo """

    def __init__(self, filename: str, size: float, center_x: float, center_y: float):
        """ Inicializa uma sprite """

        # Escala de desenho
        scale = size / 64

        super().__init__(scale = scale, center_x = center_x, center_y = center_y)

        # Carrega as texturas
        self.textures.extend(load_spritesheet(filename, 64, 64, 4, 15))

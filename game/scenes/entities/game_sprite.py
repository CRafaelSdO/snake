""" Módulo das sprites do jogo """

# Imports de pacotes externos
from arcade import Sprite, Texture, load_spritesheet

# Imports de pacotes locais
from .contents import Content

class GameSprite(Sprite):
    """ Define uma sprite do jogo """

    def __init__(self, filename: str, size: float, center_x: float, center_y: float):
        """ Inicializa uma sprite """

        # Escala de desenho
        scale = size / 64

        super().__init__(scale, 0, 0, 64, 64, center_x, center_y)

        self.textures.extend(load_spritesheet(filename, 64, 64, 6, 11))

    def update_animation(self, delta_time: float = 1 / 60):
        """ Atualiza a textura a ser mostrada """

        self.set_texture(0)
        pass
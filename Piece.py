import pygame

from pygame.locals import*
from constants import *

class Piece(pygame.sprite.Sprite):
    """ A piece is used to play PyChex allowing for movement around the board for each player.
    Returns: piece object
    Function:
    Attributes: active, color, power_level, cart_x, cart_y, x, y"""

    def __init__(self, id, power_level, zone, drop):
        self.id = id
        self.power_level = power_level
        self.zone = zone
        self.drop = drop


    def draw(self, screen):
        chip = pygame.image.load('red_piece.bmp')
        screen.blit(chip, self.drop)

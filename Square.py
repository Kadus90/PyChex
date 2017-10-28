import pygame

from constants import *
from pygame.locals import *

class Square():
    """ A square is an individual square that makes up the checkers board
    Returns: square object
    Functions: draw,
    Attributes: x_coordinate, y_coodinate, width, height, background_color """

    def __init__(self, id, x, y, length, background, active, cart_x, cart_y, image_drop):
        self.id = id
        self.x = x
        self.y = y
        self.length = length
        self.background = background
        self.active = active
        self.cart_x = cart_x
        self.cart_y = cart_y
        self.image_drop = image_drop


    # Draw a Square
    def draw(self, screen):
        pygame.draw.rect(screen, self.background, pygame.Rect(self.x, self.y, self.length, self.length))

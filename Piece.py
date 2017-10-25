import pygame

class Piece(pygame.sprite.Sprite):
    """ A piece is used to play PyChex allowing for movement around the board for each player.
    Returns: piece object
    Function:
    Attributes: active, color, power_level, cart_x, cart_y, x, y"""

    def __init__(self, id, active, color, power_level, cart_x, cart_y, x, y):
        pygame.sprite.Sprite.__init(self)
        self.id = id
        self.active = active
        self.color = color
        self.power_level = power_level
        self.cart_x = cart_x
        self.cart_y = cart_y
        self.x = x
        self.y = y

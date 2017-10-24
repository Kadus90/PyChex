import pygame

class Piece():
    """ A piece is used to play PyChex allowing for movement around the board for each player.
    Returns: piece object
    Function:
    Attributes: location, diameter, color"""

    def __init__(self, location, diameter, color):
        self.location = location
        self.diameter = diameter
        self.color = color

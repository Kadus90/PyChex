import pygame
from Square import Square

class Board ():
    """ Game board for checkers
    Returns: board object
    Functions: update,
    Attributes """

    def __init__(self, status, width, height, background, foreground, margin, square_size):
        self.status = status
        self.width = width
        self.height = height
        self.background = background
        self.foreground = foreground
        self.margin = margin
        self.square_size = square_size
        self.squares = Dict()

        for i in range (0, self.width):
            for j in range (0, self.height):
                if (i % 2 == 0 and j % 2 == 0):
                    square_bg = self.background
                    square_active = FALSE
                if (i % 2 == 0 and j % 2 == 1):
                    square_bg = self.foreground
                    square_active = TRUE
                if (i % 2 == 1 and j % 2 == 0):
                    square_bg = self.foreground
                    square_active = FALSE
                if (i % 2 == 1 and j & 2 == 0):
                    square_bg = self.background
                    square_active = FALSE

                x = i * 75
                y = j * 75

                if(i == 0):
                    x += self.margin
                if(j == 0):
                    y += self.margin

                new_square = Square(x, y, self.l, square_bg, square_active, i, j);
                self.squares[(i,j)] = new_square


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
        self.squares = dict()

        # alternate creation of black and white squares
        for i in range (0, self.width):
            for j in range (0, self.height):
                if (i % 2 == 0 and j % 2 == 0):
                    square_bg = self.background
                    square_active = False
                    # print("i = "+ str(i)+" and j = "+str(j)+" | case 1 fired -- white")
                elif (i % 2 == 0 and j % 2 == 1):
                    square_bg = self.foreground
                    square_active = True
                    # print("i = "+ str(i)+" and j = "+str(j)+" | case 2 fired -- black")
                elif (i % 2 == 1 and j % 2 == 0):
                    square_bg = self.foreground
                    square_active = True
                    # print("i = "+ str(i)+" and j = "+str(j)+" | case 3 fired -- black")
                elif (i % 2 == 1 and j % 2 == 1):
                    square_bg = self.background
                    square_active = False
                    # print("i = "+ str(i)+" and j = "+str(j)+" | case 4 fired -- white")

                # set x and y coordinates for each square
                x = (i * 75) + self.margin
                y = (j * 75) + self.margin

                # instantiate each square, passing in required properties
                new_square = Square("bob", x, y, self.square_size, square_bg, square_active, i, j)
                self.squares[(i,j)] = new_square


    def draw(self, screen):
        for i in range (0, self.width):
            for j in range (0, self.height):
                self.squares[(i,j)].draw(screen)

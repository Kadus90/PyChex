""" This is the controller for the game board of PyChex. """

import pygame
# import debug module - use logging.debug() to print debug info
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

from constants import *
from Square import Square
from Piece import Piece

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
        self.squares = {}
        self.pieces = dict

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

                # Sets the image dropzone
                image_drop = x + 5, y + 5

                # instantiate each square, passing in required properties
                new_square = Square(str('zone' + (str(i)) + (str(j))), x, y, self.square_size, square_bg, square_active, i, j, image_drop)
                self.squares[(i,j)] = new_square

                if self.squares[(i,j)].active == true:
                    new_piece = Piece(str('chip' + str(i) + str(j)), 1, self.squares[(i,j)].name)  # need to think about if drop is a valid prop?  should we have it or better way to determine where it is?


                """
                # instantiate each piece, passing in required properties
                for x in self.squares:
                    if self.squares[(i,j)].active == True and x != 3 or 4:
                        new_piece = Piece('chip'+str(x), 1, self.squares[(i,j)].name, self.squares[(i,j)].image_drop)
                        self.pieces[(x)] = new_piece

                """
                #self.all_squares.update = self.squares[(i,j)]

    # Draw the Board
    def draw(self, screen):
        for i in range (0, self.width):
            for j in range (0, self.height):
                self.squares[(i,j)].draw(screen)


    # Check if a square is clicked
    def click_check(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for i in range (0, self.width):
            for j in range (0, self.height):
                # set x and y coordinates for each square
                x = (i * 75) + self.margin
                y = (j * 75) + self.margin
                if ((x + self.square_size) > mouse_x > x) and ((y + self.square_size) > mouse_y > y) == True:
                    # check what props squares has here
                    print(self.squares[(i,j)].name)
                    return self.squares[(i,j)].name
"""
    # Generates a piece (currently only 1 loading)
    def piece_start(self, screen):
        for i in range (0, self.width):
            for j in range (0, self.height):
                # set x and y coordinates for each square
                x = (i * 75) + self.margin
                y = (j * 75) + self.margin
                if self.squares[(i,j)].active == True and i != 3 or 4:
                    for k in range (0, 24):
                        self.pieces[(k)].generate(screen)

"""

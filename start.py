""" This is the main module for PyChex. """

import sys, pygame, logging

from constants import *
from Board import Board
from Square import Square

# start pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
screen.fill(SCREEN_BACKGROUND)
done = False

clock = pygame.time.Clock()

while not done:

    # check to see if user pressed a key or click a mouse
    pressed = pygame.key.get_pressed()
    clicked = pygame.mouse.get_pressed()

    # check for Control modifier key
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
    for event in pygame.event.get():
        # check if user presses x button in corner to close window
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            # check if ctrl_w is pressed to to close window
            if event.key == pygame.K_w and ctrl_held:
                done = True
            # esc also closes window
            if event.key == pygame.K_ESCAPE:
                done = True
        # Watches for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_board.click_check()

        # instantiate game board and draw to screen
        game_board = Board(True, BOARD_WIDTH, BOARD_HEIGHT, BACKGROUND, FOREGROUND, MARGIN_SIZE, SQUARE_SIZE)
        game_board.draw(screen)

        """
        # Generates pieces
        game_board.piece_start(screen)
        """
        pygame.display.flip()

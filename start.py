import sys, pygame, logging
from Board import Board
from Square import Square

SCREEN_SIZE = 700
SQUARE_SIZE = 75
MARGIN_SIZE = 50
BOARD_WIDTH = 8
BOARD_HEIGHT = 8
BACKGROUND = (255, 255, 255)
FOREGROUND = (0, 0, 0)
BOARD_BORDER = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
done = False


clock = pygame.time.Clock()

while not done:

    pressed = pygame.key.get_pressed()
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and ctrl_held:
                done = True
            if event.key == pygame.K_ESCAPE:
                done = True

        game_board = Board(True, BOARD_WIDTH, BOARD_HEIGHT, BACKGROUND, FOREGROUND, MARGIN_SIZE, SQUARE_SIZE)
        game_board.draw(screen)

    pygame.display.flip()

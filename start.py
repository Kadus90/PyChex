import sys, pygame, logging
from Board import Board
from Square import Square

# constants to define values for board and square
SCREEN_SIZE = 700
SQUARE_SIZE = 75
MARGIN_SIZE = 50
BOARD_WIDTH = 8
BOARD_HEIGHT = 8
BACKGROUND = (255, 255, 255)
FOREGROUND = (0, 0, 0)
SCREEN_BACKGROUND = (66, 66, 99)

# start pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
screen.fill(SCREEN_BACKGROUND)
done = False

clock = pygame.time.Clock()

while not done:

    # check to see if user pressed a key
    pressed = pygame.key.get_pressed()
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

        # instantiate game board and draw to screen
        game_board = Board(True, BOARD_WIDTH, BOARD_HEIGHT, BACKGROUND, FOREGROUND, MARGIN_SIZE, SQUARE_SIZE)
        game_board.draw(screen)


    pygame.display.flip()

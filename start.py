import sys, pygame, logging

class Board ():
    """ Game board for checkers
    Returns: board object
    Functions: update,
    Attributes """

    def __init__(self, status):
        self.status = status

class Square(pygame.sprite.Sprite):
    """ A square is an individual square that makes up the checkers board
    Returns: square object
    Functions: update,
    Attributes: """

    def __init__(self, x_coord, y_coord, id):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.id = id

    def update(self):
        # update functions (put crap below to validate syntax)
        x_coord += 0

class Player():
    """ Player - user and computer
    Returns: player object
    Function: uodate, turns, color
    Attributes: """

pygame.init()
screen = pygame.display.set_mode((700, 700))
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

        startX = 50
        startY = 50
        pygame.draw.rect(screen, (255, 000, 000), pygame.Rect(startX, startY, 600, 800))

        sqW = 75
        sqH = 75

        # generate IDs:
        # blue_blobs = dict(enumerate([Classname(VALUES) for i in range(SOME_RANGE)]))

        for i in range(0, 8):
            shift = 75 if (i % 2) == 0 else 0
            for j in range (0, 4):
                pygame.draw.rect(screen, (000, 000, 000), pygame.Rect(startX + shift + (150 * j), startY + (75 * i), sqW, sqH))

        # for use later - function below spits out coords of mouse anytime it is moved by the user
        logging.warning(pygame.mouse.get_pos())

    pygame.display.flip()
    clock.tick(60)

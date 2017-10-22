import sys, pygame

pygame.init()
screen = pygame.display.set_mode((700, 700))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        startX = 50
        startY = 50
        pygame.draw.rect(screen, (255, 000, 000), pygame.Rect(startX, startY, 600, 600))

        sqW = 75
        sqH = 75
        for i in range(0, 8):
            shift = 75 if (i % 2) == 0 else 0
            for j in range (0, 4):
                pygame.draw.rect(screen, (000, 000, 000), pygame.Rect(startX + shift + (150 * j), startY + (75 * i), sqW, sqH))

    pygame.display.flip()

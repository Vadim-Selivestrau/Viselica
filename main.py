import pygame

sc = pygame.display.set_mode((800, 420))
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
GRAY = (46, 46, 46)

pygame.display.set_caption("Viselica")  # заголовок окна
runGame = True
sc.fill(GRAY)
pygame.draw.aaline(sc, WHITE,
                   [220, 70],
                   [220, 420])
pygame.draw.aaline(sc, WHITE,
                   [0, 70],
                   [800, 70])

while runGame:
    for i in pygame.event.get():
        if i.type == pygame.QUIT: runGame = False
        # sys.exit()
    pygame.display.update()

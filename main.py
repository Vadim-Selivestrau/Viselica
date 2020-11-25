import pygame

pygame.init()   #initialisation in Windows and Linux, Mac
sc = pygame.display.set_mode((800, 420))
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
GRAY = (80, 80, 80)
word = ""
death1 = pygame.image.load('img\Viselica\death1.png')
death2 = pygame.image.load('img\Viselica\death2.png')
death3 = pygame.image.load('img\Viselica\death3.png')
death4 = pygame.image.load('img\Viselica\death4.png')
death5 = pygame.image.load('img\Viselica\death5.png')
death6 = pygame.image.load('img\Viselica\death6.png')
death1.set_colorkey((255, 255, 255))
death2.set_colorkey((255, 255, 255))
death3.set_colorkey((255, 255, 255))
death4.set_colorkey((255, 255, 255))
death5.set_colorkey((255, 255, 255))
death6.set_colorkey((255, 255, 255))
death = 0
lokate_image = (0, 70, 50, 50)
pygame.display.set_caption("viselica")  # заголовок окна
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

        if i.type == pygame.QUIT:
            runGame = False
        # sys.exit()
    pygame.display.flip()
    sc.blit(death1, lokate_image)
    pygame.display.update()

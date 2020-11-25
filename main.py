import pygame

pygame.init()  # initialisation in Windows and Linux, Mac

sc_width = 800
sc_hight = 420
sc = pygame.display.set_mode((sc_width, sc_hight))
WHITE = (255, 255, 255)
GRAY = (80, 80, 80)
word = "notebook"  # test word
mistake_counter = 0
icon = pygame.image.load('img\icon\pogonya.jpg')
pygame.display.set_icon(icon)  # icon application
death1 = pygame.image.load('img\Viselica\death1.png')
death2 = pygame.image.load('img\Viselica\death2.png')
death3 = pygame.image.load('img\Viselica\death3.png')
death4 = pygame.image.load('img\Viselica\death4.png')
death5 = pygame.image.load('img\Viselica\death5.png')
death6 = pygame.image.load('img\Viselica\death6.png')
death1 = pygame.transform.scale(death1, (400, 350))
death2 = pygame.transform.scale(death2, (400, 350))
death3 = pygame.transform.scale(death3, (400, 350))
death4 = pygame.transform.scale(death4, (400, 350))
death5 = pygame.transform.scale(death5, (400, 350))
death6 = pygame.transform.scale(death6, (400, 350))
death1.set_colorkey(WHITE)  # transparent background
death2.set_colorkey(WHITE)
death3.set_colorkey(WHITE)
death4.set_colorkey(WHITE)
death5.set_colorkey(WHITE)
death6.set_colorkey(WHITE)
lokate_image = (-22, 25, 50, 50)
pygame.display.set_caption("viselica")  # заголовок окна

sc.fill(GRAY)
pygame.draw.aaline(sc, WHITE,
                   [322, 70],
                   [322, 420])
pygame.draw.aaline(sc, WHITE,
                   [0, 70],
                   [800, 70])


def runGame():
    Game = True
    while Game:
        for i in pygame.event.get():
            if (i.type == pygame.QUIT or mistake_counter == 6):
                pygame.quit()
                quit()

        pygame.display.flip()
        output_image(mistake_counter)
        pygame.display.update()


def output_image(counter):
    if (counter == 1):
        sc.blit(death1, lokate_image)
    elif (counter == 2):
        sc.blit(death2, lokate_image)
    elif (counter == 3):
        sc.blit(death3, lokate_image)
    elif (counter == 4):
        sc.blit(death4, lokate_image)
    elif (counter == 5):
        sc.blit(death5, lokate_image)
    elif (counter == 6):
        sc.blit(death6, lokate_image)


runGame()

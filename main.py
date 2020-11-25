import pygame

pygame.init()   #initialisation in Windows and Linux, Mac
sc_width = 800
sc_hight = 420
sc = pygame.display.set_mode((sc_width, sc_hight),pygame.RESIZABLE)
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
GRAY = (80, 80, 80)
word = "notebook"
mistake = 0
icon = pygame.image.load('img\icon\pogonya.jpg')
pygame.display.set_icon(icon)   #icon application
death1 = pygame.image.load('img\Viselica\death1.png')
death2 = pygame.image.load('img\Viselica\death2.png')
death3 = pygame.image.load('img\Viselica\death3.png')
death4 = pygame.image.load('img\Viselica\death4.png')
death5 = pygame.image.load('img\Viselica\death5.png')
death6 = pygame.image.load('img\Viselica\death6.png')
death1 = pygame.transform.scale(death6, (sc_width // 2, sc_hight * 6 // 7))
death1.set_colorkey((255, 255, 255))    #transparent background
death2.set_colorkey((255, 255, 255))
death3.set_colorkey((255, 255, 255))
death4.set_colorkey((255, 255, 255))
death5.set_colorkey((255, 255, 255))
death6.set_colorkey((255, 255, 255))
death = 0
lokate_image = (-22, 25, 50, 50)
pygame.display.set_caption("viselica")  # заголовок окна
runGame = True
sc.fill(GRAY)
pygame.draw.aaline(sc, WHITE,
                   [322, 70],
                   [322, 420])
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

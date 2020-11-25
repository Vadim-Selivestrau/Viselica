import pygame
import random

from words import words

pygame.init()  # initialisation in Windows and Linux, Mac
# from game_object import GameObject
# from text_object import TextObject

sc_width = 800
sc_hight = 420
sc = pygame.display.set_mode((sc_width, sc_hight))
WHITE = (255, 255, 255)
GRAY = (80, 80, 80)
CYAN = (13, 246, 205)
RED = (255, 19, 9)


# work with word
def choice_word(words):
    word = random.choice(words)
    return word


word = choice_word(words)
length_word = len(word)

mistake_counter = 6

# work with image
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
location_image = (-22, 25, 50, 50)
pygame.display.set_caption("Viselica")  # заголовок окна


# work with button
class Button:
    def __init__(self, x, y, width, height):  # initialisation atributes """,txt"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = CYAN
        self.active_color = WHITE
        # self.txt = txt

    def draw(self, x, y, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(sc, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    self.inactive_color = RED
                    self.active_color = RED
                    if action is not None:
                        action()
        else:
            pygame.draw.rect(sc, self.inactive_color, (x, y, self.width, self.height))

        # print_text(txt, x+10, y+10)


sc.fill(GRAY)
pygame.draw.aaline(sc, WHITE,
                   [322, 70],
                   [322, 420])
pygame.draw.aaline(sc, WHITE,
                   [0, 70],
                   [800, 70])

x: int = 20
y: int = 0
for i in range(0, length_word):  # drow line from secret word
    pygame.draw.aaline(sc, WHITE,
                       [y, 40],
                       [x, 40])
    y += 80
    x += 80


def runGame():
    Game: bool = True
    button_a = Button(400, 50, 25, 25)
    while Game:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:  # or mistake_counter == 6  # END GAME
                pygame.quit()
                quit()
        button_a.draw(350, 100, None)
        pygame.display.flip()
        output_image(mistake_counter)
        pygame.display.update()


def output_image(counter):
    if (counter == 1):
        sc.blit(death1, location_image)
    elif (counter == 2):
        sc.blit(death2, location_image)
    elif (counter == 3):
        sc.blit(death3, location_image)
    elif (counter == 4):
        sc.blit(death4, location_image)
    elif (counter == 5):
        sc.blit(death5, location_image)
    elif (counter == 6):
        sc.blit(death6, location_image)


runGame()

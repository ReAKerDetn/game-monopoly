from socket import socket
import pygame
# from win32gui import
from win32api import GetSystemMetrics
# import win32gui, win32con
from PIL import Image, ImageDraw
# from threading import Thread
from PIL import Image, ImageSequence

import win32gui, win32con

# hwnd = win32gui.GetForegroundWindow()
# screen = win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
pygame.init()
WIDTH, HEIGHT = GetSystemMetrics(0), GetSystemMetrics(1)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# image_cross = pygame.image.load("крест.jpg")
print(WIDTH)
print(HEIGHT)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
clock = pygame.time.Clock()
FPS = 60
logo_monopoly = pygame.image.load("logo.png")
hat = pygame.image.load("hat.png")
exit_menu = pygame.image.load("exit_menu.jpg")


# while pygame.event.wait().type != pygame.QUIT:
#     screen.fill((black))
#     screen.blit(image, (WIDTH - 50, 0))
#     pygame.display.flip()


def menu():
    # start_menu = pygame.image.load("фон3.jpg")      # изображение фона стартового меню

    button_run = Button(200, 70)
    button_quit = Button(100, 40)
    button_save = Button(100, 50)  # может быть в игре будет сейв так как игра довольно длинная, просто идеи

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # pygame.quit()
                # quit()

        screen.fill((WHITE))

        # screen.blit(image_cross, (WIDTH - 50, 0))
        # pygame.display.flip()

        # screen.blit(start_menu, (0, 0))        # если будет какая то картинка в начале игры разрешение 1920x1080

        button_quit.draw(1828, 7, "Выход", quit, 40)
        button_run.draw(850, 440, "Играть", game, 40)

        screen.blit(exit_menu, (1826, 0))
        screen.blit(logo_monopoly, (700, 250))
        screen.blit(hat, (300, 500))

        pygame.display.update()
        clock.tick(FPS)


def game():  # просто как функция начала игры или лучше класс?
    pass


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.inactive_col = inactive_color      # в случаи не статичного подсвечивания
        # self.active_col = active_color

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, RED, (x, y, self.width, self.height))
            if click[0] == 1:
                action()

        else:
            pygame.draw.rect(screen, GREEN, (x, y, self.width, self.height))
        print_text(message=message, x=x + 44, y=y + 12, font_size=font_size)

    def effects(self):  # эффекты кнопки
        pass


def print_text(message, x, y, font_color=(0, 0, 0), font_type="arial", font_size=36): # пока такой шрифт, потом поменяем
    font_type = pygame.font.SysFont(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))


def loadGIF(filename):
    pilImage = Image.open(filename)
    clock.tick(4)
    pass


if __name__ == '__main__':
    menu()
    pygame.quit()
    quit()

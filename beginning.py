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
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


class Main:
    def __init__(self):
        logo_monopoly = pygame.image.load("data/logo.png")
        run_logo = pygame.image.load("data/run.png")
        exit_menu = pygame.image.load("data/exit.png")
        mr_monopoly = pygame.image.load("data/mr-monopoly2.png")

        button_run = Button(200, 70)
        button_quit = Button(55, 37)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    # pygame.quit()
                    # quit()

            screen.fill(pygame.Color(64, 64, 64), pygame.Rect(0, 0, WIDTH, HEIGHT / 100 * 15))

            button_quit.draw(WIDTH - 55, 0, "", quit, 40)
            button_run.draw((WIDTH - 200) // 2, (HEIGHT - 70) // 2, "Играть", Game, 40)     # изменил

            screen.blit(exit_menu, (WIDTH - 55, 0))     
            screen.blit(logo_monopoly, ((WIDTH - 485) // 2, HEIGHT / 100 * 15 / 6))
            screen.blit(mr_monopoly, (200, 350))
            screen.blit(run_logo, ((WIDTH - 512) // 2, (HEIGHT - 512) // 2))

            words = 'Хотите испытать удачу и попробовать себя в роли предпринимателя?'
            words2 = 'Тогда добро пожаловать в Монополию!'
            text = font.render(words, True, pygame.Color("black"))
            place = text.get_rect(center=(WIDTH - WIDTH // 5, HEIGHT * 0.25))
            text2 = font.render(words2, True, pygame.Color("black"))
            place2 = text.get_rect(center=(WIDTH - WIDTH // 5, HEIGHT * 0.25 + 50))
            screen.blit(text, place)
            screen.blit(text2, place2)

            pygame.display.update()
            clock.tick(FPS)


class Game:
    screen.fill(pygame.Color(214, 210, 210))
    pygame.display.update()
    pass


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__(all_sprites)
        self.width = width
        self.height = height

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
    pygame.display.set_caption("Монополия")
    font = pygame.font.SysFont('poppins', 40)
    Main()
    pygame.quit()
    quit()

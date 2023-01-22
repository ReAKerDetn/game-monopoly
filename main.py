from socket import socket
import pygame, asyncio, socket
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
backgr1 = pygame.Color(214, 210, 210)
backgr2 = pygame.Color(64, 64, 64)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
logo_monopoly = pygame.image.load("data/logo.png")
run_logo = pygame.image.load("data/run.png")
exit_menu = pygame.image.load("data/exit.png")
mr_monopoly = pygame.image.load("data/mr-monopoly.png")
board = pygame.image.load("data/board.png")
back = pygame.image.load("data/back.png")
login_pic = pygame.image.load("data/login.png")
login_pic2 = pygame.image.load("data/login2.png")
NowPage, login = '', ''



class Main:
    def __init__(self):
        global NowPage, client
        NowPage = 'Main'
        button_run = Button(200, 70)
        button_quit = Button(55, 37)
        button_logo = Button(100, 100)
        
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
            screen.fill(backgr1)
            screen.fill(backgr2, pygame.Rect(0, 0, WIDTH, HEIGHT / 100 * 15))

            button_quit.draw(WIDTH - 55, 0, "", quit, 40)
            button_run.draw((WIDTH - 200) // 2, (HEIGHT - 70) // 2, "Играть", Game, 40, backgr1)
            button_logo.draw(WIDTH * 0.05, HEIGHT / 100 * 15 / 3.5, "", Login, 40, backgr2)

            screen.blit(exit_menu, (WIDTH - 55, 0))     
            screen.blit(logo_monopoly, ((WIDTH - 485) // 2, HEIGHT / 100 * 15 / 6))
            screen.blit(mr_monopoly, (200, 350))
            screen.blit(run_logo, ((WIDTH - 512) // 2, (HEIGHT - 512) // 2))
            screen.blit(login_pic, (WIDTH * 0.05, HEIGHT / 100 * 15 / 3.5))

            words = 'Хотите испытать удачу и попробовать себя в роли предпринимателя?'
            words2 = 'Тогда добро пожаловать в Монополию!'
            text = font.render(words, True, pygame.Color("black"))
            place = text.get_rect(center=(WIDTH - WIDTH // 5, HEIGHT * 0.25))
            text2 = font.render(words2, True, pygame.Color("black"))
            place2 = text.get_rect(center=(WIDTH - WIDTH // 5, HEIGHT * 0.25 + 50))
            screen.blit(text, place)
            screen.blit(text2, place2)
            # print_text('Хотите испытать удачу и попробовать себя в роли предпринимателя?', (WIDTH - 950) // 2, HEIGHT // 2 - 300, BLACK)
            # print_text('Тогда добро пожаловать в Монополию!', (WIDTH - 530) // 2, HEIGHT // 2 - 225, BLACK)

            pygame.display.update()
            clock.tick(FPS)


class Login:
    def __init__(self):
        global NowPage, login
        NowPage = 'Login'
        self.password = ''
        self.button_quit = Button(55, 37)
        self.button_back = Button(53, 35)
        self.font = pygame.font.Font(None, 32)
        self.font1 = pygame.font.Font(None, 48)
        self.login_rect = pygame.Rect(WIDTH * 0.35 * 1.35, HEIGHT * 0.285, WIDTH * 0.2, HEIGHT * 0.03) #pygame.Rect(650, 200, 140, 32)
        self.password_rect = pygame.Rect(WIDTH * 0.35 * 1.35, HEIGHT * 0.385, WIDTH * 0.2, HEIGHT * 0.03)# pygame.Rect(650, 300, 140, 32)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('grey')
        self.color1 =self.color_passive
        self.color = self.color_passive
        self.active = False
        self.active1 = False
        self.process()
    
    def process(self):
        global NowPage, login
        logging = True
        while NowPage == "Login" and logging:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logging = False
                    pygame.quit()
                    quit()
                screen.fill(backgr1)
                screen.fill(backgr2, pygame.Rect(0, 0, WIDTH, HEIGHT / 100 * 15))

                login_button = Button(118, 59)
                login_button.draw(WIDTH * 0.5, HEIGHT * 0.5, "LoginAc", Main, 40, backgr1)
                screen.blit(login_pic2, (WIDTH * 0.5, HEIGHT * 0.5))

                self.button_quit.draw(WIDTH - 55, 0, "", quit, 40)
                self.button_back.draw(0, 0, "", Main, 10)
                screen.blit(exit_menu, (WIDTH - 55, 0))
                screen.blit(logo_monopoly, ((WIDTH - 485) // 2, HEIGHT / 100 * 15 / 6))
                screen.blit(back, (-1, -1))
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        all_sprites.update(event) 
                    if self.login_rect.collidepoint(event.pos):
                        self.active = True
                    else:
                        self.active = False
                    if self.password_rect.collidepoint(event.pos):
                        self.active1 = True
                    else:
                        self.active1 = False
                if event.type == pygame.KEYDOWN:
                    if self.active is True and self.active1 == False:
                        if event.key == pygame.K_BACKSPACE: 
                            login = login[:-1]
                        elif event.key == pygame.K_KP_ENTER:
                            self.active = False
                        else:
                            login += event.unicode 
                    if self.active1 is True and self.active == False:
                        if event.key == pygame.K_BACKSPACE: 
                            self.password = self.password[:-1]
                        else:
                            self.password += event.unicode 

            if self.active and self.active1 == False:
                self.color = self.color_active
            else:
                self.color = self.color_passive

            if self.active1 and self.active == False:
                self.color1 = self.color_active
            else:
                self.color1 = self.color_passive 

            pygame.draw.rect(screen, self.color, self.login_rect, 2)
            pygame.draw.rect(screen, self.color1, self.password_rect, 2)

            screen.blit(self.font.render(login, True, pygame.Color("black")), (self.login_rect.x + 5, self.login_rect.y + 5))
            screen.blit(self.font.render(self.password, True, pygame.Color("black")), (self.password_rect.x + 5, self.password_rect.y + 5))
            screen.blit(self.font.render("Логин:", False, pygame.Color("black")), (WIDTH * 0.35 * 1.15, HEIGHT * 0.287))
            screen.blit(self.font.render("Пароль:", False, pygame.Color("black")), (WIDTH * 0.35 * 1.15, HEIGHT * 0.387))
            screen.blit(self.font1.render("Авторизация", False, pygame.Color("black")), (WIDTH * 0.35 * 1.2, HEIGHT * 0.2))
            self.login_rect.w = max(WIDTH * 0.09, self.font.render(login, True, pygame.Color("black")).get_width() + 10)
            self.password_rect.w = max(WIDTH * 0.09, self.font.render(self.password, True, pygame.Color("black")).get_width() + 10)
            # all_sprites.draw(screen)
            all_sprites.update()
            pygame.display.flip()


class Game:
    def __init__(self):
        button_quit = Button(55, 37)
        button_back = Button(53, 35)
        gaming = True

        while gaming:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gaming = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Main()

            # screen.fill(pygame.Color(181, 184, 177))
            # screen.fill(pygame.Color(135, 206, 250))
            screen.fill(pygame.Color(64, 64, 64))

            button_quit.draw(WIDTH - 55, 0, "", quit, 40)
            button_back.draw(0, 0, "", Main, 10)

            screen.blit(exit_menu, (WIDTH - 55, 0))
            screen.blit(board, (((WIDTH - 948) // 2) + 300, (HEIGHT - 941) // 2))
            screen.blit(back, (-1, -1))

            pygame.display.update()


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__(all_sprites)
        self.width = width
        self.height = height

    def draw(self, x, y, message, action=None, font_size=30, color=None):
        log = False
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if message == 'LoginAc':
            log = True
            message = ''
        if color == None:
            color = WHITE
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, color, (x, y, self.width, self.height))
            if click[0] == 1:
                if log:
                    client.send_data(f"LOGIN {login}")
                action()
        else:
            pygame.draw.rect(screen, color, (x, y, self.width, self.height))
        print_text(message=message, x=x + 44, y=y + 12, font_size=font_size)

    def effects(self):  # эффекты кнопки
        pass


class Socket:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_loop = asyncio.new_event_loop()

    async def send_data(self, data=None):
        raise NotImplementedError()

    async def listen_socket(self, listened_socket=None):
        raise NotImplementedError()

    async def main(self):
        raise NotImplementedError()

    def start(self):
        self.main_loop.run_until_complete(self.main())

    def set_up(self):
        raise NotImplementedError()


class Client(Socket):
    def __init__(self):
        super(Client, self).__init__()

    def set_up(self):
        try:
            self.socket.connect(
                ("127.0.0.1", 1234)
            )
        except ConnectionRefusedError:
            return "Sorry, server is offline"

        self.socket.setblocking(False)
        return

    async def listen_socket(self, listened_socket=None):
        global messages
        while True:
            data = await self.main_loop.sock_recv(self.socket, 2048)
            messages = data.decode('utf-8')

    def send_data(self, data=None):
        socket.send(self.socket, data.encode("utf-8"))

    async def main(self):
        await self.main_loop.create_task(self.listen_socket())


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
    client = Client()
    Main()

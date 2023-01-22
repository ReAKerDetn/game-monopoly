from socket import socket
import pygame, asyncio, sys, os
import time
from Socket import Socket
from threading import Thread
# from win32gui import
from win32api import GetSystemMetrics
# import win32gui, win32con
from PIL import Image, ImageDraw
# from threading import Thread
from PIL import Image, ImageSequence

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
findgame = pygame.image.load("data/findgame.png")
logout = pygame.image.load("data/logout.png")
create = pygame.image.load("data/create.png")

messages, online, NowPage, login, players, chance = "", False, "", "", "", ""
all_objs = []
PiecPlayers = []


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def resize_img(pict, w, h):
    img = Image.open(pict)
    new_img = img.resize((w, h))
    new_img.save(pict[:-4] + "2" + ".png", "PNG", optimize=True)


def translate(word):
    if (len(word) <= 0):
        return ""
    new_word = {}
    for i in word.split("!!!"):
        t = i.split('#')
        if (t == ['']):
            continue
        new_word[t[0]] = t[1].split('$')
    return new_word

def translate2(word):
    if (len(word) <= 0):
        return ""
    new_word = {}
    for i in word.split("!!!"):
        t = i.split('#')
        if (t == ['']):
            continue
        new_word[t[0]] = ''.join(t[1].split('$'))
    return new_word


def Game(y, game, p):
    global players
    screen.fill(pygame.Color(219, 219, 219), pygame.Rect(WIDTH * 0.16, y, WIDTH * 0.68, 150))
    font1 = pygame.font.Font(None, 24)
    text = font1.render(f'Количество игроков: {len(p)}\\5', True, pygame.Color("black"))
    place = text.get_rect(center=(WIDTH * 0.23, y + 18))
    screen.blit(text, place)
    # circle_image("data/gray_user.png")
    for i in range(5):
        if (i < len(p)):
            try:
                all_objs.append(Button(load_image("gray_usernew.png"), (WIDTH * 0.25 + (i * 180), y + 80)))
                text2 = font1.render(f'{players[p[i]]}', True, pygame.Color("black"))
                place2 = text2.get_rect(center=(WIDTH * 0.25 + (i * 180), y + 140))
                screen.blit(text2, place2)
            except:
                pass
        else:
            all_objs.append(Button(load_image("join.png", colorkey=-1), (WIDTH * 0.25 + (i * 180), y + 80), game))


class Start:
    def __init__(self):
        global online, NowPage
        if client.set_up() is None:
            online = True
        Main()


class Main:
    def __init__(self):
        global NowPage, client
        NowPage = 'Main'
        button_run = Button(200, 70)
        button_quit = Button(55, 37)
        
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
            screen.fill(backgr1)
            screen.fill(backgr2, pygame.Rect(0, 0, WIDTH, HEIGHT / 100 * 15))

            if login == '':
                button_login = Button(100, 100)
                button_login.draw(WIDTH * 0.05, HEIGHT / 100 * 15 / 3.5, "", Login, 40, backgr2)
                screen.blit(login_pic, (WIDTH * 0.05, HEIGHT / 100 * 15 / 3.5))
            else:
                button_logout = Button(118, 59)
                button_logout.draw(WIDTH * 0.05, HEIGHT / 100 * 15 / 3.5, "", Login, 40, backgr2)
                screen.blit(logout, (WIDTH * 0.05, HEIGHT / 100 * 15 / 3.5))

            button_quit.draw(WIDTH - 55, 0, "", quit, 40)
            button_run.draw((WIDTH - 200) // 2, (HEIGHT - 70) // 2, "Играть", Game, 40, backgr1)

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


class BlockPlayer(pygame.sprite.Sprite):
    def __init__(self, pos, player, command=None):
        global players
        super().__init__(all_sprites)
        self.image = load_image('BlockPlayer.png')
        self.rect = self.image.get_rect(center=pos)
        self.command = command


class TempPiece(pygame.sprite.Sprite):
    def __init__(self, image, pos, command=None):
        super().__init__(all_sprites)
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.command = command
        self.pos = 0


class LOSEORWIN(pygame.sprite.Sprite):
    def __init__(self, image, pos, command=None):
        super().__init__(all_sprites)
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.command = command
        self.pos = 0


class Piece(pygame.sprite.Sprite):
    def __init__(self, image, pos, command=None):
        super().__init__(all_sprites)
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.command = command
        self.pos = 0
    
    def turn(self, turn):
        for i in range(turn):
            self.pos += 1
            if (self.pos > 40):
                self.pos -= 40
            if (self.pos <= 10):
                self.rect = self.rect.move(WIDTH * 0.03755, 0)
            elif (self.pos <= 20):
                self.rect = self.rect.move(0, HEIGHT * 0.0665)
            elif (self.pos <= 30):
                self.rect = self.rect.move(-(WIDTH * 0.03755), 0)
            elif (self.pos <= 40):
                self.rect = self.rect.move(0, -(HEIGHT * 0.0665))


def timer_chance():
    global chance
    time.sleep(3)
    chance = ''


class Board:
    def __init__(self, g, main=False):
        global NowPage, messages, PiecPlayers, chance
        NowPage = "Game"
        resize_img("data/board.png", int(HEIGHT * 0.9), int(HEIGHT * 0.9))
        self.board = load_image('board2.png', colorkey=-1)
        self.pos_board = self.board.get_rect(center=(WIDTH * 0.60, HEIGHT // 2))
        for i in all_objs:
            i.kill()
        for i in PiecPlayers:
            i.kill()
        screen.fill(pygame.Color(33, 40, 43))
        screen.blit(self.board, self.pos_board)
        self.turn = messages
        client.send_data("check listgame")
        font1 = pygame.font.Font(None, 32)
        font1 = pygame.font.Font(None, 24)
        all_objs.append(Button(load_image("logout2.png", colorkey=-1), (80, HEIGHT * 0.05), f"ExitGame#{g}"))
        time.sleep(0.5)
        self.all_games = translate(messages.split("&")[0])
        if '&' in messages:
            self.players = (translate2(messages.split("&")[1]))
        pieces = ["red_piece.png", "blue_piece.png", "green_piece.png", "purple_piece.png", "orange_piece.png"]
        locks = ["red_lock.png", "blue_lock.png", "green_lock.png", "purple_lock.png", "orange_lock.png"]
        self.number = 0
        PiecPlayers = []
        for i in range(len(self.players)):
            try:
                all_objs.append(BlockPlayer((WIDTH * 0.20, HEIGHT * 0.15 + (i * 180)), self.all_games[g][i]))
                PiecPlayers.append(Piece(load_image(pieces[i], colorkey=-1), (WIDTH * 0.415, HEIGHT * 0.17 - (i * 5)), self.all_games[g][i]))
                if (players[self.all_games[g][i]] == login):
                    self.number = i
            except:
                pass
        if main:
            all_objs.append(Button(load_image("start.png", colorkey=-1), (WIDTH // 2, HEIGHT // 2), f"START#{g}"))
        start = True
        pos = PiecPlayers[self.number].rect
        money = [15000] * len(PiecPlayers)
        while NowPage == "Game":
            clock.tick(2)
            if ("Player" in messages and "turn" in messages):
                p, t = messages.split(" ")[1], messages.split(" ")[3]
                PiecPlayers[int(p)].turn(int(t))
                if ("Player" in messages and "turn" in messages):
                    messages = ""
                client.send_data(f"check money {p}")
            if (PiecPlayers[self.number].rect != pos):
                pos = PiecPlayers[self.number].rect
                temp.kill()
                screen.fill(pygame.Color(33, 40, 43))
            if (messages == "BUY"):
                temp = BUY(load_image("buy.png"), (WIDTH // 2, HEIGHT // 2), self.number)
                all_objs.append(temp)
            if ("CHANCE" in messages):
                chance = ' '.join(messages.split(" ")[1:])
                temp2 = LOSEORWIN(load_image("Chance.jpg"), (WIDTH // 2, HEIGHT // 2))
                all_objs.append(temp2)
                Thread(target=timer_chance, daemon=True).start()
            if ("Player" in messages and "buy" in messages):
                p = int(messages.split(" ")[1])
                if p == self.number:
                    temp.kill()
                    screen.fill(pygame.Color(33, 40, 43))
                client.send_data(f"check money {p}")
                messages = ""
                all_objs.append(TempPiece(load_image(locks[p], colorkey=-1), (PiecPlayers[p].rect.x + 15, PiecPlayers[p].rect.y + 15)))
            if ("Player" in messages and "have" in messages):
                p, m = int(messages.split(" ")[1]), int(messages.split(" ")[3])
                money[p] = m
                if ("Player" in messages and "have" in messages):
                    messages = ""
            if (messages == "START GAME"):
                NowPage = ""
                time.sleep(0.5)
                Board(g, False)
            if (messages == "YOU LOSE"):
                client.send_data(f"ExitGame#{g}")
                all_objs.append(LOSEORWIN(load_image("Lose.png", colorkey=-1), (WIDTH // 2, HEIGHT // 2)))
            if (messages == "YOU WIN"):
                all_objs.append(LOSEORWIN(load_image("WIN.png", colorkey=-1), (WIDTH // 2, HEIGHT // 2)))
            if (messages == "UPDATE"):
                NowPage = ""
                time.sleep(0.5)
                Board(g, True)
            if (("TURN" in messages and int(messages.split(" ")[1]) == self.number) or (start and "TURN" in self.turn and int(self.turn.split(" ")[1]) == self.number)):
                # PiecPlayers[self.number].turn(random.randint(1, 6) + random.randint(1, 6))
                if ("TURN" in messages and int(messages.split(" ")[1]) == self.number):
                    messages = ""
                start = False
                temp = TURN(load_image("turn.png"), (WIDTH // 2, HEIGHT // 2), self.number)
                all_objs.append(temp)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    all_sprites.update(event) 
            if (chance == ''):
                try:
                    temp2.kill()
                    screen.fill(pygame.Color(33, 40, 43))
                except:
                    pass
            screen.blit(self.board, self.pos_board)
            all_sprites.draw(screen)
            all_sprites.update()
            jj = 0
            for i in range(len(self.players)):
                try:
                    text2 = font1.render(f'{self.players[self.all_games[g][i]]}', True, pygame.Color(colors[i]))
                    place2 = text2.get_rect(center=(WIDTH * 0.20, HEIGHT * 0.15 + (i * 180)))
                    screen.blit(text2, place2)
                    text3 = font1.render(f'{money[jj]}$', True, pygame.Color("white"))
                    place3 = text3.get_rect(center=(WIDTH * 0.20, HEIGHT * 0.20 + (i * 180)))
                    screen.blit(text3, place3)
                    jj += 1
                except:
                    pass
            if (chance != ''):
                text4 = font1.render(chance, True, pygame.Color('black'))
                place4 = text4.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(text4, place4)
            colors = ["red", "blue", "green", "purple", "orange"]
            pygame.display.flip()

# class Game:
#     def __init__(self):
#         button_quit = Button(55, 37)
#         button_back = Button(53, 35)
#         gaming = True

#         while gaming:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     gaming = False
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_ESCAPE:
#                         Main()

#             # screen.fill(pygame.Color(181, 184, 177))
#             # screen.fill(pygame.Color(135, 206, 250))
#             screen.fill(pygame.Color(64, 64, 64))

#             button_quit.draw(WIDTH - 55, 0, "", quit, 40)
#             button_back.draw(0, 0, "", Main, 10)

#             screen.blit(exit_menu, (WIDTH - 55, 0))
#             screen.blit(board, (((WIDTH - 948) // 2) + 300, (HEIGHT - 941) // 2))
#             screen.blit(back, (-1, -1))

#             pygame.display.update()


class BUY(pygame.sprite.Sprite):
    def __init__(self, image, pos, number):
        super().__init__(all_sprites)
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.number = number

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(args[0].pos):
                client.send_data(f"BUY {self.number}")


class TURN(pygame.sprite.Sprite):
    def __init__(self, image, pos, number):
        super().__init__(all_sprites)
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.number = number


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__(all_sprites)
        self.width = width
        self.height = height

    def draw(self, x, y, message, action=None, font_size=30, color=None):
        log = False
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if message == 'LoginAc' and online:
            log = True
            message = ''
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
    Start()

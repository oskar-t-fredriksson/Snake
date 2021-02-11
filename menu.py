import pygame
import json


class Menu:
    pygame.font.init()
    title_font = pygame.font.Font('assets/Acadian_Runes-Regular_PERSONAL_USE.ttf', 60)
    font = pygame.font.Font('assets/Acadian_Runes-Regular_PERSONAL_USE.ttf', 40)
    smallfont = pygame.font.Font('assets/Acadian_Runes-Regular_PERSONAL_USE.ttf', 35)

    SCREEN_HEIGHT = 800
    SCREEN_WIDTH = 800
    SCREEN_TITLE = 'SnakeSnack'
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    uname = ''
    uscore = 0

    def __init__(self):
        self.menu_screen = self.screen
        self.width = self.SCREEN_WIDTH
        self.height = self.SCREEN_HEIGHT
        self.running = True
        self.play_button = pygame.Rect(self.width / 2 - 200 / 2, self.height - 275, 200, 50)
        self.quit_button = pygame.Rect(self.width / 2 - 200 / 2, self.height - 200, 200, 50)
        self.uinput = self.smallfont.render(self.uname + '_', True, (255, 255, 255))
        self.score_board = load_score()

    def username(self, events):
        e = events
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_BACKSPACE:
                self.uname = self.uname[:-1]
            if e.key == pygame.K_RETURN:
                return self.uname
            else:
                pygame.key.set_repeat(500, 10)
                self.uname += e.unicode
                print(self.uname)

        self.uinput = self.smallfont.render(self.uname + '_', True, (255, 255, 255))

    def draw_menu(self):
        pygame.draw.rect(self.menu_screen, (255, 255, 255), pygame.Rect(200, 428, 400, 75), 2)
        pygame.draw.rect(self.menu_screen, (255, 255, 255), pygame.Rect(200, 180, 400, 250), 2)
        pygame.draw.rect(self.menu_screen, (26, 175, 96), self.play_button)
        pygame.draw.rect(self.menu_screen, (26, 175, 96), self.quit_button)
        self.menu_screen.blit(self.uinput, (225, 450))
        self.draw_text()

    def load_score(self):
        readfile = open('./assets/scores.json', )
        score_board = json.load(readfile)
        readfile.close()
        return score_board

    def draw_text(self):
        x = 187
        self.score_board = load_score()

        title_text = self.title_font.render(self.SCREEN_TITLE, True, ((26, 175, 96)))
        highscore_text = self.font.render('Highscores', True, ((255, 255, 255)))
        play_text = self.font.render('Play', True, ((255, 255, 255)))
        quit_text = self.font.render('Quit', True, ((255, 255, 255)))
        self.menu_screen.blit(title_text, (self.width / 2 - (title_text.get_rect().width / 2), 50))
        self.menu_screen.blit(highscore_text, (self.width / 2 - (highscore_text.get_rect().width / 2), 125))
        self.menu_screen.blit(play_text, (
            self.play_button.x + int(self.play_button.width / 2) - int(play_text.get_rect().width / 2),
            self.height - 275 + 5))
        self.menu_screen.blit(quit_text, (
            self.quit_button.x + int(self.quit_button.width / 2) - int(quit_text.get_rect().width / 2),
            self.height - 200 + 5))

        self.score_board.sort(key=lambda x: x.get('score'), reverse=True)
        for i in range(len(self.score_board)):
            score = self.smallfont.render(self.score_board[i].get('name'), True, (255, 255, 255))
            points = self.smallfont.render(str(self.score_board[i].get('score')), True, (255, 255, 255))
            self.menu_screen.blit(score, (220, x))
            self.menu_screen.blit(points, (535, x))
            x += 40

    def run_menu(self):
        running = True
        while running:

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                else:
                    self.username(event)

            mouse_pos = pygame.mouse.get_pos()
            if self.play_button.collidepoint(mouse_pos):
                if click:
                    running = False
            if self.quit_button.collidepoint(mouse_pos):
                if click:
                    pygame.quit()

            self.menu_screen.fill((0, 0, 0))
            self.draw_menu()
            pygame.display.update()


def save_score(score_board):
    with open('./assets/scores.json', 'w') as fp:
        json.dump(score_board, fp)


def load_score():
    readfile = open('./assets/scores.json', )
    score_board = json.load(readfile)
    readfile.close()
    return score_board

# pygame.init()
# menu = Menu()
# menu.run_menu()
# pygame.quit()

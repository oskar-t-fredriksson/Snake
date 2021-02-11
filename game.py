import pygame
import random
import menu
from menu import *

clock = pygame.time.Clock()


def random_snack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break
    return x, y


class Game:
    TICK_RATE = 10
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    PLAY_AREA_Y = (50, 850)
    ROWS = 20
    SCREEN_TITLE = 'SnakeSnack'
    snake_head_file = pygame.image.load('assets/snake.png')
    snack_body_file = pygame.image.load('assets/fish.png')
    snake_head = pygame.transform.scale(snake_head_file, (40, 40))
    snack_body = pygame.transform.scale(snack_body_file, (40, 40))
    paused = True
    score_font = pygame.font.Font('assets/Acadian_Runes-Regular_PERSONAL_USE.ttf', 35)
    score = 0

    game_over = False

    def __init__(self):
        self.title = self.SCREEN_TITLE
        self.width = self.SCREEN_WIDTH
        self.height = self.SCREEN_HEIGHT
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        self.game_screen.fill([0, 0, 0])
        self.snake = Snake(self.snake_head, (10, 10))
        self.snack = Cube(random_snack(self.ROWS, self.snake), self.snack_body)
        self.speed = 0
        self.menu = Menu()
        pygame.display.set_caption(self.title)

    def run_game_loop(self):
        self.game_over = False
        self.paused = True
        self.snake.reset((10, 10))
        self.score = 0

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_p or event.key == pygame.K_SPACE):
                    self.paused = not self.paused
            if not self.paused:
                self.snake.move()
                self.collision()

            menu.Menu.uscore = self.score
            self.redraw_window(self.game_screen)
            clock.tick(self.TICK_RATE)

        high_score = menu.load_score()
        high_score.sort(key=lambda x: x.get('score'), reverse=True)
        if self.score > high_score[-1].get('score'):
            high_score.pop(-1)
            high_score.append({'name': self.menu.uname, 'score': self.score})
        menu.save_score(high_score)

    def redraw_window(self, game_screen):
        game_screen.fill((59, 149, 191))
        self.snake.draw(game_screen)
        self.snack.draw(game_screen, False, True)
        self.show_score()
        pygame.display.update()

    def collision(self):
        snake = self.snake
        snack = self.snack
        if snake.body[0].pos == snack.pos:
            self.snake.add_segment()
            self.snack = Cube(random_snack(self.ROWS, self.snake), self.snack_body)
            self.score += 1

        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1:])):
                self.snake.reset((10, 10))
                self.game_over = True
                break

    def show_score(self):
        score = self.score_font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.game_screen.blit(score, (0, 0))


class Cube(object):
    ROWS = Game.ROWS
    SCREEN_WIDTH = Game.SCREEN_WIDTH
    snake_head = Game.snake_head
    snack_body = Game.snack_body

    def __init__(self, start, dnx=1, dny=0, sprite=snake_head, color=(160, 196, 50)):
        self.pos = start
        self.dnx = dnx
        self.dny = dny
        self.sprite = sprite
        self.color = color

    def move(self, dnx, dny):
        self.dnx = dnx
        self.dny = dny
        self.pos = (self.pos[0] + self.dnx, self.pos[1] + self.dny)

    def draw(self, game_screen, head=False, snack=False, rotation=0):
        dis = self.SCREEN_WIDTH // self.ROWS
        i = self.pos[0]
        j = self.pos[1]

        if not head and not snack:
            pygame.draw.circle(game_screen, self.color, (round(dis * (i + 1 / 2)), round(dis * (j + 1 / 2))),
                               dis // 2 - 5)
        elif snack and not head:
            pygame.Surface.blit(game_screen, self.snack_body, (dis * i, dis * j))
        elif head and not snack:
            pygame.Surface.blit(game_screen, pygame.transform.rotate(self.snake_head, rotation), (dis * i, dis * j))


class Snake(object):
    body = []
    turns = {}
    score = 0

    def __init__(self, sprite, pos):
        self.sprite = sprite
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dnx = -1
        self.dny = 0
        self.rotation = 90

    # Move the snake
    def move(self):
        keys = pygame.key.get_pressed()
        # Control the snake
        for key in keys:
            if keys[pygame.K_LEFT]:
                self.dnx = -1
                self.dny = 0
                self.turns[self.head.pos[:]] = [self.dnx, self.dny]
                self.rotation = 270

            if keys[pygame.K_RIGHT]:
                self.dnx = 1
                self.dny = 0
                self.turns[self.head.pos[:]] = [self.dnx, self.dny]
                self.rotation = 90

            if keys[pygame.K_UP]:
                self.dnx = 0
                self.dny = -1
                self.turns[self.head.pos[:]] = [self.dnx, self.dny]
                self.rotation = 180

            if keys[pygame.K_DOWN]:
                self.dnx = 0
                self.dny = 1
                self.turns[self.head.pos[:]] = [self.dnx, self.dny]
                self.rotation = 0

        # Delete last segment and change positions
        for i, segment in enumerate(self.body):
            p = segment.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                segment.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if segment.dnx == -1 and segment.pos[0] <= 0:
                    segment.pos = (segment.ROWS - 1, segment.pos[1])
                elif segment.dnx == 1 and segment.pos[0] >= segment.ROWS - 1:
                    segment.pos = (0, segment.pos[1])
                elif segment.dny == 1 and segment.pos[1] >= segment.ROWS - 1:
                    segment.pos = (segment.pos[0], 0)
                elif segment.dny == -1 and segment.pos[1] <= 0:
                    segment.pos = (segment.pos[0], segment.ROWS - 1)
                else:
                    segment.move(segment.dnx, segment.dny)

    # Reset the snake
    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.rotation = 90
        self.turns = {}
        self.dnx = -1
        self.dny = 0

    # Add segment to snake
    def add_segment(self):
        tail = self.body[-1]
        dx, dy = tail.dnx, tail.dny
        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dnx = dx
        self.body[-1].dny = dy
        self.score += 1

    # Draw the snake
    def draw(self, game_screen):
        for i, segment in enumerate(self.body):
            if i == 0:
                segment.draw(game_screen, True, False, self.rotation)
            else:
                segment.draw(game_screen)

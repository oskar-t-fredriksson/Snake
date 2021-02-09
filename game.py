import pygame
import random

clock = pygame.time.Clock()


class Game:
    TICK_RATE = 60
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 850
    PLAY_AREA_Y = (50, 800)
    SCREEN_TITLE = 'SnakeSnack'
    snake_head = pygame.image.load('assets/snake.png')
    snack_body = pygame.image.load('assets/snack.png')
    snack_body_scaled = pygame.transform.scale(snack_body,(40, 40))
    snack = Cube(randomSnack(rows, s), snack_body_scaled)

    game_over = False

    def __init__(self):
        self.title = self.SCREEN_TITLE
        self.width = self.SCREEN_WIDTH
        self.height = self.SCREEN_HEIGHT
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        self.game_screen.fill([0, 0, 0])
        pygame.display.set_caption(self.title)

    def run_game_loop(self):
        game_over = False
        i = 0  # Initialise rotation: Only for testing

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
            self.game_screen.fill([0, 0, 0])
            self.game_screen.blit(pygame.transform.rotate(self.snake_head, i),
                                  ((self.width - self.snake_head.get_width()) // 2,
                                   (self.height - self.snake_head.get_height()) // 2))  # Rotate snake: Only for testing
            pygame.display.update()
            clock.tick(self.TICK_RATE)
            i += 1  # Rotate one degree: Only for testing

    def redraw_window(self):
        pass

    def random_snack(self):
        pass

    def collision(self):
        pass


class Cube(object):
    ROWS = 20
    SCREEN_WIDTH = Game.SCREEN_WIDTH
    rotate = pygame.transform.rotate(snake_head, 90)


class Snake(object):
    body = []
    turns = {}

    def __init__(self, sprite, pos):
        self.sprite = sprite
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dnx = 0
        self.dny = 0

    # Move the snake
    def move(self):
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            # Control the snake and save directions
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dnx = -1
                    self.dny = 0
                    self.turns[self.head.pos[:]] = [self.dnx, self.dny]

                if keys[pygame.K_RIGHT]:
                    self.dnx = 1
                    self.dny = 0
                    self.turns[self.head.pos[:]] = [self.dnx, self.dny]

                if keys[pygame.K_UP]:
                    self.dnx = 0
                    self.dny = -1
                    self.turns[self.head.pos[:]] = [self.dnx, self.dny]

                if keys[pygame.K_DOWN]:
                    self.dnx = 0
                    self.dny = 1
                    self.turns[self.head.pos[:]] = [self.dnx, self.dny]

        # Delete last segment and change positions
        for i, segment in enumerate(self.body):
            p = segment.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                segment.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
                else:
                    if segment.dnx == -1 and segment[0] <= 0:
                        segment.pos = (segment.ROWS - 1, segment.pos[1])
                    elif segment.dnx == 1 and segment[0] >= segment.ROWS - 1:
                        segment.pos = (0, segment.pos[1])
                    elif segment.dny == 1 and segment[1] >= segment.ROWS - 1:
                        segment.pos = (segment.pos[0], 0)
                    elif segment.dny == -1 and segment[1] <= 0:
                        segment.pos = (segment.pos[1], segment.ROWS - 1)
                    else:
                        segment.move(segment.dnx, segment.dny)

    # Reset the snake
    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dnx = 0
        self.dny = 1

    # Add segment to snake
    def add_segment(self):
        tail = self.body[-1]
        dx, dy = tail.dnx, tail.dny
        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]+1)))

        self.body[-1].dnx = dx
        self.body[-1].dny = dy

    # Draw the snake
    def draw(self, game_screen):
        for i, segment in enumerate(self.body):
            if i == 0:
                segment.draw(game_screen, True)
            else:
                segment.draw(game_screen)

def randomSnack(rows, item):

    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break

    return (x,y)

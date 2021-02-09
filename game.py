import pygame

clock = pygame.time.Clock()


class Game:
    TICK_RATE = 60
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 850
    PLAY_AREA_Y = (50, 800)
    SCREEN_TITLE = 'SnakeSnack'
    snake_head = pygame.image.load('assets/snake.png')

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


class Snake(object):
    body = []



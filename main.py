import pygame
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'SnakeSnack'
clock = pygame.time.Clock()


class Game:
    TICK_RATE = 60
    is_game_over = False

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill([0, 0, 0])
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False

        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
            pygame.draw.rect(self.game_screen, [255, 255, 255], [400, 400, 100, 100])
            pygame.display.update()
            clock.tick(self.TICK_RATE)


# Start pygame
pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
quit()

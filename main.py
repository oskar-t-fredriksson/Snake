import pygame
import math
import random
from game import Game


# Start pygame
pygame.init()
new_game = Game()

while new_game.menu.running:   
    new_game.menu.run_menu()
    new_game.run_game_loop()

pygame.quit()
quit()

import pygame

pygame.font.init()
font = pygame.font.Font('assets/Acadian_Runes-Regular_PERSONAL_USE.ttf', 50)

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
SCREEN_TITLE = 'SnakeSnack'
menu_screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))

def run_menu(): 

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
           
        draw_menu()

        pygame.display.update()

def draw_menu():   

    screen_title_text = font.render(SCREEN_TITLE.upper(), True, (26,175,96))
    high_scores_text = font.render('Highscores', True, (255,255,255))
    play_text = font.render('Play', True, (255,255,255))
    quit_text = font.render('Quit', True, (255,255,255))

    menu_screen.fill((0,0,0))
    menu_screen.blit(screen_title_text, (SCREEN_WIDTH/2 - (screen_title_text.get_rect().width / 2), 50))
    menu_screen.blit(high_scores_text, (SCREEN_WIDTH/2 - (high_scores_text.get_rect().width / 2), 100))
    menu_screen.blit(play_text, (SCREEN_WIDTH/2 - (play_text.get_rect().width / 2), 550))
    menu_screen.blit(quit_text, (SCREEN_WIDTH/2 - (quit_text.get_rect().width / 2), 600))


pygame.init()
run_menu()
pygame.quit()
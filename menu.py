import pygame

pygame.font.init()
title_font = pygame.font.Font('assets/Acadian_Runes-Regular_PERSONAL_USE.ttf', 60)
font = pygame.font.Font('assets/Acadian_Runes-Regular_PERSONAL_USE.ttf', 40)

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
SCREEN_TITLE = 'SnakeSnack'
menu_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def run_menu(): 

    running = True
    while running:
       
        play_button = pygame.Rect(SCREEN_WIDTH/2 - 200/2, SCREEN_HEIGHT - 275, 200,50)
        quit_button = pygame.Rect(SCREEN_WIDTH/2 - 200/2, SCREEN_HEIGHT - 200, 200,50)
        pygame.draw.rect(menu_screen, (26,175,96), play_button) 
        pygame.draw.rect(menu_screen, (26,175,96), quit_button) 

        screen_title_text = title_font.render(SCREEN_TITLE, True, ((26,175,96)))
        high_scores_text = font.render('Highscores', True, ((255,255,255)))
        play_text = font.render('Play', True, ((255,255,255)))
        quit_text = font.render('Quit', True, ((255,255,255)))

        menu_screen.blit(screen_title_text, (SCREEN_WIDTH/2 - (screen_title_text.get_rect().width / 2), 50))
        menu_screen.blit(high_scores_text, (SCREEN_WIDTH/2 - (high_scores_text.get_rect().width / 2), 125))
        menu_screen.blit(play_text, (play_button.x + int(play_button.width / 2) - int(play_text.get_rect().width/2), SCREEN_HEIGHT - 275 + 5 ))
        menu_screen.blit(quit_text, (play_button.x + int(quit_button.width / 2) - int(quit_text.get_rect().width/2), SCREEN_HEIGHT - 200 + 5))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if play_button.collidepoint(mouse_x, mouse_y):
            if click:
                print('Play')
                
        if quit_button.collidepoint(mouse_x, mouse_y):
            if click:            
                pygame.quit()
                
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
          
        #draw_menu()    
        pygame.display.update()

    
pygame.init()
run_menu()
pygame.quit()
import pygame

class Menu:
    pygame.font.init()
    title_font = pygame.font.Font('assets/Acadian_Runes-Regular_PERSONAL_USE.ttf', 60)
    font = pygame.font.Font('assets/Acadian_Runes-Regular_PERSONAL_USE.ttf', 40)

    SCREEN_HEIGHT = 800
    SCREEN_WIDTH = 800
    SCREEN_TITLE = 'SnakeSnack'
    screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    def __init__(self):   
        self.menu_screen = self.screen
        self.width = self.SCREEN_WIDTH
        self.height = self.SCREEN_HEIGHT
        self.play_button = pygame.Rect(self.width/2 - 200/2, self.height - 275, 200,50)
        self.quit_button = pygame.Rect(self.width/2 - 200/2, self.height - 200, 200,50)

    def draw_menu(self):
        pygame.draw.rect(self.menu_screen, (26,175,96), self.play_button) 
        pygame.draw.rect(self.menu_screen, (26,175,96), self.quit_button) 
        self.draw_text()       
        
    def draw_text(self):
        title_text = self.title_font.render(self.SCREEN_TITLE, True, ((26,175,96)))
        highscore_text = self.font.render('Highscores', True, ((255,255,255)))
        play_text = self.font.render('Play', True, ((255,255,255)))
        quit_text = self.font.render('Quit', True, ((255,255,255)))
        self.menu_screen.blit(title_text, (self.width/2 - (title_text.get_rect().width / 2), 50))
        self.menu_screen.blit(highscore_text, (self.width/2 - (highscore_text.get_rect().width / 2), 125))
        self.menu_screen.blit(play_text, (self.play_button.x + int(self.play_button.width / 2) - int(play_text.get_rect().width/2), self.height - 275 + 5 ))
        self.menu_screen.blit(quit_text, (self.quit_button.x + int(self.quit_button.width / 2) - int(quit_text.get_rect().width/2), self.height - 200 + 5 ))
    
    def run_menu(self):
        running = True
        while running:    

            click = False      
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True  

            mouse_pos = pygame.mouse.get_pos()
            if self.play_button.collidepoint(mouse_pos):
                if click:
                    print('Play')              
            if self.quit_button.collidepoint(mouse_pos):
                if click:            
                    running = False

            self.draw_menu()
            pygame.display.update()


pygame.init()
menu = Menu()
menu.run_menu()
pygame.quit()
quit()
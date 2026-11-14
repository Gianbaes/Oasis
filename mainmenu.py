from config import *
from os.path import join
from levelselection import Levelselection

class Main_Menu:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Oasis_Menu")
        self.display_surface.fill('Yellow')
        self.overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.overlay.fill ((250, 225, 0, 50))

        self.buttonpos = 0
        self.maxbuttonpos = 4
        
               
    def menurun(self):

        pygame.mixer.music.load(os.path.join(BASE_DIR,'data', 'music', 'Menubg.wav'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        running = True
        self.enter = False

        while running:
            clicking = False
            endgame = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicking = True
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        if self.buttonpos <= self.maxbuttonpos:
                            if not self.buttonpos == 1:
                                self.buttonpos -= 1
                    if event.key == pygame.K_DOWN:
                        if self.buttonpos >= 0:
                            if not self.buttonpos == self.maxbuttonpos:
                                self.buttonpos += 1
                    if event.key == pygame.K_RETURN:
                        if self.buttonpos != 0 :
                            self.enter = True
                    
                                


            Menudow = pygame.image.load(os.path.join(BASE_DIR,'images', 'menudow.png')).convert()
            Menudow = pygame.transform.scale(Menudow, (WINDOW_WIDTH, WINDOW_HEIGHT))

            mouse_X, mouse_Y = pygame.mouse.get_pos()
            

            self.display_surface.blit(Menudow, (0,0))

            font = pygame.font.Font(None, 100)
            start_text = font.render(f"Start", True, "Yellow")
            start_rect = start_text.get_rect(
                center = (WINDOW_WIDTH//2 + 350,
                        WINDOW_HEIGHT//2)
            )

            font = pygame.font.Font(None, 100)
            levels_text = font.render(f"Levels", True, "Yellow")
            levels_rect = levels_text.get_rect(
                center = (WINDOW_WIDTH//2 + 350,
                        (WINDOW_HEIGHT//2) + 100 )
            )

            font = pygame.font.Font(None, 100)
            quit_text = font.render(f"Quit", True, "Yellow")
            quit_rect = start_text.get_rect(
                center = (WINDOW_WIDTH//2 + 350,
                        (WINDOW_HEIGHT//2) + 200)
            )

            font = pygame.font.Font(None, 40)
            Gamemodes_text = font.render(f"Gamemodes", True, "Yellow")
            Gamemodes_rect = start_text.get_rect(
                center = (WINDOW_WIDTH//2 + 350,
                        (WINDOW_HEIGHT//2) + 350)
            )

            box_rect_start = start_rect.inflate(95,20)
            
            box_rect_levels = levels_rect.inflate(40,20)

            box_rect_quit = quit_rect.inflate(95,20)

            box_rect_Gamemodes = Gamemodes_rect.inflate(100,20)

            #border
            pygame.draw.rect( self.display_surface,(255, 215, 0), box_rect_start, width=3, border_radius=15)

            pygame.draw.rect( self.display_surface,(255, 215, 0), box_rect_levels, width=3, border_radius=15)

            pygame.draw.rect( self.display_surface,(255, 215, 0), box_rect_quit, width=3, border_radius=15)

            pygame.draw.rect( self.display_surface,(255, 215, 0), box_rect_Gamemodes, width=3, border_radius=15)

            self.display_surface.blit (start_text, start_rect)
            self.display_surface.blit (levels_text, levels_rect)
            self.display_surface.blit (quit_text, quit_rect)
            self.display_surface.blit (Gamemodes_text, Gamemodes_rect)

            self.display_surface.blit(self.overlay, (0,0))

            mouse_alligned_start = start_rect.collidepoint((mouse_X, mouse_Y)) 
            mouse_alligned_levels = levels_rect.collidepoint((mouse_X, mouse_Y)) 
            mouse_alligned_quit = quit_rect.collidepoint((mouse_X, mouse_Y)) 
            mouse_alligned_Gamemodes = Gamemodes_rect.collidepoint((mouse_X, mouse_Y)) 

            mouse_alligned_any = (
                        mouse_alligned_start
                        or mouse_alligned_levels 
                        or mouse_alligned_quit  
                        or mouse_alligned_Gamemodes 
                        )

            if mouse_alligned_start or ( not mouse_alligned_any and self.buttonpos == 1) :
                pygame.draw.rect( self.display_surface,('white'), box_rect_start, border_radius=15)
                pygame.draw.rect( self.display_surface,(255, 215, 0), box_rect_start, width=3, border_radius=15)
                self.display_surface.blit (start_text, start_rect)
            if mouse_alligned_levels or ( not mouse_alligned_any and self.buttonpos == 2) :
                pygame.draw.rect( self.display_surface,('white'), box_rect_levels, border_radius=15)
                pygame.draw.rect( self.display_surface,(255, 215, 0), box_rect_levels, width=3, border_radius=15)
                self.display_surface.blit (levels_text, levels_rect)
            if mouse_alligned_quit or ( not mouse_alligned_any and self.buttonpos == 3) :
                pygame.draw.rect( self.display_surface,('white'), box_rect_quit, border_radius=15)
                pygame.draw.rect( self.display_surface,(255, 215, 0), box_rect_quit, width=3, border_radius=15)
                self.display_surface.blit (quit_text, quit_rect)
            if mouse_alligned_Gamemodes or ( not mouse_alligned_any and self.buttonpos == 4) :
                pygame.draw.rect( self.display_surface,('white'), box_rect_Gamemodes, border_radius=15)
                pygame.draw.rect( self.display_surface,(255, 215, 0), box_rect_Gamemodes, width=3, border_radius=15)
                self.display_surface.blit (Gamemodes_text, Gamemodes_rect)
    

            if mouse_alligned_start and clicking == True or self.buttonpos == 1 and self.enter:
                
                pygame.mixer.music.stop()
                return "start"
            
            if mouse_alligned_levels and clicking == True or self.buttonpos == 2 and self.enter:
                
                pygame.mixer.music.stop()
                return "levels"

            if mouse_alligned_quit and clicking == True  or self.buttonpos == 3 and self.enter:
                return "quit"
                endgame =  True

            if mouse_alligned_Gamemodes and clicking == True or self.buttonpos == 4 and self.enter:

                pygame.mixer.music.stop()
                return "Gamemodes"
            

        

            if endgame == True:
                pygame.quit()
                import sys ;sys.exit(1)

            pygame.display.update()

        pygame.quit()
        
       
    
        
                        
        

    
        



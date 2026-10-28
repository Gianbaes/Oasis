from config import *
from os.path import join
from levelselection import Levelselection

class Main_Menu:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Oasis_Menu")
        self.display_surface.fill('Yellow')
       
               
    def menurun(self):

        running = True

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


            Menudow = pygame.image.load(os.path.join(BASE_DIR,'images', 'menudow.png')).convert()
            Menudow = pygame.transform.scale(Menudow, (WINDOW_WIDTH, WINDOW_HEIGHT))

            mouse_X, mouse_Y = pygame.mouse.get_pos()
            

            font = pygame.font.Font(None, 100)
            start_text = font.render(f"Start", True, "Red")
            start_rect = start_text.get_rect(
                center = (WINDOW_WIDTH//2 + 350,
                        WINDOW_HEIGHT//2)
            )

            font = pygame.font.Font(None, 100)
            levels_text = font.render(f"Levels", True, "Red")
            levels_rect = levels_text.get_rect(
                center = (WINDOW_WIDTH//2 + 350,
                        (WINDOW_HEIGHT//2) + 100 )
            )

            font = pygame.font.Font(None, 100)
            quit_text = font.render(f"Quit", True, "Red")
            quit_rect = start_text.get_rect(
                center = (WINDOW_WIDTH//2 + 350,
                        (WINDOW_HEIGHT//2) + 200)
            )
            

            self.display_surface.blit(Menudow, (0,0))
            self.display_surface.blit (start_text, start_rect)
            self.display_surface.blit (levels_text, levels_rect)
            self.display_surface.blit (quit_text, quit_rect)
            

            mouse_alligned_start = start_rect.collidepoint((mouse_X, mouse_Y)) 
            mouse_alligned_levels = levels_rect.collidepoint((mouse_X, mouse_Y)) 
            mouse_alligned_quit = quit_rect.collidepoint((mouse_X, mouse_Y)) 
                        
            if mouse_alligned_start and clicking == True  :
                return "start"

            if mouse_alligned_levels and clicking == True  :
                return "levels"

            if mouse_alligned_quit and clicking == True  :
                return "quit"
                endgame =  True


            if endgame == True:
                pygame.quit()
                import sys ;sys.exit(1)

            pygame.display.update()

        pygame.quit()
        
       
    
        
                        
        

    
        



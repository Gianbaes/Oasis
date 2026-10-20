from config import *
import sys
from os.path import join


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

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicking = True


            Menudow = pygame.image.load(join('images', 'mainmenu.png')).convert()
            Menudow = pygame.transform.scale(Menudow, (WINDOW_WIDTH, WINDOW_HEIGHT))

            mouse_X, mouse_Y = pygame.mouse.get_pos()
            

            font = pygame.font.Font(None, 100)
            start_text = font.render(f"Start", True, "red")
            start_rect = start_text.get_rect(
                center = (WINDOW_WIDTH//2,
                        WINDOW_HEIGHT//2)
            )

            self.display_surface.blit(Menudow, (0,0))
            self.display_surface.blit (start_text, start_rect)

            mouse_alligned = start_rect.collidepoint((mouse_X, mouse_Y)) 
            

            if mouse_alligned and clicking == True  :
                return True
                

            pygame.display.update()

        pygame.quit()
        sys.exit()
    
        
                        
        

    
        



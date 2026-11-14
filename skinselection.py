from config import *
from os.path import join
from Oasis_Game import Oasis_Game


class SkinSelection():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Oasis_Skins")
        self.display_surface.fill ((15, 25, 60))
    
    def skinmenu(self):
        running = True

        pygame.event.clear()
        
        while running:
            clicking = False
         

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #self.running = False
                    #return False
                    pygame.quit()
                    sys.exit(1)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicking = True


            mouse_X, mouse_Y = pygame.mouse.get_pos()

            font = pygame.font.Font(None, 50)
            Back_text = font.render(f"Back", True, "White")
            Back_rect = Back_text.get_rect(
                center = (50,10 ))
            
            self.display_surface.blit (Back_text, Back_rect)
            
            mouse_alligned_Back = Back_rect.collidepoint((mouse_X, mouse_Y)) 
            
            self.display_surface.blit (Back_text, Back_rect)
          
           

            skin_1 = pygame.Rect(0, 0, 300, 550)
            skin_1.center = (
                    (WINDOW_WIDTH // 2) - 400,
                    WINDOW_HEIGHT // 2
            )
            pygame.draw.rect(self.display_surface,(255, 255, 255), skin_1, width = 3, border_radius = 14) 

            skin_1_head = pygame.Rect(0, 0, 300, 100)
            skin_1_head.center = (
                    (WINDOW_WIDTH // 2) - 400,
                    (WINDOW_HEIGHT // 2 ) + 100
            )
            pygame.draw.rect(self.display_surface,(255, 255, 255), skin_1_head, width = 3, border_radius = 14)




            skin_2 = pygame.Rect(0, 0, 300, 550)
            skin_2.center = (
                    (WINDOW_WIDTH // 2),
                    WINDOW_HEIGHT // 2
            )
            pygame.draw.rect(self.display_surface,(255, 255, 255), skin_2, width = 3, border_radius = 14)
            skin_2_head = pygame.Rect(0, 0, 300, 100)
            skin_2_head.center = (
                    (WINDOW_WIDTH // 2),
                    (WINDOW_HEIGHT // 2 ) + 100
            )
            pygame.draw.rect(self.display_surface,(255, 255, 255), skin_2_head, width = 3, border_radius = 14)
            





            if mouse_alligned_Back and clicking == True  :
                return "Back"
            pygame.display.update()

        pygame.quit()
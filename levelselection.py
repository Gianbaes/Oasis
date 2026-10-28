from config import *
from os.path import join
from Oasis_Game import Oasis_Game


class Levelselection():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Oasis_Levels")
        self.display_surface.fill ((15, 25, 60))
    


    def levelmenu(self):
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
            

            #fonts,pos
            font = pygame.font.Font(None, 50)
            lvl1_text = font.render(f"LVL 1", True, "White")
            lvl1_rect = lvl1_text.get_rect(
                center = (200,100 ))

            font = pygame.font.Font(None, 50)
            lvl2_text = font.render(f"LVL 2", True, "White")
            lvl2_rect = lvl2_text.get_rect(
                center = (400,100 ))

            font = pygame.font.Font(None, 50)
            lvl3_text = font.render(f"LVL 3", True, "White")
            lvl3_rect = lvl3_text.get_rect(
                center = (600,100 ))

            font = pygame.font.Font(None, 50)
            Back_text = font.render(f"Back", True, "White")
            Back_rect = Back_text.get_rect(
                center = (50,10 ))


            #borderrect
            box_rect_lvl1 = lvl1_rect.inflate(40,20)

            box_rect_lvl2 = lvl2_rect.inflate(40,20)

            box_rect_lvl3 = lvl3_rect.inflate(40,20)


            #border
            pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_lvl1, width=3, border_radius=15)

            pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_lvl2, width=3, border_radius=15)

            pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_lvl3, width=3, border_radius=15)



            #display
            self.display_surface.blit (lvl1_text, lvl1_rect)

            self.display_surface.blit (lvl2_text, lvl2_rect)
            
            self.display_surface.blit (lvl3_text, lvl3_rect)

            self.display_surface.blit (Back_text, Back_rect)

            
            #mouse
            mouse_alligned_lvl1 = lvl1_rect.collidepoint((mouse_X, mouse_Y)) 

            mouse_alligned_lvl2 = lvl2_rect.collidepoint((mouse_X, mouse_Y)) 

            mouse_alligned_lvl3 = lvl3_rect.collidepoint((mouse_X, mouse_Y)) 

            mouse_alligned_Back = Back_rect.collidepoint((mouse_X, mouse_Y)) 
            
                        
           #ifs
            if mouse_alligned_lvl1 and clicking == True  :
                return 0
            if mouse_alligned_lvl2 and clicking == True  :
                return 1
            if mouse_alligned_lvl3 and clicking == True  :
                return 2
            if mouse_alligned_Back and clicking == True  :
                return "Back"
            pygame.display.update()

        pygame.quit()
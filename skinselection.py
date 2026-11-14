from config import *
from os.path import join
from Oasis_Game import Oasis_Game
from players.daplayer import Player



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
            pygame.draw.rect(self.display_surface,(255, 255, 255), skin_1, width = 3, border_radius = 18) 

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
            pygame.draw.rect(self.display_surface,(255, 255, 255), skin_2, width = 3, border_radius = 18)
            skin_2_head = pygame.Rect(0, 0, 300, 100)
            skin_2_head.center = (
                    (WINDOW_WIDTH // 2),
                    (WINDOW_HEIGHT // 2 ) + 100
            )
            pygame.draw.rect(self.display_surface,(255, 255, 255), skin_2_head, width = 3, border_radius = 14)
            


            skin_1_image = pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', 'PlayerSkin_1' , 'Leftperson0.png')).convert_alpha()
            skin_1_image = pygame.transform.scale(skin_1_image, (skin_1.center[0] - 20, skin_1.center[1] - 60)) 
            self.display_surface.blit(skin_1_image, (
                    (WINDOW_WIDTH // 2) - 510,
                    WINDOW_HEIGHT // 2 - 250
            ))
            skin_2_image = pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', 'PlayerSkin_2', 'Leftperson0.png')).convert_alpha()
            skin_2_image = pygame.transform.scale(skin_2_image, (skin_2.center[0] - 80, skin_2.center[1] - 60)) 
            self.display_surface.blit(skin_2_image, (
                    (WINDOW_WIDTH // 2) - 280,
                    WINDOW_HEIGHT // 2  - 250
            ))



            font = pygame.font.Font(None, 65)
            Jack_text = font.render(f"Jack Sterling", True, "White")
            Jack_rect = (skin_1_head.center[0] - 130, skin_1_head.center[1] - 30)
            self.display_surface.blit (Jack_text, Jack_rect)
            font = pygame.font.Font(None, 100)
            Chloe_text = font.render(f"Chloe", True, "White")
            Chloe_rect = (skin_2_head.center[0] - 80, skin_2_head.center[1] - 30)
            self.display_surface.blit (Chloe_text, Chloe_rect)
            



            font = pygame.font.Font(None, 75)
            UseSkin1_text = font.render(f"Select", True, "White")
            UseSkin1_rect = UseSkin1_text.get_rect(
                center = (skin_1_head.center[0], skin_1_head.center[1] + 110))
            
            box_rect_UseSkin1 = UseSkin1_rect.inflate(40,20)

            pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_UseSkin1, width=3, border_radius=15)

            mouse_alligned_UseSkin1 = UseSkin1_rect.collidepoint((mouse_X, mouse_Y))

            if mouse_alligned_UseSkin1 :
                pygame.draw.rect( self.display_surface,(255, 215, 0), box_rect_UseSkin1, border_radius=15)
                pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_UseSkin1, width=3, border_radius=15)
                self.display_surface.blit (UseSkin1_text, UseSkin1_rect)
            else :
                pygame.draw.rect( self.display_surface,(15, 25, 60), box_rect_UseSkin1, border_radius=15)
                pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_UseSkin1, width=3, border_radius=15)
                self.display_surface.blit (UseSkin1_text, UseSkin1_rect)




            font = pygame.font.Font(None, 75)
            UseSkin2_text = font.render(f"Select", True, "White")
            UseSkin2_rect = UseSkin2_text.get_rect(
                center = (skin_2_head.center[0], skin_2_head.center[1] + 110))
            
            box_rect_UseSkin2 = UseSkin2_rect.inflate(40,20)

            pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_UseSkin2, width=3, border_radius=15)

            mouse_alligned_UseSkin2 = UseSkin2_rect.collidepoint((mouse_X, mouse_Y))

            if mouse_alligned_UseSkin2 :
                pygame.draw.rect( self.display_surface,(255, 215, 0), box_rect_UseSkin2, border_radius=15)
                pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_UseSkin2, width=3, border_radius=15)
                self.display_surface.blit (UseSkin2_text, UseSkin2_rect)
            else :
                pygame.draw.rect( self.display_surface,(15, 25, 60), box_rect_UseSkin2, border_radius=15)
                pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_UseSkin2, width=3, border_radius=15)
                self.display_surface.blit (UseSkin2_text, UseSkin2_rect)
            


            if Player.choosenskin == 0 :
                pygame.draw.rect(self.display_surface,(255, 215, 0), skin_1, width = 3, border_radius = 18)
                pygame.draw.rect(self.display_surface,(255, 255, 255), skin_2, width = 3, border_radius = 18)
            if Player.choosenskin == 1 :
                pygame.draw.rect(self.display_surface,(255, 215, 0), skin_2, width = 3, border_radius = 18)
                pygame.draw.rect(self.display_surface,(255, 255, 255), skin_1, width = 3, border_radius = 18)


            if mouse_alligned_UseSkin1 and clicking == True  :
                return "0" 
            if mouse_alligned_UseSkin2 and clicking == True  :
                return "1" 
            if mouse_alligned_Back and clicking == True  :
                return "Back"
            pygame.display.update()

        pygame.quit()
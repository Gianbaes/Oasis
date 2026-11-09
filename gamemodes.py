from config import *
from os.path import join
from Oasis_Game import Oasis_Game


class GameModeSelection():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Oasis_Gamemodes")
        self.display_surface.fill ((15, 25, 60))
        self.menudow1 = False
        self.menudow2 = False
    
    def gamemenu(self):
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
            
            Menudow = pygame.image.load(os.path.join(BASE_DIR,'images', 'menudow.png')).convert()
            Menudow = pygame.transform.scale(Menudow, (WINDOW_WIDTH, WINDOW_HEIGHT))

            Menudow2 = pygame.image.load(os.path.join(BASE_DIR,'images', '2menudow.png')).convert()
            Menudow2 = pygame.transform.scale(Menudow2, (WINDOW_WIDTH, WINDOW_HEIGHT))

            if self.menudow1 :
                self.display_surface.blit(Menudow, (0,0))

            elif self.menudow2 :
                self.display_surface.blit(Menudow2, (0,0))

            else:
                self.display_surface.fill ((15, 25, 60))


            HeadingBOX = pygame.Rect(0, 0, 800, 200)
            HeadingBOX.center = (
                    (WINDOW_WIDTH // 2),
                    0
            )

            pygame.draw.rect(self.display_surface,(15, 25, 60), HeadingBOX, border_radius = 10)

            #fonts,pos
            font = pygame.font.Font(None, 100)
            Halloween_text = font.render(f"Halloween", True, "White")
            Halloween_rect = Halloween_text.get_rect(
                center = (650,300 ))

            font = pygame.font.Font(None, 50)
            BACKbutton_text = font.render(f"BACK", True, "White")
            BACKbutton_rect = BACKbutton_text.get_rect(
                center = (650,600 ))

            
            
            font = pygame.font.Font(None, 150)
            Heading_text = font.render(f"GAMEMODES", True, "Yellow")
            Heading_rect = Heading_text.get_rect(
                center = (620,50 ))


            #borderrect
            box_rect_Halloween = Halloween_rect.inflate(40,20)

            box_rect_BACKbutton = BACKbutton_rect.inflate(40,20)

            

            #border
            pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_Halloween, width=3, border_radius=15)

            pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_BACKbutton, width=3, border_radius=15)

          
            #display
            self.display_surface.blit (Halloween_text, Halloween_rect)
            
            self.display_surface.blit (BACKbutton_text, BACKbutton_rect)
            
            
            self.display_surface.blit (Heading_text, Heading_rect)

            
            #mouse
            mouse_alligned_Halloween = Halloween_rect.collidepoint((mouse_X, mouse_Y)) 

            mouse_alligned_BACKbutton = BACKbutton_rect.collidepoint((mouse_X, mouse_Y)) 

            
           
            
            if mouse_alligned_Halloween :
                pygame.draw.rect( self.display_surface,(255, 215, 0), box_rect_Halloween, border_radius=15)
                pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_Halloween, width=3, border_radius=15)
                self.display_surface.blit (Halloween_text, Halloween_rect)
                self.menudow1 = False
                self.menudow2 = True

            elif mouse_alligned_BACKbutton :
                pygame.draw.rect( self.display_surface,(255, 215, 0), box_rect_BACKbutton, border_radius=15)
                pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_BACKbutton, width=3, border_radius=15)
                self.display_surface.blit (BACKbutton_text, BACKbutton_rect)
                
                self.menudow2 = False
                self.menudow1 = True

            else :
                self.display_surface.fill ((15, 25, 60))
        
            pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_Halloween, width=3, border_radius=15)
            
            pygame.draw.rect( self.display_surface,(255, 255, 255), box_rect_BACKbutton, width=3, border_radius=15)

            

            #display
            self.display_surface.blit (Halloween_text, Halloween_rect)

            self.display_surface.blit (BACKbutton_text, BACKbutton_rect)
            
            
            self.display_surface.blit (Heading_text, Heading_rect)



           
           #ifs
            if mouse_alligned_Halloween and clicking == True  :
                return "Hlw"
            if mouse_alligned_BACKbutton and clicking == True  :
                return "Back"
           
            pygame.display.update()

        pygame.quit()
from config import *
from os.path import join

class Main_Menu:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Oasis_Menu")

    def menurun(self):
        Menudow = pygame.image.load(join('images', 'mainmenu.png')).convert()
        Menudow = pygame.transform.scale(Menudow, (WINDOW_WIDTH, WINDOW_HEIGHT))

        font = pygame.font.Font(None, 50)
        start_text = font.render(f"Start", True, "red")
        start_rect = start_text.get_rect(
            center = (WINDOW_WIDTH//2,
                       WINDOW_HEIGHT//2)
        )
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    
        self.display_surface.blit(Menudow, (0,0))

        self.display_surface.blit (start_text, start_rect)
        

        pygame.display.update()


    
        pygame.QUIT()

    
        



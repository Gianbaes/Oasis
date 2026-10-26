from config import *
from daplayer import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from random import randint
from groups import TheSprites, Oasiss
import time
from mainmenu import Main_Menu


class Oasis_Game:
    def __init__(self):
        #initilize
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Oasis_Searcher")

        self.clock = pygame.time.Clock()
        self.running = True
        self.dead = False
        self.wintime = False
        self.pause = False
    
        self.currentlevel = 0
        self.lastlevel = 2

        #note to self - the groups
        self.the_sprites = TheSprites()
        self.Collision_SP = pygame.sprite.Group()
        self.BigCollision_SP = pygame.sprite.Group()
        self.Oasis = Oasiss()
        

        #note the sprite of character
        
        
        
        self.setup()

    def victory(self):
            clicking = False
            maxlevel = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicking = True

            WINdow = pygame.image.load(os.path.join(BASE_DIR, 'images', 'WINdow.png')).convert()
            WINdow = pygame.transform.scale(WINdow, (1000, 500))

            mouse_X, mouse_Y = pygame.mouse.get_pos()
            
            self.display_surface.blit( WINdow, (150,120))

            if  self.currentlevel >= self.lastlevel :
                  maxlevel = True

            if maxlevel == False :
                font = pygame.font.Font(None, 70)
                retry_text = font.render(f"Return", True, "yellow")
                retry_rect = retry_text.get_rect(center =
                                                    (650,560)
                                            )
    
                font = pygame.font.Font(None, 70)
                next_text = font.render(f"Next", True, "yellow")
                next_rect = next_text.get_rect(center =
                                                    (650,510)
                                            )
                next_rect.inflate(700,520)
                
                self.display_surface.blit (next_text, next_rect) 
                self.display_surface.blit (retry_text, retry_rect)

                mouse_alligned_next = next_rect.collidepoint((mouse_X, mouse_Y))

                if mouse_alligned_next and clicking == True  :
                        self.player.winning = False
                        self.wintime = False
                        self.currentlevel = self.currentlevel + 1
                        self.setup()
                                    
                    
                        return
                        pygame.display.update()

            else :

                font = pygame.font.Font(None, 100)
                retry_text = font.render(f"Return", True, "yellow")
                retry_rect = retry_text.get_rect(center =
                                                    (650,550)
                                            )
    
                self.display_surface.blit (retry_text, retry_rect)         
            
            mouse_alligned_return = retry_rect.collidepoint((mouse_X, mouse_Y)) 
                        
            self.wintime = True
            
           
            if mouse_alligned_return and clicking == True  :
                menu = Main_Menu()
                menu.menurun()
                  
                game = Oasis_Game()
                game.run()

                pygame.quit()

            pygame.display.update()
        
    def lose(self):

        clicking = False
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicking = True

        LOSEdow = pygame.image.load(os.path.join(BASE_DIR, 'images', 'LOSEdow.png')).convert()
        LOSEdow = pygame.transform.scale(LOSEdow, (1000, 500))

        mouse_X, mouse_Y = pygame.mouse.get_pos()

        font = pygame.font.Font(None, 100)
        return_text = font.render(f"Return", True, "Red")
        return_rect = return_text.get_rect(center =
                                        (650,570)
                                    )

        font = pygame.font.Font(None, 100)
        retry_text = font.render(f"Retry", True, "Red")
        retry_rect = retry_text.get_rect(center =
                                        (650,510)
                                    )
            
        self.display_surface.blit( LOSEdow, (150,120))

        self.display_surface.blit (return_text, return_rect)
        self.display_surface.blit (retry_text, retry_rect)
        
        mouse_alligned_retry = retry_rect.collidepoint((mouse_X, mouse_Y)) 
        mouse_alligned_return = return_rect.collidepoint((mouse_X, mouse_Y))

                    
        self.wintime = True

        if mouse_alligned_retry and clicking == True  :
            self.wintime = False
            self.setup()
            
            return

        if mouse_alligned_return and clicking == True  :
            menu = Main_Menu()
            menu.menurun()
                
            game = Oasis_Game()
            game.run()

            
            pygame.quit()

        pygame.display.update()

    def pausemenu(self):
                
                clicking = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            clicking = True
    
                menupause = pygame.Rect(0, 0, 400, 550)
                menupause.center = (
                      WINDOW_WIDTH // 2,
                      WINDOW_HEIGHT // 2
                )

                pygame.draw.rect(self.display_surface,(15, 25, 60), menupause, border_radius = 20)

                mouse_X, mouse_Y = pygame.mouse.get_pos()
                
                font = pygame.font.Font(None, 100)
                return_text = font.render(f"Return", True, "white")
                return_rect = return_text.get_rect(center =
                                                    (600,330)
                                            )

                font = pygame.font.Font(None, 90)
                resume_text = font.render(f"Resume", True, "white")
                resume_rect = return_text.get_rect(center =
                                                    (600,230)
                                            )

                self.display_surface.blit(resume_text, resume_rect)
                self.display_surface.blit(return_text, return_rect)
    
                mouse_alligned_resume = resume_rect.collidepoint((mouse_X, mouse_Y))
                mouse_alligned_return = return_rect.collidepoint((mouse_X, mouse_Y))

                if mouse_alligned_resume and clicking == True :
                      self.pause = False


                if mouse_alligned_return and clicking == True  :
                    menu = Main_Menu()
                    menu.menurun()
                    
                    game = Oasis_Game()
                    game.run()

                    pygame.quit()
                
    def setup(self): #maptile
        
        currentlevel = self.currentlevel

        self.the_sprites.empty()
        self.BigCollision_SP.empty()
        self.Collision_SP.empty()
        self.Oasis.empty()


        levelstime =[ 
                    60,
                    45,
                    30              
                ]

        self.time_left  = levelstime[currentlevel]

        spawnpoint = [
              (100,1200),
              (500,1020),
              (300,1710)
        ]
        

        playerlevel = spawnpoint[currentlevel]
        
        
        levels =[ 
            'level-0.tmx',
            'level-1.tmx',
            'level-2.tmx'              
        ]

        
        
        tmx_map = load_pygame(os.path.join(BASE_DIR, 'data', 'maps',levels[currentlevel]))

        for x, y, image in tmx_map.get_layer_by_name('Collision').tiles():
                    image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
                    CollisionSP(
                        (x * TILE_SIZE, y * TILE_SIZE),
                        image,
                        (self.the_sprites, self.Collision_SP)
                    )
        
        for x, y, image in tmx_map.get_layer_by_name('Background').tiles():
                    image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
                    Spriteg(
                        (x * TILE_SIZE, y * TILE_SIZE),
                        image,
                        self.the_sprites
                    )
        for x, y, image in tmx_map.get_layer_by_name('Oasis').tiles():
                    image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
                    Oasis(
                        (x * TILE_SIZE, y * TILE_SIZE),
                        image,
                        (self.the_sprites, self.Oasis)
                    )

        for x, y, image in tmx_map.get_layer_by_name('Big obstacle').tiles():
                            image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
                            CollisionSP(
                                    (x * TILE_SIZE, y * TILE_SIZE),
                                    image,
                                    (self.the_sprites, self.Collision_SP)
                            )

        for x, y, image in tmx_map.get_layer_by_name('Foreground').tiles():
                    image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
                    CollisionSP(
                            (x * TILE_SIZE, y * TILE_SIZE),
                            image,
                            (self.the_sprites, self.Collision_SP)
                    )

        self.player = Player(playerlevel, self.the_sprites, self.Collision_SP, self.BigCollision_SP, self.Oasis)
        
        self.the_sprites.add(self.player)

    def run(self):

        while self.running:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_SPACE:
                            self.pause = not self.pause

            if not self.pause:
                  
                self.the_sprites.update(dt) # updt sprite

                if self.wintime == False :
                    self.time_left -= dt
                    self.time_left = max(0, self.time_left)


            bgimg = pygame.image.load(os.path.join(BASE_DIR, 'images', 'background.png')).convert()
            bgimg = pygame.transform.scale(bgimg, (WINDOW_WIDTH, WINDOW_HEIGHT))

            
            
            self.display_surface.fill('Yellow')
            self.display_surface.blit(bgimg, (0,0))
            self.the_sprites.draw(self.player.rect.center) #draw the sprite hehe


            font = pygame.font.Font(None, 50)
            colortime = "blue"
            if self.time_left <= 10 :
                colortime = "Red"
            if self.time_left <= 30 and self.time_left > 10 :
                colortime = "Yellow"

            timer_countdown = font.render(f"Hydration level: {int(self.time_left)}", True, colortime)
            
            font = pygame.font.Font(None, 30)
            pausetext = font.render("Press SPACE to Pause", True, "Blue")

            self.display_surface.blit(timer_countdown,(500,0))
            self.display_surface.blit(pausetext,(0,650))

            if self.player.winning:

                self.victory()

            

            if self.time_left == 0 :
                self.lose()

            if self.pause:
                  self.pausemenu()
                  
            pygame.display.update()

        pygame.quit()
       
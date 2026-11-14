from config import *
from players.daplayer_hlw import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from random import randint
from groups import *
import time




class Halloween_Oasis:
    def __init__(self,currentlevel = 0 ):
        #initilize
        pygame.init()
        pygame.mixer.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.environment = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.environment.fill((2,2, 12, 200))
        
        pygame.display.set_caption("Oasis_Searcher_Halloween")


        self.clock = pygame.time.Clock()
        self.running = True
        self.dead = False
        self.wintime = False
        self.pause = False
        self.refilled = False
        self.damages = False
        self.sprint = False
        self.beastspawned = False
        
        self.beast = None
        self.beast_x = 0
        self.beast_y = 0
        self.refilledtimer = 0
        self.currentlevel = currentlevel
    
        #self.currentlevel = 0
        self.lastlevel = 2

        #note to self - the groups
        self.the_sprites = TheSprites()
        self.Collision_SP = pygame.sprite.Group()
        self.BigCollision_SP = pygame.sprite.Group()
        self.Smallcollision_SP = pygame.sprite.Group()
        self.Oasis = Oasiss()
        self.Wells = Wellss()
        self.Cactus = Cactuss()
        self.Chase = Chasee ()
        self.Beast_SP = Beastt()
        self.FakeOasis = FakeOasiss()
        

        #note the sprite of character
        
        
        
        self.setup()

    def victory(self):
            from mainmenu import Main_Menu


            clicking = False
            maxlevel = False
            nextlev = False 

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicking = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                                nextlev = not nextlev
                        

            WINdow = pygame.image.load(os.path.join(BASE_DIR, 'data', 'maps', 'haloween', 'WINdowH.png')).convert()
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

                if mouse_alligned_next and clicking == True or nextlev  :
                        self.player.winning = False
                        self.wintime = False
                        self.currentlevel = self.currentlevel + 1
                        self.setup()
                        self.gamerunning = True
                                    
                    
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
                self.running = False
                return "menu"

            pygame.display.update()
        
    def lose(self):
        from mainmenu import Main_Menu        

        retryy = False
        clicking = False
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicking = True
                if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RETURN:
                          retryy = not retryy


        LOSEdow = pygame.image.load(os.path.join(BASE_DIR, 'data', 'maps', 'haloween', 'LOSEdowH.png' )).convert()
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

        if mouse_alligned_retry and clicking == True  or retryy :

            self.wintime = False                 
            self.setup()
            self.gamerunning = True
            
            return
            

        if mouse_alligned_return and clicking == True  :
           self.running = False
           return "menu"

           

        pygame.display.update()

    def pausemenu(self):
                from mainmenu import Main_Menu
                                
                clicking = False
                returning = False 
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            clicking = True
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE :
                                    returning = True

    
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
                                                    (600,430)
                                            )

                font = pygame.font.Font(None, 100)
                reset_text = font.render(f"Reset", True, "white")
                reset_rect = reset_text.get_rect(center =
                                                    (600,330)
                                            )

                font = pygame.font.Font(None, 90)
                resume_text = font.render(f"Resume", True, "white")
                resume_rect = return_text.get_rect(center =
                                                    (600,230)
                                            )

                self.display_surface.blit(resume_text, resume_rect)
                self.display_surface.blit(return_text, return_rect)
                self.display_surface.blit(reset_text, reset_rect)
    
                mouse_alligned_resume = resume_rect.collidepoint((mouse_X, mouse_Y))
                mouse_alligned_return = return_rect.collidepoint((mouse_X, mouse_Y))
                mouse_alligned_reset = reset_rect.collidepoint((mouse_X, mouse_Y))

                if mouse_alligned_resume and clicking == True :
                    self.pause = False

                if mouse_alligned_reset and clicking == True :
                    self.setup()
                    self.pause = False

                if returning:
                    self.pause = False

                if mouse_alligned_return and clicking == True  :
                    self.running = False
                    return "menu"

    def chaseSEQ(self): #beast mechanics

        self.beasttime =[ 
                            0,
                            10,
                            15
                                       
                        ]
        
                 
        self.beastspeed = self.beasttime[self.currentlevel]

        self.beastmode = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.beastmode.fill((28,0, 0, 80))
         

        if self.beastspawned :

                if self.beast == None :
                        
                        beastimg = pygame.image.load(os.path.join(BASE_DIR, 'data', 'maps', 'haloween','beast.png')).convert_alpha()
                        beast_img = pygame.transform.scale (beastimg, (158,208))
                        
                        self.beast = Beast( (self.beast_x, self.beast_y),beast_img,
                        (self.the_sprites, self.Beast_SP)
                        )  

                self.display_surface.blit(self.beastmode, (0,0))
                font = pygame.font.Font(None, 50)
                beasttext = font.render("WARNING : Run to the Oasis now !, The beast has SPAWNED", True, "Red")
                self.display_surface.blit(beasttext,(200,40))
                        

                        

                target = pygame.math.Vector2(self.player.rect.center)
                beastpos = pygame.math.Vector2(self.beast.rect.center)
                newbeastpos = pygame.math.Vector2(self.beast.rect.center)
                min_d = 25
               
    
                distance = beastpos.distance_to(target)

                if self.gamerunning: 

                    if distance > min_d :
                            direction = (target - beastpos)/ distance 
        
                            newbeastpos = beastpos + direction * self.beastspeed

                            self.beast.rect.center = newbeastpos 
                else:
                     pass
                             
    def setup(self): #maptile
        
        #currentlevel = self.currentlevel

        #clearing every after level
        self.the_sprites.empty()
        self.BigCollision_SP.empty()
        self.Collision_SP.empty()
        self.Smallcollision_SP.empty()
        self.Oasis.empty()
        self.Wells.empty ()
        self.Cactus.empty()
        self.beast = None
        self.beastspawned = False
        
       
        self.levelstime =[ 
                    30,
                    40,
                    35
                               
                ]

        self.time_left  = self.levelstime[self.currentlevel]

        spawnpoint = [
              (100,1800),
              (20, 1900),
              (20,1900)
        ]
        

        playerlevel = spawnpoint[self.currentlevel]
        
        
        levels =[ 
            'halloween-1.tmx',
            'halloween-2.tmx',
            'halloween-3.tmx'
        
            ]

        self.max_hydrduration = self.levelstime[self.currentlevel]
        self.hydration_drainrate = 2

        scale_tiled = int(TILE_SIZE )
        
        tmx_map = load_pygame(os.path.join(BASE_DIR, 'data', 'maps', 'haloween', levels[self.currentlevel]))

        
        for x, y, image in tmx_map.get_layer_by_name('Background').tiles():
                    image = pygame.transform.scale(image, (scale_tiled, scale_tiled))
                    Spriteg(
                        (x * scale_tiled, y * scale_tiled),
                        image,
                        self.the_sprites
                    )
        for x, y, image in tmx_map.get_layer_by_name('Oasis').tiles():
                    image = pygame.transform.scale(image, (scale_tiled, scale_tiled))
                    Oasis(
                        (x * scale_tiled, y * scale_tiled),
                        image,
                        (self.the_sprites, self.Oasis)
                    )

       

        for x, y, image in tmx_map.get_layer_by_name('Foreground').tiles():
                    image = pygame.transform.scale(image, (scale_tiled, scale_tiled))
                    CollisionSP(
                            (x * scale_tiled, y * scale_tiled),
                            image,
                            (self.the_sprites, self.Collision_SP)
                    )
    
        for x, y, image in tmx_map.get_layer_by_name('Trees').tiles():
                    image = pygame.transform.scale(image, (scale_tiled, scale_tiled))
                    SmallcollisionSP(
                        (x * scale_tiled, y * scale_tiled),
                        image,
                        (self.the_sprites, self.Smallcollision_SP)
                    )
        if self.currentlevel >= 1:
            for x, y, image in tmx_map.get_layer_by_name('Beast Trigger').tiles(): #trigger collisioncheck for beast
                    self.beast_x = (x * scale_tiled) - 300
                    self.beast_y = (y * scale_tiled) - 300

                    image = pygame.transform.scale(image, (scale_tiled, scale_tiled))
                    Chase(
                        (x * scale_tiled, y * scale_tiled),
                        image,
                        (self.the_sprites, self.Chase)
                    )

            for x, y, image in tmx_map.get_layer_by_name('Fake Oasis').tiles():
                    image = pygame.transform.scale(image, (scale_tiled, scale_tiled))
                    FakeOasis(
                        (x * scale_tiled, y * scale_tiled),
                        image,
                        (self.the_sprites, self.FakeOasis)
                    )

                
        self.player = Player(playerlevel, self.the_sprites, self.Collision_SP, self.BigCollision_SP, 
                             self.Oasis, self.Wells, self.Cactus, self.Smallcollision_SP, 
                             self.Chase, self.Beast_SP, self.FakeOasis)
        
        self.the_sprites.add(self.player)

    def run(self):

        self.gamerunning = True

        pygame.mixer.music.load(os.path.join(BASE_DIR,'data', 'music', 'halloween.wav'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        
               
        

        while self.running:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_SPACE:
                            self.pause = not self.pause

            
            keyhold = pygame.key.get_pressed()
            if keyhold[pygame.K_LSHIFT]:
                self.sprint = True
            elif keyhold[pygame.K_RSHIFT]:
                self.sprint = True
            else :
                  self.sprint = False

            
            
            if self.gamerunning == True:
                self.the_sprites.update(dt) # updt sprite
                pygame.mixer_music.unpause()

                if self.wintime == False :
                    self.time_left -= dt
                    self.time_left = max(0, self.time_left)
                    self.current_hydrduration = max(0, self.time_left)

            else:
                pygame.mixer_music.pause()

            if not self.pause:
            
                self.stopgame = False
                self.gamerunning = True
                

            else:
                self.stopgame = True
                self.gamerunning = False
                pygame.mixer_music.pause()



            bgimg = pygame.image.load(os.path.join(BASE_DIR, 'data', 'maps', 'haloween', 'bg.png')).convert()
            bgimg = pygame.transform.scale(bgimg, (WINDOW_WIDTH, WINDOW_HEIGHT))

            self.display_surface.fill('Yellow')
            self.display_surface.blit(bgimg, (0,0)) 
            self.the_sprites.draw(self.player.rect.center) #draw the sprite hehe
            
            
                
                

            font = pygame.font.Font(None, 40)
            colortime = "white"
            if self.time_left <= 10 :
                colortime = "Red"
            if self.time_left <= 30 and self.time_left > 10 :
                colortime = "Yellow"

            timer_countdown = font.render(f"Hydration level: {int(self.time_left)}", True, colortime)
            
            font = pygame.font.Font(None, 30)
            pausetext = font.render("Press SPACE to Pause", True, "Blue")
            self.display_surface.blit(pausetext,(0,13))

            font = pygame.font.Font(None, 30)
            pausetext = font.render("Press SHIFT to Sprint", True, "Blue")

            self.display_surface.blit(pausetext,(0,30))




            # hydr bar---------------------
            hydrbar_width =300
            hydrbar_height = 30
            fill_ratio = self.time_left / self.max_hydrduration
            fill_width = int(hydrbar_width * fill_ratio)


            hydrbar_bg_rect = pygame.Rect(500, 10, hydrbar_width, hydrbar_height)
            pygame.draw.rect(self.display_surface, (50, 50, 50), hydrbar_bg_rect, border_radius = 4)

            if fill_width > 0 :
                  fill_rect = pygame.Rect(500,10, fill_width, hydrbar_height)
                  pygame.draw.rect(self.display_surface, (0,191,255), fill_rect, border_radius = 4)

            pygame.draw.rect(self.display_surface, (255, 255, 255), hydrbar_bg_rect, width=2, border_radius=4)


            self.display_surface.blit(timer_countdown,(520, 13))

            dark_ambience = self.environment = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
            self.environment.fill((2,2, 12, 200))

            pygame.draw.circle(dark_ambience,(0,5,0,120),(WINDOW_WIDTH // 2, WINDOW_HEIGHT//2), 50)

            self.display_surface.blit(self.environment, (0,0))

            if self.player.Replenish:
                  
                self.time_left = min(self.max_hydrduration , self.time_left + 5)

                self.player.Replenish = False

                self.refilled = True
                self.refilledtimer = .5

            if self.refilled:
                    font = pygame.font.Font(None, 75)
                    refilltext = font.render("+5", True, "Blue")
                    self.display_surface.blit(refilltext,(750, 23))

            if self.refilled :
                  self.refilledtimer -=  dt
                  if self.refilledtimer <= 0:
                        self.refilled = False


            if self.player.Damaged :

                if not self.damages:
                    self.time_left = min(self.max_hydrduration , self.time_left - 3)

                    self.player.Damaged = False

                    self.damages = True
                    self.damagestimer = .5

            if self.damages:

                if int(self.damagestimer * 2) % 2 == 0:
                    font = pygame.font.Font(None, 75)
                    damagetext = font.render("-3", True, "Red")
                    self.display_surface.blit(damagetext,(750, 23))
          
                self.damagestimer -=  dt
                if self.damagestimer <= 0:
                        self.damages = False


            if self.sprint == True :
                  self.player.speed = 700
                  self.time_left -= 2 * dt
                  font = pygame.font.Font(None, 30)
                  sprinttext = font.render("*sprinting*", True, "Red")
                  self.display_surface.blit(sprinttext,((WINDOW_WIDTH // 2) - 45,(WINDOW_HEIGHT // 2) + 35))
            else :
                  self.player.speed = 350
                  self.sprint = False


            if self.player.winning:
                self.gamerunning = False
                self.wintime = True
                self.victory()

            if self.player.chasePlayer: #leyman terms if collision true spawn beast
                self.beastspawned = True

            if self.beastspawned: #if there is beast do the chase seq
                 self.chaseSEQ()

            if self.time_left == 0 :
                self.player.lose = True
                
            if self.player.lose :
                self.gamerunning = False
                self.wintime = True
                self.lose()

            if self.current_hydrduration <= 0 :
                self.gamerunning = False
                self.wintime = True
                self.lose()


            if self.pause:
                  self.pausemenu()
 
            
            
            pygame.display.update()

        pygame.quit()
       
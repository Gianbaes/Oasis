from config import *



class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups, Collision_SP, BigCollision_SP, oasis ,
                  wells, cactus, mirageoasis, heatzones, quicksand, waterbottle):
        super().__init__(groups)

        self.choosenskin = 0

        self.playerskinfile =[ 
                            'PlayerSkin_1',
                            'PlayerSkin_2'        
                        ]
                
        self.playerskin = self.playerskinfile[self.choosenskin]


        self.frames_left = [
            pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', self.playerskin, 'Leftperson0.png')).convert_alpha(),
            pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', self.playerskin, 'Leftperson1.png')).convert_alpha(),
            pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', self.playerskin, 'Leftperson2.png')).convert_alpha()
            ]
        self.frames_right = [
            pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', self.playerskin, 'Rightperson0.png')).convert_alpha(),
            pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', self.playerskin, 'Rightperson1.png')).convert_alpha(),
            pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', self.playerskin, 'Rightperson2.png')).convert_alpha()
            ]


        self.frame_index = 0
        self.animation_speed = 8
        self.facing = 'right'
        self.image = self.frames_right[0]
        

        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-20,-10)


    #moving variable
        self.direction = pygame.Vector2()
        self.speed = 350
        self.Collision_SP = Collision_SP
        self.Oasis = oasis
        self.Wells = wells
        self.Cactus = cactus
        self.MirageOasis_SP = mirageoasis
        self.HeatZones = heatzones
        self.quicksand = quicksand
        self.waterbottle = waterbottle
        
        self.BigCollision_SP = BigCollision_SP
       

        self.winning = False
        
        self.Replenish = False
        self.Damaged = False
        self.heatstroked = False
        self.Toleft = False
        self.lose = False
        self.SawMirage = False
        self.quicksandstepped = False
        self.collect_bottle = False
        self.collect_bottlequest = False
        
        
    

    def input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a]) 

        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt): #reminder when adding a new def, add here
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.Bigcollision('horizontal')
        self.Oasis_colli('horizontal')
        self.Well_colli('horizontal')
        self.Cactus_colli('horizontal')
        self.MirageOasis('horizontal')
        self.Heat_colli('horizontal')
        self.QuickSand_colli('horizontal')
        self.Waterbottle_colli('horizontal')

        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
        self.Bigcollision('vertical')
        self.Oasis_colli('vertical')
        self.Well_colli('vertical')
        self.Cactus_colli('vertical')
        self.MirageOasis('vertical')
        self.Heat_colli('vertical')
        self.QuickSand_colli('vertical')
        self.Waterbottle_colli('vertical')
        
        self.rect.center = self.hitbox_rect.center

    def collision(self, direction): #collision logic
        for sprite in self.Collision_SP:
            if sprite.rect.colliderect(self.hitbox_rect): #hit wall
                if direction == 'horizontal':
                    if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top
                    if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom

    def Bigcollision(self, direction): #collision logic
            for sprite in self.BigCollision_SP:
                if sprite.rect.colliderect(self.hitbox_rect): #hit wall
                    if direction == 'horizontal':
                        if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                        if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                    else:
                        if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top
                        if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom

    def Oasis_colli(self, direction): #oaisis logic
            for sprite in self.Oasis:
                if sprite.rect.inflate(-40, -40).colliderect(self.hitbox_rect): #hit wall
                    if direction == 'horizontal':
                        if self.direction.x > 0: self.winning = True                        
                        if self.direction.x < 0: self.winning = True
                    else:
                        if self.direction.y > 0: self.winning = True
                        if self.direction.y < 0: self.winning = True

    def Well_colli(self, direction): #wells logic
            for sprite in self.Wells:
                if sprite.rect.inflate(+10, +10).colliderect(self.hitbox_rect): #hit wall
                    if direction == 'horizontal':
                        if self.direction.x > 0: self.Replenish = True                        
                        if self.direction.x < 0: self.Replenish = True
                    else:
                        if self.direction.y > 0: self.Replenish = True
                        if self.direction.y < 0: self.Replenish = True

                    kill_rect = sprite.rect.inflate (TILE_SIZE * 8, TILE_SIZE * 8)

                    for sprite in self.Wells:
                         if kill_rect.colliderect(sprite.rect): #note to self : parang ganto yan if killrect radius ay naghit or collide sa colliderect(self.hitbox) then sprite.kill
                            sprite.kill()

    def Cactus_colli(self, direction):
         self.Damaged = False
         for sprite in self.Cactus:

              if sprite.rect.inflate(+20,+20).colliderect(self.hitbox_rect):
                   self.Damaged = True

                   break

    def Heat_colli(self, direction):
             self.heatstroked = False
             for sprite in self.HeatZones:
    
                  if sprite.rect.inflate(+20,+20).colliderect(self.hitbox_rect):
                       self.heatstroked = True
    
                       break

    def MirageOasis(self, direction):
             for sprite in self.MirageOasis_SP:
    
                if sprite.rect.inflate(+20,+20).colliderect(self.hitbox_rect):

                    self.SawMirage = True
                        
                    kill_rect = sprite.rect.inflate (TILE_SIZE * 8, TILE_SIZE * 8)
                    
                    for sprite in self.MirageOasis_SP:
                        if kill_rect.colliderect(sprite.rect): #note to self : parang ganto yan if killrect radius ay naghit or collide sa colliderect(self.hitbox) then sprite.kill
                            sprite.kill()  

    def QuickSand_colli(self, direction):
             self.quicksandstepped = False
             for sprite in self.quicksand:
    
                  if sprite.rect.inflate(+20,+20).colliderect(self.hitbox_rect):
                       self.quicksandstepped = True
    
                       break

    def Waterbottle_colli(self, direction):
            self.collect_bottlequest = False
            
            for sprite in self.waterbottle:

                if sprite.rect.inflate(+50,+50).colliderect(self.hitbox_rect):
                   
                        self.collect_bottlequest = True

                        self.waterbottle_x = sprite.rect.centerx
                        self.waterbottle_y = sprite.rect.centery

                        if self.collect_bottle:
                            kill_rect = sprite.rect.inflate (TILE_SIZE * 4, TILE_SIZE * 4)
                            
                            for sprite in self.waterbottle:
                                if kill_rect.colliderect(sprite.rect): #note to self : parang ganto yan if killrect radius ay naghit or collide sa colliderect(self.hitbox) then sprite.kill
                                        sprite.kill()
                                        
                            self.collect_bottle = False
                            
                            break

    def animation(self, dt):

                    if self.direction.x < 0: self.facing = 'left'
                    elif self.direction.x > 0: self.facing = 'right'

               
                    if self.facing == 'left':
                         frames = self.frames_left
                    else:
                         frames = self.frames_right

                    

                    if self.direction:
                         self.frame_index += self.animation_speed *dt 
                         self.frame_index %= len(frames)
                    else:
                         self.frame_index = 0

                    self.image = frames[int(self.frame_index)]
                         
    def update(self, dt):
        self.input()
        self.move(dt)
        self.animation(dt)
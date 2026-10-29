from config import *


class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups, Collision_SP, BigCollision_SP, oasis , wells):
        super().__init__(groups)


        self.frames_left = [
            pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', 'Leftperson0.png')).convert_alpha(),
            pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', 'Leftperson1.png')).convert_alpha(),
            pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', 'Leftperson2.png')).convert_alpha()
            ]
        self.frames_right = [
            pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', 'Rightperson0.png')).convert_alpha(),
            pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', 'Rightperson1.png')).convert_alpha(),
            pygame.image.load (os.path.join(BASE_DIR,'images', 'animations', 'Rightperson2.png')).convert_alpha()
            ]


        self.frame_index = 0
        self.animation_speed = 8
        self.facing = 'right'
        self.image = self.frames_right[0]
        

        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-20,-10)


    #moving variable
        self.direction = pygame.Vector2()
        self.speed = 500
        self.Collision_SP = Collision_SP
        self.Oasis = oasis
        self.Wells = wells
        self.BigCollision_SP = BigCollision_SP

        self.winning = False
        self.Replenish = False
        self.Toleft = False
    

    def input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a]) 

        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

        self.direction = self.direction.normalize() if self.direction else self.direction


    def move(self, dt):
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.Bigcollision('horizontal')
        self.Oasis_colli('horizontal')
        self.Well_colli('horizontal')
        self.hitbox_rect.y += self.direction.y* self.speed * dt
        self.collision('vertical')
        self.Bigcollision('vertical')
        self.Oasis_colli('vertical')
        self.Well_colli('vertical')
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

    def Well_colli(self, direction): #oaisis logic
            for sprite in self.Wells:
                if sprite.rect.inflate(+10, +10).colliderect(self.hitbox_rect): #hit wall
                    if direction == 'horizontal':
                        if self.direction.x > 0: self.Replenish = True                        
                        if self.direction.x < 0: self.Replenish = True
                    else:
                        if self.direction.y > 0: self.Replenish = True
                        if self.direction.y < 0: self.Replenish = True


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
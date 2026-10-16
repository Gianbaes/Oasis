from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, Collision_SP, Oasis_SP):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'Leftperson.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-65,-30)

    #moving variable
        self.direction = pygame.Vector2()
        self.speed = 500
        self.Collision_SP = Collision_SP
        self.Oasis = Oasis_SP


    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.Oasis_colli('horizontal')
        self.hitbox_rect.y += self.direction.y* self.speed * dt
        self.collision('vertical')
        self.Oasis_colli('vertical')
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


    def Oasis_colli(self, direction): #collision logic
            for sprite in self.Oasis:
                if sprite.rect.colliderect(self.hitbox_rect): #hit wall
                    if direction == 'horizontal':
                        if self.direction.x > 0: print('wow')
                        if self.direction.x < 0: print('woww')
                    else:
                        if self.direction.y > 0: print('win')
                        if self.direction.y < 0: print('winn')
                    
    def update(self, dt):
        self.input()
        self.move(dt)
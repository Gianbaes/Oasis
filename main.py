from config import *
from daplayer import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from random import randint
from groups import TheSprites, Oasiss

class Game:
    def __init__(self):
        #initilize
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Oasis")
        self.clock = pygame.time.Clock()
        self.running = True

        #note to self - the groups
        self.the_sprites = TheSprites()
        self.Collision_SP = pygame.sprite.Group()
        self.Oasis = Oasiss()
        self.setup()

        #note the sprite of character
        self.player = Player((400,300), self.the_sprites, self.Collision_SP, self.Oasis)
        


    
    def setup(self): #maptile
        tmx_map = load_pygame(join('data', 'maps', 'level-1.tmx'))

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
        for x, y, image in tmx_map.get_layer_by_name('Foreground').tiles():
                    image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
                    CollisionSP(
                            (x * TILE_SIZE, y * TILE_SIZE),
                            image,
                            (self.the_sprites, self.Collision_SP)
                    )
        

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.the_sprites.update(dt) # updt sprite

            self.display_surface.fill('Yellow')
            self.the_sprites.draw(self.player.rect.center) #draw the sprite hehe



            pygame.display.update()
        pygame.quit()

#for running the loop

game = Game()
game.run()
from config import *
from daplayer import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from random import randint
from groups import TheSprites, Oasiss
import time


class Game:
    def __init__(self):
        #initilize
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Oasis")

        self.clock = pygame.time.Clock()
        self.running = True
        self.wintime = None
        self.restart_delay = 5000

        #note to self - the groups
        self.the_sprites = TheSprites()
        self.Collision_SP = pygame.sprite.Group()
        self.Oasis = Oasiss()
        self.setup()

        #note the sprite of character
        self.player = Player((500,1200), self.the_sprites, self.Collision_SP, self.Oasis)

    def victory(self):
            WINdow = pygame.image.load(join('images', 'WINdow.png')).convert()
            WINdow = pygame.transform.scale(WINdow, (1000, 500))

            self.display_surface.blit( WINdow, (270,120))
            pygame.display.update()

            time.sleep(5)
            self.wintime = None
            pygame.quit()
            game = Game()
            game.run()



    
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

            bgimg = pygame.image.load(join('images', 'background.png')).convert()
            bgimg = pygame.transform.scale(bgimg, (WINDOW_WIDTH, WINDOW_HEIGHT))
            
            
            self.display_surface.fill('Yellow')
            self.display_surface.blit(bgimg, (0,0))
            self.the_sprites.draw(self.player.rect.center) #draw the sprite hehe

            if self.player.winning:
                self.victory()

                  
            pygame.display.update()


pygame.quit()
game = Game()
game.run()
#for running the loop


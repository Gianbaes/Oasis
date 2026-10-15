from config import *
from daplayer import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from random import randint

class Game:
    def __init__(self):
        #initilize
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Oasis")
        self.clock = pygame.time.Clock()
        self.running = True

        #note to self - the groups
        self.the_sprites = pygame.sprite.Group()
        self.Collision_SP = pygame.sprite.Group()

        self.setup()

        #note the sprite
        self.player = Player((400,300), self.the_sprites, self.Collision_SP)
        


    
    def setup(self):
        tmx_map = load_pygame(join('data', 'maps', 'level-1.tmx'))

        for x, y, image in tmx_map.get_layer_by_name('Background').tiles():
            image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
            Spriteg(
                (x * TILE_SIZE, y * TILE_SIZE),
                image,
                self.the_sprites
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

            self.display_surface.fill('Black')
            self.the_sprites.draw(self.display_surface) #draw the sprite hehe



            pygame.display.update()
        pygame.quit()

#for running the loop

game = Game()
game.run()
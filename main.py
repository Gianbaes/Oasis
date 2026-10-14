import pygame
import inputcode
from daplayer import Player
from sprite import sprites, Sprite
from damap import TileKind, Map 
from camera import create_screen

pygame.init()

screen = create_screen(800, 600, "Oasis game")



clear_color = (255, 239, 174) 
running = True
player = Player("images/player.png", 200,150)
tile_kinds = [
    TileKind("sand", "images/sand.png", False),
    TileKind("cactus","images/Cacti.png", False)
]
map = Map("mapa/start.map", tile_kinds, 32)
Sprite("images/Pyramid.png", 7 * 32, 4*32)
Sprite("images/Phynx.png",  200, 50)
Sprite("images/Oasis.png", 400, 550)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            inputcode.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            inputcode.keys_down.remove(event.key)
    #upd code
    player.update()

    #drawing
    screen.fill(clear_color)
    map.draw(screen)
    for s in sprites:
        s.draw(screen)
    pygame.display.flip()

    pygame.time.delay(15)

pygame.quit()
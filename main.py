from config import *
from mainmenu import Main_Menu
from Oasis_Game import Oasis_Game
from daplayer import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from random import randint
from groups import TheSprites, Oasiss
import time

menu = Main_Menu()



menu.menurun()   
if menu.menurun():
    game = Oasis_Game()
    game.run()


pygame.quit()

#for running the loopdddd


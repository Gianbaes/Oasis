from config import *
from mainmenu import Main_Menu
from Oasis_Game import Oasis_Game
from daplayer import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from random import randint
from groups import TheSprites, Oasiss
import time
from levelselection import Levelselection

menu = Main_Menu()
levels = Levelselection()

menu.menurun()  
if menu.menurun():
    game = Oasis_Game()
    game.run()

if levels.levelmenu() return "0" :
    self.currentlevel + 0




pygame.quit()

#for running the loopdddd


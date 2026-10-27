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


while True:
    menu = Main_Menu()

    
    action = menu.menurun() 

    if action == "start" :
        game = Oasis_Game()
        game.setup
        game.run()

    elif action == "levels" :

        levelsmenu = Levelselection()
        choosedlevel = levelsmenu.levelmenu()

        if choosedlevel is not None :
            game = Oasis_Game(choosedlevel)
            game.setup()
            game.run()
    elif action == "quit" or action is None:
        break

pygame.quit()

#for running the loopdddd


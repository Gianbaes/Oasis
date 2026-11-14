from config import *
from mainmenu import Main_Menu
from Oasis_Game import Oasis_Game
from players.daplayer import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from random import randint
from groups import TheSprites, Oasiss
import time
import json
from levelselection import Levelselection
from HalloweenOasis import Halloween_Oasis
from gamemodes import GameModeSelection
from skinselection import SkinSelection


with open("skin.json", "r") as skinsavedata :
        Player.choosenskin = json.load(skinsavedata)["choosenskin"]


while True:
    menu = Main_Menu()
 
    action = menu.menurun() 
    

    if action == "start" :
        game = Oasis_Game()
        game.setup
        game.run()

    elif action == "Gamemodes" :
        gamemodes = GameModeSelection()
        choosedgm = gamemodes.gamemenu()

        if choosedgm == "Back":
                    pass
        
        elif choosedgm == "Hlw" :
            Hlw = Halloween_Oasis()
            Hlw.setup
            Hlw.run()

    elif action == "Skins" :
            Skinsmenu = SkinSelection()
            choosedskin = Skinsmenu.skinmenu()

            if choosedskin == "Back":
                        pass
            elif choosedskin is not None :
                        Player.choosenskin = int(choosedskin)
                        with open("skin.json", "w") as skinsavedata :
                            json.dump({"choosenskin": Player.choosenskin}, skinsavedata )
                         

    elif action == "levels" :

        levelsmenu = Levelselection()
        choosedlevel = levelsmenu.levelmenu()

        if choosedlevel == "Back":
            pass

        elif choosedlevel is not None :
            game = Oasis_Game(choosedlevel)
            game.setup()
            game.run()

    
    elif action == "quit" or action is None:
        break

pygame.quit()


#for running the loopdddd


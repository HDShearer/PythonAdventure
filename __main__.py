import os
import random as r
import map as M

from colorama import Fore, Style

import mainPlayer as P

# print(Style.RESET_ALL)

# Define all variables, lists, etc

actions = {"look": "Look", "go": "Go", "clear": "Clear", "help": "Help", "attack": "Attack", "map": "Map"}

global currentPlayer
PlayerNotDead = True
EnemyNotDead = True
turn = 0
gameQuit = False
attack = True


class Game:
    @staticmethod
    def __init__():
        pass

    @staticmethod
    def clearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def setupGame():
        global currentPlayer
        P.Name = input(Fore.CYAN + "What is your name, Hero? > ")
        Race = input("Are you an elf, dwarf, or human? > ")
        Race = str(Race.lower())
        if Race == "elf":
            P.Race = "Elf"
        elif Race == "dwarf":
            P.Race = "Dwarf"
        elif Race == "human":
            P.Race = "Human"
        else:
            print("What?")
            Game.setupGame()
        Class = ""
        if Race == "human":
            Class = input("Are you a rogue or a monk? > ")
            print(Style.RESET_ALL)
            Class = str(Class.lower())
            if Class == "rogue":
                currentPlayer = P.Rogue()
            elif Class == "monk":
                currentPlayer = P.Monk()
            else:
                print("What?")
                Game.setupGame()
        elif Race == "elf":
            Class = input("Are you a ranger or a mage? > ")
            print(Style.RESET_ALL)
            Class = str(Class.lower())
            if Class == "ranger":
                currentPlayer = P.Ranger()
            elif Class == "mage":
                currentPlayer = P.Mage()
            else:
                print("What?")
                Game.setupGame()
        elif Race == "dwarf":
            Class = input("Are you a cleric or a barbarian? > ")
            print(Style.RESET_ALL)
            Class = str(Class.lower())
            if Class == "cleric":
                currentPlayer = P.Cleric()
            elif Class == "barbarian":
                currentPlayer = P.Barbarian()
            else:
                print("What?")
                Game.setupGame()
        print(f"Rise {P.Name} the {Race} {Class}. The kingdom needs you!")

    @staticmethod
    def UpdateGame():
        pass

    @staticmethod
    def Help():
        print("\n")
        for action in actions:
            currentAction = actions[action]
            print(Fore.RED + currentAction)
        print("\n")
        print(Fore.RED + "Red text designates errors or help commands")
        print(Fore.CYAN + "Cyan text designates meta information, such as menus and game setup.")
        print(Fore.GREEN + "Green text designates information about something you see.")
        print(Fore.YELLOW + "Yellow text designates combat actions")
        print(Fore.BLUE + "Blue text designates conversations with NPCs.")
        print(Fore.MAGENTA + "Purple text designates all other player actions.")
        print(Style.RESET_ALL + "Plain text designates commands you enter.")
        print(Style.RESET_ALL)

    @staticmethod
    def TakeInput(x):
        x = x.lower()
        args = x.split(' ')
        length = len(args)
        if args[0] in actions:
            if args[0] == "look":
                P.Player.Look(currentPlayer, args[length - 1])
            elif args[0] == "clear":
                Game.clearScreen()
            elif args[0] == "help":
                Game.Help()
            elif args[0] == "attack":
                P.Player.Attack(currentPlayer, args[length - 1])
            elif args[0] == "map":
                M.Map.showMap(map)
            else:
                print(Fore.RED + "I don't know what you mean")
                print(Style.RESET_ALL)

    @staticmethod
    def RandomEncounter(Monster):
        # add individual monster noises)
        EnemyRoll = r.randint(0, 20)
        PlayerRoll = r.randint(0, 20)
        if EnemyRoll > PlayerRoll:
            pass
        else:
            pass

    @staticmethod
    def initiate():
        Game.clearScreen()
        Game.setupGame()
        P.Player.inv.clear()
        map = M.Map()

    @staticmethod
    def MainLoop():
        Game.UpdateGame()
        Game.TakeInput(input("> "))

    @staticmethod
    def GetLoot(Monster, DC):
        DC = int(DC)
        if DC % 2 == 0:
            lowBound = int(DC / 2)
        else:
            lowBound = int((DC + 1) / 2)
            lootCheck = r.randint(lowBound, DC)
        if lootCheck == 1:
            print(f"The {Monster} had nothing.")
            P.Player.inv.append(None)
        else:
            pass


# run game
Game.initiate()
while gameQuit == False:
    Game.MainLoop()

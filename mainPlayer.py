import random as r

from colorama import Fore, Style

import enemies as E
# import items as I
import rooms as R

global roomIn


class Player(object):
    roomName = "spawn"
    global roomIn
    roomIn = 0
    damage = 0
    Race = '"gnOwO whats this?" *gnotices bulge*'
    armor = 0
    HP = 0
    Roll = 0
    inv = {}
    gold = 0
    Name = ""

    def getLoot(self, x, DC):
        pass

    def Attack(self, x):
        global attack
        global EnemyHP
        global EnemyArmor
        global EnemyNotDead
        global PlayerNotDead
        Enemy = E.Goblin()
        EnemyNotDead = True
        PlayerNotDead = True
        attack = True
        if x in E.monsters:
            if attack == True:
                if PlayerNotDead and EnemyNotDead:
                    checkForHit = r.randint(0, 20)
                    print(checkForHit)
                    if checkForHit >= Enemy.armor:
                        damageDealt = r.randint(0, 20)
                        damageDealt += self.damage
                        Enemy.HP -= damageDealt
                        print(Fore.YELLOW + f"You did {damageDealt} damage to the {x}")
                        if Enemy.HP <= 0:
                            print(f"You killed the {x}!")
                            EnemyNotDead = False
                            attack = False
                            print(Style.RESET_ALL)
                        else:
                            pass  # continue fight
                    else:
                        print(Fore.YELLOW + "It hit the armor.")  # hit armor
                else:
                    pass  # end combat
            else:
                print(Fore.RED + "There is nothing to attack!")
                print(Style.RESET_ALL)
        else:
            print(Fore.RED + "Attack what?")
            print(Style.RESET_ALL)

    def Look(x):
        print(Fore.GREEN)
        if x == "look":
            x = roomIn
            print(R.rooms[x])
            print(Style.RESET_ALL)
        elif x in I.items:
            print(I.items[x])
            print(Style.RESET_ALL)
        elif x in E.monsters:
            print(E.monsters[x])
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "What?")
            print(Style.RESET_ALL)


class Elf(Player):
    pass


class Human(Player):
    pass


class Dwarf(Player):
    pass


# Elf Classes
class Mage(Elf):
    pass


class Ranger(Elf):
    pass


# Human Classes
class Monk(Human):
    pass


class Rogue(Human):
    pass


# Dwarf Classes
class Cleric(Dwarf):
    pass


class Barbarian(Dwarf):
    pass

import random as r
import __main__ as main
from colorama import Fore, Style

import enemies as E
import items as I
import rooms as R

global roomIn
global x
global y


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
    x = 3
    y = 6

    def getLoot(self, x, DC):
        pass

    def Attack(self, x):
        global attack
        global EnemyHP
        global EnemyArmor
        global EnemyNotDead
        global PlayerNotDead
        curEnemy = None
        Enemy = {E.goblin.Type: E.goblin}
        print(E.goblin.Type)
        EnemyNotDead = True
        PlayerNotDead = True
        attack = True
        Output = None
        if attack == True:
            if PlayerNotDead and EnemyNotDead:
                checkForHit = r.randint(0, 20)
                print(checkForHit)
                if checkForHit >= Enemy[x].armor:
                    damageDealt = r.randint(0, 20)
                    damageDealt += self.damage
                    Enemy[x].HP -= damageDealt
                    print(Fore.YELLOW +
                          f"You did {damageDealt} damage to the {x}")
                    Output = f"You did {damageDealt} damage to the {x}"
                    if Enemy[x].HP <= 0:
                        print(f"You killed the {x}!")
                        Output = f"You killed the {x}!"
                        EnemyNotDead = False
                        attack = False
                        print(Style.RESET_ALL)
                    else:
                        pass  # continue fight
                else:
                    print(Fore.YELLOW + "It hit the armor.")  # hit armor
                    Output = "It hit the armor."
            else:
                Output = 'You won!'
                pass  # end combat
        else:
            Output = "There is nothing to attack!"
            print(Fore.RED + "There is nothing to attack!")
            print(Style.RESET_ALL)
        return Output

    def Look(self, x):
        global lookObject
        print(Fore.GREEN)
        if x == "look":
            x = roomIn
            print(R.rooms[x])
            print(Style.RESET_ALL)
            lookObject = "What?"
        # elif x in I.items:
            # print(I.items[x])
            # print(Style.RESET_ALL)
        elif x in E.monsters:
            print(E.monsters[x])
            print(Style.RESET_ALL)
        else:
            lookObject = "What?"
            print(Fore.RED + "What?")
            print(Style.RESET_ALL)
        return lookObject, roomIn


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

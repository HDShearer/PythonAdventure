import random as R

import mainPlayer as P

monsters = {"goblin": "A stubby little green thing", }


class Enemy(object):
    roomIn = ("spawn")
    damagelow = 0
    damagehigh = 0
    damagemod = 0
    BattleCry = "lel I'm a monster"
    armor = 0
    HP = 0
    Roll = 0
    RollMod = 0
    DC = 0
    Type = ""

    def attack(self):
        self.Roll = R.randint(0, 20)
        self.Roll += self.RollMod
        self.damage = R.randint(self.damagelow, self.damagehigh)
        self.damage += self.damagemod
        if self.Roll >= P.Player.HP:
            P.Player.HP -= self.damage
            print(f"The {self.Type} does {self.damage} points of damage. You have {P.Player.HP} health left.")
            if P.Player.HP <= 0:
                pass
        else:
            print(f"The {self.Type} missed you.")


class goblin(Enemy):
    Type = "goblin"
    def __init__(self):
        self.HP = R.randint(1, 6)
        self.damagelow = 1
        self.damagehigh = 6
        self.damagemod = 2
        self.armor = 15
        self.RollMod = 4
        self.BattleCry = "The goblin charges out of the brush! ...And then trips. Prepare to fight!"
        self.Type = "goblin"


class bugbear(Enemy):
    def __init__(self):
        for i in range(0, 4):
            self.HP += R.randint(1, 8)
        self.HP += 5
        self.damagelow = 2
        self.damagehigh = 16
        self.damagemod = 2
        self.armor = 16
        self.RollMod = 4
        self.BattleCry = "ROARRRRRRRRR"
        self.Type = "goblin"

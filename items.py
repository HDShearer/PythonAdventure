import random

# why'd you have to make it dictionaries?
category = {"weapon": 0, "key": 1, 'food': 2, 'armour': 3}

# name: {(type), "description", (stat)} ## stat is dependant on the type. A weapon (0) would have a damage stat. A
# key (1) has a stat that unlocks a lock of the corresponding value, food (2) is health restored, etc.
# after the stat is the rarity. The item is determined by a 0 in (the rarity) to be in a chest or dropped by an enemy.

# this one is for generic items you find in chests, in rooms, etc.
itemsGeneric = {"sword": [0, "A sharp hunk of metal, perfect for decapitating enemies!", 5, 25],
                "key": [1, " This ornately carved piece of bronze looks perfect for opening a lock", 0, 25],
                'ration': [2,
                           "This is a standard-issue ration. Not too tasty, but supplies you with the energy you need "
                           "for adventuring.", 10, 6],
                'leather armour': [3, 'A simple set of armour made from cheap hide. '
                                      'It does not offer much defence.', 3, 25]}

# this one is for items dropped by orks
orkItems = {'rusted ax': [0, 'A hunk of rusting iron crudely shaped into a blade then fitted onto a tree branch.',
                          7, 2],
            'rotting meat': [1, 'It has a putrid smell. No maggots yet, so it is still safe to eat.', 4, 3]}

Inventory = None


def generateGeneric(self):
    random_item_key = None
    LIST = random.choice(list(category.keys()))
    type = category[LIST]
    # attempts to generate a random item until it is the matching type
    while True:
        random_item_key = random.choice(list(itemsGeneric.keys()))
        name = itemsGeneric[random_item_key]
        print(name[0])
        if name[0] == type:
            break
        else:
            continue
    return random_item_key


# creates a starting inventory. Will add different variations based on the race the player picked.
def startingInventory(self):
    Inventory = {0: items['sword'], 1: items['ration'], 2: items['leather armour']}
    return Inventory


# use to save current inventory when save command is added
def saveInventory(self):
    try:
        inventory_writer = open('inventory.txt', 'w')
        count = 0
        for entries in Inventory:
            inventory_writer.write(Inventory[count])
            inventory_writer.write('\n')
            count += 1

    except IOError:
        print('Error writing to inventory.txt. Type save to try again')
    return


def readInventory(self):
    inventory = Inventory
    count = 0
    inventory_load = open('inventory.txt', 'r')
    inventory_state = list(inventory_load.readlines())
    count = 0
    for line in inventory_state:
        inventory[count]: line
        count += 1
        # for debugging
        print(inventory)

    # returns saved inventory
    return inventory

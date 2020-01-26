import random

# why'd you have to make it dictionaries?
category = {"weapon": 0, "key": 1, 'food': 2}

# name: {(type), "description", (stat)} ## stat is dependant on the type. A weapon (0) would have a damage stat. A
# key (1) has a stat that unlocks a lock of the corresponding value, food (2) is health restored, etc.
items = {"sword": [0, "A sharp hunk of metal, perfect for decapitating enemies!", 5],
         "key": [1, " This ornately carved piece of bronze looks perfect for opening a lock", 0],
         'ration': [2, "This is a standard-issue ration. Not too tasty, but supplies you with the energy you need "
                       "for adventuring.", 10], 'leather armour': [3, 'A simple set of armour made from cheap hide. '
                                                                      'It does not offer much defence.', 3]}
global Inventory
# for debugging
Inventory = {0: 'test'}


class Item(object):
    # returns a randomItemKey object
    def generateItem(self):
        randomItemKey = None
        LIST = random.choice(list(category.keys()))
        type = category[LIST]
        if type == 0:
            # attempts to generate a random item until it is a weapon
            while True:
                randomItemKey = random.choice(list(items.keys()))
                name = items[randomItemKey]
                print(name[0])
                if name[0] == 0:
                    break
                else:
                    continue
        elif type == 1:
            while True:
                randomItemKey = random.choice(list(items.keys()))
                name = items[randomItemKey]
                if name[0] == 1:
                    break
                else:
                    continue
        elif type == 2:
            while True:
                randomItemKey = random.choice(list(items.keys()))
                name = items[randomItemKey]
                if name[0] == 2:
                    break
                else:
                    continue
        return randomItemKey

    def __init__(self):
        Item.generateItem(object)

class inventory(object):
    def startingInventory(self):
        Inventory = {0: items['sword'], 1: items['ration'], 2: items['leather armour']}
        return Inventory

    def saveInventory(self):
        try:
            inventory_writer = open('inventory.txt', 'w')
            count = 0
            for entries in Inventory:
                inventory_writer.write(Inventory[count])
                inventory_writer.write('\n')
                count + 1

        except IOError:
            print('Error writing to inventory.txt. Type save to try again')
        return

    def readInventory(self):
        count = 0
        inventory_load = open('inventory.txt', 'r')
        inventory_state = list(inventory_load.readlines())
        count = 0
        for line in inventory_state:
            Inventory[count]: line
            count = count + 1
        # for debugging
        print(Inventory)
        return Inventory


# for debugging
inventory.saveInventory(object)
inventory.readInventory(object)
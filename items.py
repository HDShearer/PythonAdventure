import random

# why'd you have to make it dictionaries?
category = {"weapon": 0, "key": 1, 'food': 2}

# name: [(type), "description", (stat)] ## stat is dependant on the type. A weapon (0) would have a damage stat. A
# key (1) has a stat that unlocks a lock of the corresponding value, food (2) is health restored, etc.
items = {"sword": [0, "A sharp hunk of metal, perfect for decapitating enemies!"],
         "key": [1, " This ornately carved piece of bronze looks perfect for opening a lock"],
         'ration': [2, "This is a standard-issue ration. Not too tasty, but supplies you with the energy you need "
                       "for adventuring.", 10]}


class Item(object):
    def generateItem(self):
        itemsKeysAsList = None
        LIST = random.choice(list(category.keys()))
        type = category[LIST]
        if type == 0:
            # attempts to generate a random item until it is a weapon
            while True:
                itemsKeysAsList = random.choice(list(items.keys()))
                # I used the same name for 3 different variables. This is called mental efficiency and is
                # a good trait to have.
                name = items[itemsKeysAsList]
                print(name[0])
                if name[0] == 0:
                    break
                else:
                    continue
        elif type == 1:
            while True:
                itemsKeysAsList = random.choice(list(items.keys()))
                name = items[itemsKeysAsList]
                if name[0] == 1:
                    break
                else:
                    continue
        elif type == 2:
            while True:
                itemsKeysAsList = random.choice(list(items.keys()))
                name = items[itemsKeysAsList]
                if name[0] == 2:
                    break
                else:
                    continue
        return itemsKeysAsList

    def __init__(self):
        Item.generateItem(object)


class Weapon(Item):
    pass


class Treasure(Item):
    pass


class Magic(Item):
    pass


class Other(Item):
    pass


class inventory(object):
    def readInventory(self):
        return
        Inventory = dict
        inventorySave = open('inventory.text', 'r')
        inventoryState = inventorySave.readline()
        count = list(len(inventoryState))
        for lines in inventoryState:
            Inventory[count] = str(lines)


Item.__init__(object)

# work in progress
import random as rdm
import map
import numpy as np
import pandas as pds
import rooms as rms


_MAP = map.Map.loadMap(object)

OCCUPATIONS = ['blacksmith', 'shopkeeper', 'peasant', ]

INTROSHOPKEEPER = ['Need anything?', 'I have many things to offer.']

INTROBLACKSMITH = ['You need some armour to protect against those blows, traveler.',
                   'Each blade should have a story. Pick one and give it to it, traveler!',
                   'My work is know throughout the kingdom.',
                   'Every day I do the same things over and over. Some days I look back and wonder why I want to '
                   'be here. '
                   ]

INTROGENERIC = ['Hello traveler.', "What do you want? Can't you see I'm busy?", 'Good day.',
                "I don't have anything to offer, sorry.",
                'I fear death. The end is so soon.']

NAME = [
    'Otis',
    'Mervin',
    'Vicky',
    'Chieko',
    'Magnolia',
    'Larisa',
    'Danilo',
    'Danita',
    'Florrie',
    'Justina',
    'Erwin',
    'Jarred',
    'Seth',
    'Michel',
    'Michell',
    'Taylor',
    'Reginald',
    'Velvet',
    'Karisa',
    'Clarice'
]



class generateNPCs(object):

    def generateOccupation(self):
        NOBLACKSMITH = True
        NOSHOPKEEPER = True

        my_occupation = OCCUPATIONS[rdm.randrange(0, len(OCCUPATIONS))]
        if my_occupation == 'blacksmith' and NOBLACKSMITH == True:
            NOBLACKSMITH = False
            return my_occupation
        elif my_occupation == 'blacksmith' and NOBLACKSMITH == False:
            my_occupation = 'peasant'
            return my_occupation
        elif my_occupation == 'shopkeeper' and NOSHOPKEEPER == True:
            NOSHOPKEEPER = False


NOBLACKSMITH = True
NOSHOPKEEPER = True


class generateNPCs(object):
    def generateOccupation(self, noblacksmith=NOBLACKSMITH, noshopkeeper=NOSHOPKEEPER):
        my_occupation = OCCUPATIONS[rdm.randrange(0, len(OCCUPATIONS))]
        if my_occupation == 'blacksmith' and noblacksmith == True:
            noblacksmith = False
            return my_occupation
        elif my_occupation == 'blacksmith' and noblacksmith == False:
            my_occupation = 'peasant'
        elif my_occupation == 'shopkeeper' and noshopkeeper == True:
            noshopkeeper = False
        else:
            my_occupation = 'peasant'

        return my_occupation

    def generateName(self, name=NAME):
        return name[rdm.randrange(0, len(name))]

    def generateLocation(self):
        MAP = _MAP
        MAP_X = rdm.randrange(0, len(MAP))
        MAP_Y = rdm.randrange(0, len(MAP[0]))
        MAP_XY = [MAP_X, MAP_Y]
        return MAP_XY

    def generate_number_of_npcs(self):
        return rdm.randrange(2, 5)

    def generateNPC(self):
        I = generateNPCs.generate_number_of_npcs(object)
        i = I
        count = 0

        npcOccupations = dict
        npcNames = dict
        npcLocations_X = dict
        npcLocations_Y = dict

        while not i == 0:
            npcOccupations[count]: generateNPCs.generateOccupation(object)
            npcNames[count]: generateNPCs.generateName(object)
            map_xy = generateNPCs.generateLocation(object)
            npcLocations_X[count]: int(map_xy[1])
            npcLocations_Y[count]: int(map_xy[2])
            i = i - 1
            count = count + 1
            print(i)

        npcLocations = np.meshgrid(npcLocations_X, npcLocations_Y)
        return npcNames, npcOccupations, npcLocations

    def run(self):
        return generateNPCs.generateNPC(object)

    def __init__(self):
        generateNPCs.generateNPC(object)

class run(object):
    generateNPCs.__init__(object)

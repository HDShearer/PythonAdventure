# work in progress
import random as rdm
import map
import numpy as np

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


def generateName():
    return NAME[rdm.randrange(0, len(NAME))]


def generateLocation():
    MAP = _MAP
    MAP_X = rdm.randrange(0, len(MAP))
    MAP_Y = rdm.randrange(0, len(MAP[0]))
    MAP_XY = [MAP_X, MAP_Y]
    return MAP_XY


def generate_number_of_npcs():
    return rdm.randrange(2, 6)


def generateOccupation():
    my_occupation = OCCUPATIONS[rdm.randrange(0, len(OCCUPATIONS))]
    return my_occupation


def generateNPCs():
    I = generate_number_of_npcs()
    i = I
    count = 0

    npcOccupations = {0: 0}
    npcNames = {0: 0}
    npcLocations_X = {0: 0}
    npcLocations_Y = {0: 0}

    while i >= 0:
        npcOccupations.update({count: generateOccupation()})
        npcNames.update({count: generateName()})
        map_xy = generateLocation()
        npcLocations_X.update({count: int(map_xy[0])})
        npcLocations_Y.update({count: int})
        print(npcOccupations[count])
        temp = count - 1
        while temp >= 0:
            print(temp)
            if npcOccupations[temp] == 'blacksmith' and npcOccupations[count] == 'blacksmith':
                npcOccupations[count] = 'peasant'
                print(npcOccupations[count])
            elif npcOccupations[temp] == 'shopkeeper' and npcOccupations[count] == 'shopkeeper':
                npcOccupations[count] = 'peasant'
                print(npcOccupations[count])
            temp = temp - 1

        count = count + 1
        i = i - 1

    npcLocations = np.meshgrid(npcLocations_X, npcLocations_Y)
    return npcNames, npcOccupations, npcLocations


class interact(object):
    pass

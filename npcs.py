# work in progress
import random as rdm
import  rooms as rms

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
            return my_occupation
        elif my_occupation == 'shopkeeper' and noshopkeeper == True:
            noshopkeeper = False
            return my_occupation
        else:
            my_occupation = 'peasant'
            return my_occupation

    def generateName(self, name=NAME):
        my_name = name[rdm.randrange(0, len(name))]
        return my_name

    def generateLocation(self):


    def __init__(self):
        name = generateNPCs.generateName(self, name=NAME)
        occupation = generateNPCs.generateOccupation(self, noblacksmith=NOBLACKSMITH, noshopkeeper=NOSHOPKEEPER)
        print(name)
        print(occupation)

class run(object):
    generateNPCs.__init__(object)
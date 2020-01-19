# work in progress
import random as rdm


class generateNPC(object):
    occupations = ['blacksmith', 'shopkeeper', 'peasant', ]

    introBlacksmith = ['You need some armour to protect against those blows, traveler.',
                       'Each blade should have a story. Pick one and give it to it, traveler!',
                       'My work is know throughout the kingdom.',
                       'Every day I do the same things over and over. Some days I look back and wonder why I want to be here.'
                       ]
    introGeneric = ['Hello traveler.', "What do you want? Can't you see i'm busy?", 'Good day.',
                    "I don't have anything to offer, sorry.",
                    'I fear death. The end is so soon.']
    name = (
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
    )

    def __init__(self, name=name, occupations=occupations):
        no_blacksmith = True
        no_shopkeeper = True
        my_name = name(rdm.randrange(1, len(name)))
        my_occupation = occupations[rdm.randrange(1, len(occupations))]
        if my_occupation == 'blacksmith' and no_blacksmith == True:
            no_blacksmith = False
            return
        elif my_occupation == 'blacksmith' and no_blacksmith == False:
            my_occupation = 'peasant'
        elif my_occupation == 'shopkeeper' and no_shopkeeper == True:
            return

        elif my_occupation == 'shopkeeper' and no_shopkeeper == False:
            my_occupation = 'peasant'
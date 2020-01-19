import items as I

class Room(object):
    Exits = None
    Description = None
    Name = None
    Contents = []
    Enemies = None
    PosX = 0
    PosY = 0

    def __init__(self, DefExits, DefDescription, DefName, DefContents, DefPosX, DefPosY, DefEnemies):
        self.Exits = DefExits
        self.Description = DefDescription
        self.Name = DefName
        self.Contents = DefContents
        self.PosX = DefPosX
        self.PosY = DefPosY
        self.Enemies = DefEnemies

    def generate(self):
        for i in self.Contents:
            if i in I.items:
                if "WWW" in I.category[i]:
                    pass
                elif "OOO" in I.category[i]:
                    pass
                elif "MMM" in I.category[i]:
                    pass
                elif "TTT" in I.category[i]:
                    pass


rooms = {0: "A blank room for debugging.", 1: "A not blank room for debugging", 2: "more blank rooms for debugging"}

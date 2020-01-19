descriptions = {0: "A plain grassy field", 1: "A tall stone wall. You probably won't get past this."}
name = {0: "Field", 1: "Wall"}


class Room(object):
    Exits = []
    Description = ""
    Name = ""
    Contents = []
    Enemies = []
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


rooms = {0: "A blank room for debugging.", 1: "A not blank room for debugging", 2: "more blank rooms for debugging"}

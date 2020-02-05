import numpy
import mainPlayer as Player

def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

def file_length(fname):
    with open(fname) as f:
        for i, l in enumerate(f, 1):
            pass
    return i

def line_length(fname):
    mapEnv = open("mapstate.txt", "r")
    mapLines = mapEnv.readlines()
    for line in mapLines:
        cleanedLine = line.strip()
        print(cleanedLine)
        roomList = cleanedLine.split(" ")
        roomList.pop()
        return len(roomList)

class Map(object):
    def loadMap(self):
        yL = file_length("mapstate.txt")
        xL = line_length("mapstate.txt")
        global gameMap
        gameMap = numpy.zeros((yL, xL))
        remove_newlines("mapstate.txt")
        mapEnv = open("mapstate.txt", "r")
        mapLines = mapEnv.readlines()
        i = 0
        for line in mapLines:
            cleanedLine = line.strip()
            roomList = cleanedLine.split(" ")
            roomList.pop()
            x = 0
            for room in roomList:
                gameMap[i, x] = roomList[x]
                if int(gameMap[i, x]) == 0:
                    gameMap[i, x] = "⠀"
                x = x + 1
            i = i + 1


    def generate(self):
        for row in gameMap:
            pass

    def showMap(self):
        printMap = gameMap
        printMap[Player.Player.y, Player.Player.x] = "P"
        print(printMap)
        print("The P indicates where you are.")







class DungeonMap(Map):
    randomMap = []


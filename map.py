import numpy


def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]


class Map(object):
    def loadMap(self):
        gameMap = numpy.array(
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        remove_newlines("mapstate.txt")
        mapEnv = open("mapstate.txt", "r")
        mapLines = mapEnv.readlines()
        i = 0
        for line in mapLines:
            cleanedLine = line.strip()
            #print(cleanedLine) commented out for debugging on my end
            roomList = cleanedLine.split(" ")
            roomList.pop()
            #print(roomList)
            x = 0
            for room in roomList:
                #print(roomList[x])
                gameMap[i, x] = roomList[x]
                x = x + 1
            i = i + 1
        #print(gameMap)
        return gameMap

    def __init__(self):
        Map.loadMap(object)


class DungeonMap(Map):
    randomMap = []

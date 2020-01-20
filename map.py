import numpy


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
    def __init__(self):
        yL = file_length("mapstate.txt")
        xL = line_length("mapstate.txt")
        gameMap = numpy.zeros((yL, xL))
        remove_newlines("mapstate.txt")
        mapEnv = open("mapstate.txt", "r")
        mapLines = mapEnv.readlines()
        i = 0
        for line in mapLines:
            cleanedLine = line.strip()
            print(cleanedLine)
            roomList = cleanedLine.split(" ")
            roomList.pop()
            print(roomList)
            x = 0
            for room in roomList:
                print(roomList[x])
                gameMap[i, x] = roomList[x]
                x = x + 1
            i = i + 1
        print(gameMap)

    #def generate(self):
     #   for row in gameMap:
      #      pass



class DungeonMap(Map):
    randomMap = []


map = Map()

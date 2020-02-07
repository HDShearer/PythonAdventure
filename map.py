import numpy

import __main__ as main
import mainPlayer as Player

global gameMap


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
        gameMap = numpy.array(
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        yL = file_length("mapstate.txt")
        xL = line_length("mapstate.txt")
        gameMap = numpy.zeros((yL, xL))
        remove_newlines("mapstate.txt")
        mapEnv = open("mapstate.txt", "r")
        mapLines = mapEnv.readlines()
        i = 0
        for line in mapLines:
            cleanedLine = line.strip()
            # print(cleanedLine) commented out for debugging on my end
            roomList = cleanedLine.split(" ")
            roomList.pop()
            # print(roomList)
            x = 0
            for room in roomList:
                gameMap[i, x] = roomList[x]
                if int(gameMap[i, x]) == 0:
                    gameMap[i, x] = "⠀"
                x = x + 1
            i = i + 1

    # def generate(self):
    #   for row in gameMap:
    #      pass
    @staticmethod
    def showMap():

        printMap = gameMap
        printMap[Player.Player.y, Player.Player.x] = "P"
        print(printMap)
        main.Ui_MainWindow.Output = printMap
        main.Ui_MainWindow.tb.append(main.Ui_MainWindow.Output)
        main.Ui_MainWindow.lineEdit.clear()


class DungeonMap(Map):
    randomMap = []

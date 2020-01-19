import numpy
import random as R


def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

class Map(object):
    def __init__(self):
        gameMap = numpy.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        remove_newlines("mapstate.txt")
        mapEnv = open("mapstate.txt", "r")
        mapLines = mapEnv.readlines()
        for line in mapLines:
            roomList = line.split(" ")
            for room in roomList:
                liner = int(line)
                except ValueError:
                number = int(room)
                gameMap[liner, number] = number
        print(gameMap)
        print("darn")


class DungeonMap(Map):
    randomMap = []


map = Map()

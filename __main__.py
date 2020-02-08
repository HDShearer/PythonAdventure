import os
import random as r
from map import *
import rooms as rms
from PyQt5 import QtCore, QtGui, QtWidgets
from colorama import Fore, Style
import mainPlayer as P

# print(Style.RESET_ALL)

# Define all variables, lists, etc

actions = {"look": "Look", "go": "Go", "clear": "Clear", "help": "Help", "attack": "Attack", "map": "Map"}

global currentPlayer
global Output
PlayerNotDead = True
EnemyNotDead = True
turn = 0
gameQuit = False
attack = True


class Game:
    @staticmethod
    def __init__():
        pass

    @staticmethod
    def clearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def UpdateGame():
        pass

    @staticmethod
    def Help():
        print("\n")
        for action in actions:
            currentAction = actions[action]
            print(Fore.RED + currentAction)
        print("\n")
        print(Fore.RED + "Red text designates errors or help commands")
        print(Fore.CYAN + "Cyan text designates meta information, such as menus and game setup.")
        print(Fore.GREEN + "Green text designates information about something you see.")
        print(Fore.YELLOW + "Yellow text designates combat actions")
        print(Fore.BLUE + "Blue text designates conversations with NPCs.")
        print(Fore.MAGENTA + "Purple text designates all other player actions.")
        print(Style.RESET_ALL + "Plain text designates commands you enter.")
        print(Style.RESET_ALL)

    @staticmethod
    def RandomEncounter(Monster):
        # add individual monster noises)
        EnemyRoll = r.randint(0, 20)
        PlayerRoll = r.randint(0, 20)
        if EnemyRoll > PlayerRoll:
            pass
        else:
            pass

    @staticmethod
    def initiate():
        global map
        Game.clearScreen()
        ui.setupGame(Ui_MainWindow)
        P.Player.inv.clear()
        map = Map()

    @staticmethod
    def MainLoop():
        Game.UpdateGame()
        # Ui_MainWindow.TakeInput()

    @staticmethod
    def GetLoot(Monster, DC):
        DC = int(DC)
        if DC % 2 == 0:
            lowBound = int(DC / 2)
        else:
            lowBound = int((DC + 1) / 2)
            lootCheck = r.randint(lowBound, DC)
        if lootCheck == 1:
            print(f"The {Monster} had nothing.")
            P.Player.inv.append(None)
        else:
            pass


class Ui_MainWindow(object):
    global Output
    global tb
    global lineEdit

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1206, 707)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 642, 750, 22))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 750, 620))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1206, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Game = QtWidgets.QAction(MainWindow)
        self.actionSave_Game.setObjectName("actionSave_Game")
        self.actionLoad_Game = QtWidgets.QAction(MainWindow)
        self.actionLoad_Game.setObjectName("actionLoad_Game")
        self.actionEnter_current_command = QtWidgets.QAction(MainWindow)
        self.actionEnter_current_command.setObjectName("actionEnter_current_command")
        self.menuFile.addAction(self.actionSave_Game)
        self.menuFile.addAction(self.actionLoad_Game)
        self.menuFile.addSeparator()
        self.menuEdit.addAction(self.actionEnter_current_command)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionEnter_current_command.triggered.connect(lambda: self.appendTB(self.lineEdit.text()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Type Here"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionSave_Game.setText(_translate("MainWindow", "Save Game"))
        self.actionSave_Game.setToolTip(_translate("MainWindow", "Save Game"))
        self.actionSave_Game.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionLoad_Game.setText(_translate("MainWindow", "Load Game"))
        self.actionEnter_current_command.setText(_translate("MainWindow", "Enter current command"))
        self.actionEnter_current_command.setShortcut(_translate("MainWindow", "Return"))

    def appendTB(self, text):
        tb = self.textBrowser
        print(self.textBrowser.length())
        self.playerLastInput = text
        x = self.playerLastInput
        x = x.lower()
        args = x.split(' ')
        length = len(args)
        Output = []
        if args[0] in actions:
            if args[0] == "look":
                P.Player.Look(currentPlayer, args[length - 1])
                Output = str(rms.descriptions[length - 1])
            #elif args[0] == "clear":
                #Game.clearScreen()
            #elif args[0] == "help":
                #Game.Help()
            elif args[0] == "attack":
                attackEnemy = P.Player.Attack(currentPlayer, args[length - 1])
                Output.append(attackEnemy)
        else:
            Output = "I don't know what you mean"
        if type(Output) == list:
            tb.append('Game: ' + str(Output[0]))
        else:
            tb.append('Game: ' + str(Output))
        self.lineEdit.clear()

    def setupGame(self):
        global currentPlayer
        P.Name = input(Fore.CYAN + "What is your name, Hero? > ")
        Race = input("Are you an elf, dwarf, or human? > ")
        Race = str(Race.lower())
        if Race == "elf":
            P.Race = "Elf"
        elif Race == "dwarf":
            P.Race = "Dwarf"
        elif Race == "human":
            P.Race = "Human"
        else:
            print("What?")
            Game.setupGame()
        Class = ""
        Class = input("Are you a rogue or a monk? > ")
        print(Style.RESET_ALL)
        Class = str(Class.lower())
        if Race == "human":
            if Class == "rogue":
                currentPlayer = P.Rogue()
            elif Class == "monk":
                currentPlayer = P.Monk()
            else:
                pass
        elif Race == "elf":
            Class = input("Are you a ranger or a mage? > ")
            print(Style.RESET_ALL)
            Class = str(Class.lower())
            if Class == "ranger":
                currentPlayer = P.Ranger()
            elif Class == "mage":
                currentPlayer = P.Mage()
            else:
                print("What?")
                Ui_MainWindow.setupGame()
        elif Race == "dwarf":
            Class = input("Are you a cleric or a barbarian? > ")
            print(Style.RESET_ALL)
            Class = str(Class.lower())
            if Class == "cleric":
                currentPlayer = P.Cleric()
            elif Class == "barbarian":
                currentPlayer = P.Barbarian()
        else:
            tb.append('Game: ' + "What?")
            self.lineEdit.clear()
            Ui_MainWindow.setupGame()
        print(f"Rise {P.Player.Name} the {Race} {Class}. The kingdom needs you!")

# run game
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

Game.initiate()

while gameQuit == False:
    Game.MainLoop()

#import maya.cmds as mc
from PySide2 import QtCore
from PySide2 import QtWidgets



class RigWin(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(RigWin, self).__init__(parent)
        self.button_one = QtWidgets.QPushButton("Push Me")

        self.layout()




if __name__ == "__main__": # this is when your program start
    d = RigWin()
    d.show()

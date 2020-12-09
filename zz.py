# Do not declare more than what you plan to use
from sys import exit  as sysExit

# from PyQt5.QtCore    import *
# from PyQt5.QtGui     import *
# QWidgets Container Objects
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
# QWidgets Action Objects
from PyQt5.QtWidgets import QPushButton


# The 2nd Little Window to Demonstrate. Now since this is a
# Class it could be another QMainWindow object that does a lot
# of things or be as simplistic as this one - further we could
# import this from outside rather than have it contained within
class NewWindow(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.Parent = parent
        self.Name = 'Child'
        self.setWindowTitle(self.Name)
        self.setGeometry(600, 100, 150, 150)

        self.btnQuit = QPushButton('Quit')
        self.btnQuit.clicked.connect(self.QuitGUI)

        HBox = QHBoxLayout()
        HBox.addWidget(self.btnQuit)
        HBox.addStretch(1)

        VBox = QVBoxLayout()
        VBox.addLayout(HBox)
        VBox.addStretch(1)

        self.setLayout(VBox)

    def QuitGUI(self):
        self.Parent.WindOpen = False
        self.close()


class CentralPanel(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.Parent = parent
        self.Toggle = True

        btnShow = QPushButton('Show', self)
        btnShow.clicked.connect(self.Parent.OpenWindow)

        HBox = QHBoxLayout()
        # HBox.addWidget(self.btnShow)
        HBox.addStretch(1)

        VBox = QVBoxLayout()
        VBox.addLayout(HBox)
        VBox.addStretch(1)

        self.setLayout(VBox)


# Note one does not need a QMainWindow to render the first Window
# I have created windows by just delcaring and showing a QPushButton
# However if using a QMainWindow then the Center Panel out to be
# classed as shown and a minimalistic approach applied to the MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.WindOpen = False

        # self.setMinimumSize(QSize(300, 200))
        self.setWindowTitle("Main")

        left = 150;
        top = 150;
        width = 400;
        height = 300
        self.setGeometry(left, top, width, height)

        self.CenterPane = CentralPanel(self)
        self.setCentralWidget(self.CenterPane)

    def OpenWindow(self):
        # This is used to avoid accidentally opening the
        # window twice as that could cause issues unless
        # handled properly -- aka you could open more than
        # one instances of this 2ndary window if you wanted
        # but certain things would need to be done to handled
        # that to keep from breaking the program
        if not self.WindOpen:
            self.WindOpen = True
            # Instantiate the 2nd Window Class
            self.NewWind = NewWindow(self)
            # Now Show it
            self.NewWind.show()


if __name__ == '__main__':
    MainThred = QApplication([])

    MainGui = MainWindow()
    MainGui.show()

    sysExit(MainThred.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monty_hall.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random

#Generate UI class from PyQt designer

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.entry = QtWidgets.QLineEdit(self.centralwidget)
        self.entry.setGeometry(QtCore.QRect(130, 140, 241, 41))
        self.entry.setObjectName("entry")
        self.Btn = QtWidgets.QPushButton(self.centralwidget)
        self.Btn.setGeometry(QtCore.QRect(190, 210, 93, 28))
        self.Btn.setObjectName("Btn")
        self.Output = QtWidgets.QLabel(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(60, 90, 391, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Output.setFont(font)
        self.Output.setAlignment(QtCore.Qt.AlignCenter)
        self.Output.setObjectName("Output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Btn.clicked.connect(self.Monty_Hall)
        self.entry.returnPressed.connect(self.Monty_Hall)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn.setText(_translate("MainWindow", "Send"))
        self.Output.setText(_translate("MainWindow", "Which door would you like to pick? 1-3"))


    def Monty_Hall(self):

        listOfPrize = ["Goat", "Goat", "Car"]
        random.shuffle(listOfPrize)

        # def user_selection
        userInput = self.entry.text()
        try:
            userInput = int(userInput)

        except ValueError:
            self.Output.setText("Your input need to be numeric")

        else:
            if userInput not in range(1, 4):
                self.Output.setText("Your choice need to be between 1-3 inclusive")

            else:
                self.Output.setText(f"You chose door number {userInput}")
                userDoorIndex = userInput - 1
                print(userDoorIndex)
                i = 0

                for i in range(3):
                    if listOfPrize[i] != 'Car' and i != userDoorIndex:
                        firstDoorIndex = i

            self.Output.setText(f"Let's open door {firstDoorIndex + 1}")
            self.Output.setText(f"There is... {listOfPrize[i]}")

             # def SwitchDoor
            self.Output.setText("Would you like to switch the door? y/n")
            lastChoice = self.entry.text().lower()
            if lastChoice == 'n':
                self.Output.setText(f"Let's open Door {userInput}")
                self.Output.setText(f"The door left has...{listOfPrize[userDoorIndex]}")

            elif lastChoice == 'y':
                del listOfPrize[firstDoorIndex]

                del listOfPrize[userDoorIndex]
                self.Output.setText(f"The door left has...{listOfPrize}")

            else:
                self.Output.setText("Your input should be y or n")

        if (listOfPrize[userDoorIndex] == "Car"):
            self.Output.setText("Congrats! You won!")

        else:
            self.Output.setText("You lose...")







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

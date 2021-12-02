from PyQt5 import QtCore, QtGui, QtWidgets
import random

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

        ''''#Hookup btn
        self.Btn.clicked(self.play_monty_hall)
        self.entry.returnPressed.connect(self.play_monty_hall)'''

        self.Btn.clicked((self.test))
        self.entry.returnPressed().connect(self.test)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn.setText(_translate("MainWindow", "Send"))
        self.Output.setText(_translate("MainWindow", "Which door would you like to pick? 1-3"))

    def test(self):

        self.Output.Text('It is test')

    '''def play_monty_hall(self):

        self.Output.Text("Hello")

        choice = self.entry.text()
        choice = int(choice)

        prizes = ['Goat', 'Car', 'Goat']

        random.shuffle(prizes)

        while True:
            opening_door = random.randint(len(prizes))
            if prizes[opening_door] != 'Car' and choice-1 != opening_door:
                break

        opening_door = opening_door + 1
        self.Output.setText('We are opening the door number -%d' %(opening_door))

        options = [1, 2, 3]
        options.remove(choice)
        options.remove(opening_door)
        switching_door = options[0]

        self.Output.setText('Now do you want to switch to door number-%d? (yes/no)' %(switching_door))
        answer = self.entry.text()
        if answer == 'yes':
            result = switching_door - 1
        else:
            result = choice - 1

        self.Output.setText('And your prize is... ', prizes[result].upper()'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

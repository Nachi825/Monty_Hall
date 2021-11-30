import random
import sys
from PyQt5.QtWidgets import QListWidget, QLineEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

'''def GUI():
    #Create window
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()

    btn = QtWidgets.QPushButton(windowExample)

    btn.setText('Guess')
    btn.move(100, 50)

    windowExample.setGeometry(0, 0, 400, 400)
    windowExample.setWindowTitle('Monty Hall Game')
    windowExample.show()
    sys.exit(app.exec_())

    #Create texbox'''



def main():

    #def assignPrize
    listOfPrize = ["Goat", "Goat", "Car"]
    random.shuffle(listOfPrize)
    #print(listOfPrize)

    #def user_selection
    while True:
        try:
            firstChoice = int(input(("Which door would you like to pick? 1-3")))

        except ValueError:
            print("Your input need to be numeric")

        else:
            if firstChoice not in range(1, 4):
                print("Your choice need to be between 1-3 inclusive")

            else:
                print(f"You chose door number {firstChoice}")
                userDoorIndex = firstChoice - 1

                #def OpenADoor
                i = 0
                while True:
                    while (i < len(listOfPrize)):
                        if listOfPrize[i] != 'Car' and i != userDoorIndex:
                                firstDoorIndex = i
                                break
                        else:
                            i += 1

                    print(f"Let's open door {firstDoorIndex + 1}")
                    print(f"There is... {listOfPrize[i]}")

                    #def SwitchDoor
                    lastChoice = input("Would you like to switch the door? y/n").lower()
                    if lastChoice == 'n':
                        print(f"Let's open Door {firstChoice}")
                        print(f"The door left has...{listOfPrize[userDoorIndex]}")
                        break

                    elif lastChoice == 'y':

                        del listOfPrize[firstDoorIndex]

                        del listOfPrize[userDoorIndex]
                        print(f"The door left has...{listOfPrize}")
                        break

                    else:
                        print("Your input should be y or n")

                if (listOfPrize[userDoorIndex] == "Car"):
                    print("Congrats! You won!")
                else:
                    print("You lose...")
                break




if __name__ == '__main__':
    GUI()
    main()
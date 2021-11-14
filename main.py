"""import random ttyl



class Monty_Hall():

    def assignPrize(self):

        listOfPrize = ["Goat", "Goat", "Car"]
        random.shuffle(listOfPrize)
        print(listOfPrize)

    def door_selection(self):

        while True:
            try:
                print()
                user_selection = int(input(("Which door would you like to pick? 1-3")))

            except ValueError:
                print("Your input need to be numeric")

            else:
                if user_selection not in range(1, 4):
                    print("Your choice need to be between 1-3 inclusive")

                else:
                    print(f"You choose door number {user_selection}")


    def behindTheDoor(self, user_selection, listOfPrize):
        userDoor = listOfPrize[user_selection-1]
        return userDoor

    def main(self):
        pass


if __name__ == '__main__':
    game = Monty_Hall()
    game.assignPrize()
    game.door_selection()
""" #game.behindTheDoor()

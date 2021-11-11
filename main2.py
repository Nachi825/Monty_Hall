import random

def main():

    #def assignPrize
    listOfPrize = ["Goat", "Goat", "Car"]
    random.shuffle(listOfPrize)
    print(listOfPrize)

    #def user_selection
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
            userDoor = listOfPrize[user_selection - 1]

            #def OpenADoor
            #Open a door which has "Goat" && not userDoor

            i = 0
            while i < len(listOfPrize):
                #print(i)
                #print(listOfPrize[i])
                i = i+1

                if listOfPrize[i] == "Goat"
                    print(f"index num is {i}")
                    print(f"Let's open door  {i+1}")
                    print(listOfPrize[i])
                    break





if __name__ == '__main__':
    main()
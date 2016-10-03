import random as rnd

bailout = False
room = 1
print('Welcome to Zork\'s Haunted House')



while not bailout:
    #print("Room is " + str(room))
    #print("bailout is " + str(bailout))

    # You are in the foyer
    if room == 1:
        print ("You are standing in the foyer of an old house.")
        print ("You see a dead scorpion.")
        print("You can (1) exit to the north, (2) run.")

        ans = int(input("What do you want to do? "))
        print(ans)
        
        if ans == 1:
            room = 2
        elif ans == 2:
            bailout = True

    # You are in the front room
    elif room == 2:
        print("You are standing in the front room.")
        print("You see a piano.")
        print("You can (1) exit to the south, (2) exit to the east, (3) exit to the west, (4) run. ")

        ans = int(input("What do you want to do? "))

        if ans == 1:
            room = 1
        elif ans == 2:
            room = 4
        elif ans == 3:
            room = 3
        elif ans == 4:
            bailout = True

    # You are in the library
    elif room == 3:
        print("You are standing in the library.")
        print("You see spiders.")
        print("You can (1) exit to the east, (2) exit to the north, (3) run. ")

        ans = int(input("What do you want to do? "))

        if ans == 1:
            room = 2
        elif ans == 2:
            room = 7
        elif ans == 3:
            bailout = True
    # You are in the kitchen
    elif room == 4:
        print("You are standing in the kitchen.")
        print("You see bats.")
        print("You can (1) exit to the east, (2) exit to the north, (3) run. ")

        ans = int(input("What do you want to do? "))

        if ans == 1:
            room = 2
        elif ans == 2:
            room = 5
        elif ans == 3:
            bailout = True

    # You are in the dining room
    elif room == 5:
        print("You are standing in the dining room.")
        print("You see a dust and empty box.")
        print("You can (1) exit to the south, (2) run. ")

        ans = int(input("What do you want to do? "))

        if ans == 1:
            room = 4
        elif ans == 2:
            bailout = True

    # You are in the vault
    elif room == 6:
        print("You are standing in the vault.")
        print("You see a three walking skeletons.")
        print("You can (1) exit to the west, (2) run. ")

        ans = int(input("What do you want to do? "))
        
        if ans == 1:
            room = 7
        elif ans == 2:
            bailout = True

    # You are in the parlor
    elif room == 7:
        print("You are standing in the parlor.")
        print("You see a treasure chest.")
        print("You can (1) exit to the east, (2) exit to the south, (3) run. ")

        ans = int(input("What do you want to do? "))

    if input == 1:
        room = 6
    elif input == 2:
        room = 3
    elif input == 3:
        bailout = True

print("You have exited the house. But you are not alone. ")

fate = rnd.randint(1, 4)
if fate == 1:
    print("Something is crawling up your leg.")
else:
    print("Or are you? . . .")



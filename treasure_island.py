print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road = input("You come to a fork in the road. Do you go left (L) or right(R)? \n").lower()
if road == "l":
    lake = input("You come to a lake. Do you swims (S) or wait (W)?\n").lower()
    if lake == "w":
        door = input("Once you get to the other side, you see 3 doors. Do you choose Red(R), "
                     "Blue(B) or Yellow(Y)?\n").lower()
        if door == "y":
            print("YOU WIN!")
        elif door == "b":
            print("Wrong Choice Amigo, you lose!")
        elif door == "r":
            print("No way dude, you lose!")
        else:
            print("You chose a door that doesn't exist. GAME OVER")

            print("YOU LOSE!")
    else:
        print("YOU LOSE")
else:
    print("YOU LOSE")

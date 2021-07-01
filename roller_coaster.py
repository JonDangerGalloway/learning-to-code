print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? \n"))

total = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? \n"))
    if age < 12:
        total += 5
        print("Child Tickets are $5")
    elif age <= 18:
        total += 7
        print("Youth Tickets are $7")
    elif age >= 45 and age <= 55:
        print("Hang in there, your ticket is on the house")
    else:
        total += 12
        print("Adult Tickets are $12")

    pic = input("Would you like a photo? y or n\n")

    if pic == "y":
        total += 3

    print(f"Your total is ${total}")

else:
    print("Sorry, you have to grow taller before you can ride.")
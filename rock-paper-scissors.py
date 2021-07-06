import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



userSelect = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))


choices = [0, 1, 2]
computerSelect = random.choice(choices)
#computer_choice = random.randint(0,2)
if userSelect >= 3 or userSelect < 0:
    print("Invalid entry, you lose!")


if userSelect == 0:
    print(rock)
    if computerSelect == 0:
        print(f"Computer Chose:\n{rock}\n Tie Game")
    elif computerSelect == 1:
        print(f"Computer Chose:\n{paper}\nYou Lose")
    elif computerSelect == 2:
        print(f"Computer Chose:\n{scissors}\nYou Win")

if userSelect == 1:
    print(paper)
    if computerSelect == 0:
        print(f"Computer Chose:\n{rock}\nYou Win")
    elif computerSelect == 1:
        print(f"Computer Chose:\n{paper}\nTie Game")
    elif computerSelect == 2:
        print(f"Computer Chose:\n{scissors}\nYou Lose")


if userSelect == 2:
    print(scissors)
    if computerSelect == 0:
        print(f"Computer Chose:\n{rock}\nYou Lose")
    elif computerSelect == 1:
        print(f"Computer Chose:\n{paper}\nYou Win")
    elif computerSelect == 2:
        print(f"Computer Chose:\n{scissors}\nTie Game")
import random
# from replit import clear
from game_data import data
from art import logo, vs
print(logo)
def select_options(choice_a, choice_b):
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
    print(vs)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
def compare(a_followers, b_followers, guess):
    if guess == "a":
        guess = a_followers
    else:
        guess = b_followers
    followers = [a_followers, b_followers]
    high_followers = 0
    for number in followers:
        if number > high_followers:
            high_followers = number
    if guess == high_followers:
        return "right"
    else:
        return "wrong"
score = 0
choice_a = random.choice(data)
play = True
while play:
    choice_b = random.choice(data)
    a_followers = (choice_a["follower_count"])
    b_followers = (choice_b["follower_count"])
    select_options(choice_a, choice_b)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    result = compare(a_followers, b_followers, guess)
    if result == "right":
        score += 1
        choice_a = choice_b
        # clear()
        print(logo)
        print(f"You're right! Current score: {score}!")
    else:
        play = False
        # clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")





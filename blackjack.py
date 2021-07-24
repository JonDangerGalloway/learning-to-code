import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    score = sum(cards)
    if len(cards) == 2 and score == 21:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "YOU LOSE, OPPONENT HAS BLACKJACK"
    elif user_score == 0:
        return "YOU WIN WITH A BLACKJACK"
    elif user_score > 21:
        return "YOU WENT OVER, YOU LOSE"
    elif computer_score > 21:
        return "COMPUTER WENT OVER, YOU WIN!"
    elif user_score > computer_score:
        return"YOU WIN"
    else:
        return "YOU LOSE"

def game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computers first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_another_card = input("Type 'y' to get another card, type 'n' to pass: " ).lower()
            if user_another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, your final score: {user_score}")
    print(f"Computers final hand n: {computer_cards}, computer final score: {computer_score}")
    print(compare(user_score, computer_score))

    while input(f"Would you like to play another game? Y or N? ").lower() == "y":
        game()

game()
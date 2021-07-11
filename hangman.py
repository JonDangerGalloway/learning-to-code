import random
import hangman_art
import hangman_words


chosen_word = random.choice(hangman_words.word_list)
display = []
word = len(chosen_word)
lives = 6
print(hangman_art.logo)

for _ in chosen_word:
    display += "_"
print(display)

end_of_game = False
while not end_of_game:

    guess = input("Guess a letter: \n").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE!")
            print(chosen_word)

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")


    print(hangman_art.stages[lives])
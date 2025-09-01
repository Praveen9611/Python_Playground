import random
import hangman_word_list
from hangmanlogo import logo
from hangman_art import hangman_art

print(logo)
lives = 6

word = random.choice(hangman_word_list.word_list)
# print(word)  # Debug only

placeholder = "_" * len(word)
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    letter = input("Guess a letter: ").lower()

    if letter in correct_letters:
        print(f"You already guessed '{letter}'!")
        continue

    display = ""
    for char in word:
        if letter == char:
            display += letter
            correct_letters.append(letter)
        elif char in correct_letters:
            display += char
        else:
            display += "_"

    print(display)

    if letter not in word:
        lives -= 1
        print(f"'{letter}' is not in the word. You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print(f"You lose. The word was '{word}'.")

    if "_" not in display:
        game_over = True
        print("You WIN 🎉")

    print(hangman_art[lives])

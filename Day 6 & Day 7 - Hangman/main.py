import random
import hangman_words.py
import hangman_art.py
#Step 1 



# word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(hangman_words.word_list)

chances = 6

print(hangman_art.logo)

print(f"Testing: {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"




end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        

    print(display)

    if guess not in chosen_word:
        print("Wrong guess!")
        chances = chances - 1
        if chances == 0:
            end_of_game = True
            print("Hanged. GAME OVER")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(hangman_art.stages[chances])
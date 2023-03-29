#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

def guess(mode):
    Number_To_Guess = random.randint(1, 100)
    print(f"Number guess is {Number_To_Guess}")
    guesses = 0
    if mode == "easy":
        n = 10
        while guesses < 10:
            guess = int(input("Make a guess: "))
            if guess == Number_To_Guess:
                print(f"You got it! The number was {Number_To_Guess}")
                break
            else:
                if guess > Number_To_Guess:
                    n = n - 1
                    print(f"Too High. \nTry Again. \nNumber of Attempts left: {n}")
                else:
                    n = n - 1
                    print(f"Too Low. \nTry Again. \nNumber of Attempts left: {n}")
                guesses += 1
        else:
            print("You have exhausted the number of attempts. Game Over.")
    elif mode == "hard":
        n = 5
        while guesses < 5:
            guess = int(input("Make a guess: "))
            if guess == Number_To_Guess:
                print(f"You got it! The number was {Number_To_Guess}")
                break
            else:
                if guess > Number_To_Guess:
                    n = n - 1
                    print(f"Too High. \nTry Again. \nNumber of Attempts left: {n}")
                else:
                    n = n - 1
                    print(f"Too Low. \nTry Again. \nNumber of Attempts left: {n}")
                guesses += 1
        else:
            print("You have exhausted the number of attempts. Game Over.")

print("""
  ____  __ __    ___  _____ _____     ______  __ __    ___      ____   __ __  ___ ___  ____     ___  ____  
 /    ||  |  |  /  _]/ ___// ___/    |      ||  |  |  /  _]    |    \ |  |  ||   |   ||    \   /  _]|    \ 
|   __||  |  | /  [_(   \_(   \_     |      ||  |  | /  [_     |  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )
|  |  ||  |  ||    _]\__  |\__  |    |_|  |_||  _  ||    _]    |  |  ||  |  ||  \_/  ||     ||    _]|    / 
|  |_ ||  :  ||   [_ /  \ |/  \ |      |  |  |  |  ||   [_     |  |  ||  :  ||   |   ||  O  ||   [_ |    \ 
|     ||     ||     |\    |\    |      |  |  |  |  ||     |    |  |  ||     ||   |   ||     ||     ||  .  \
|___,_| \__,_||_____| \___| \___|      |__|  |__|__||_____|    |__|__| \__,_||___|___||_____||_____||__|\_|
                                                                                                           
""")
print("Welcome to the Number Guessing Game")
print("I'm Thinking of a number between 1-100")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
guess(mode)
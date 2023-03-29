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

#Write your code below this line 👇

game_images = [rock, paper, scissors]

userc = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[userc])

compc = random.randint(0, 2)
print("Computer chose:")
print(game_images[compc])

if userc >= 3 or userc < 0: 
  print("You typed an invalid number, you lose!") 
elif userc == 0 and compc == 2:
  print("You win!")
elif compc == 0 and userc == 2:
  print("You lose")
elif compc > userc:
  print("You lose")
elif userc > compc:
  print("You win!")
elif compc == userc:
  print("It's a draw")
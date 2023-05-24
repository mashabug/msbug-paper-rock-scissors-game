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


import random

game_pics = [rock, paper, scissors]
print("Welcome to Rock, Paper, Scissors Game.")
you = int(input("What would you choose?\nPress 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if you >= 3 or you < 0:
  print("You typed invalid number. You loose.")
else:
  print(game_pics[you])

  computer = random.randint(0, 2)
  print(f"Computer choise:\n{game_pics[computer]}")

  if computer == 0 and you == 2:
    print("You loose.")
  elif you == 0 and computer == 2:
      print("You win.")
  elif computer > you:
    print("You loose.")
  elif you > computer:
    print("You win.")
  else:
      print("You have a draw. Play gain.")

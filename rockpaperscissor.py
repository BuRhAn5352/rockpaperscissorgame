import random

# ASCII art for the choices
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List of choices and their corresponding ASCII art
choices = [rock, paper, scissor] #stores the string of this data
symbol = ["rock", "paper", "scissors"] #stores textual representation

# Get user's choice
gamer = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))

# Check if the user's input is valid
if gamer < 0 or gamer > 2:
    print("You typed an invalid number, you lose!")
else:
    # Display the user's choice with ASCII art
    print(f"You chose: {symbol[gamer]}")
    print(choices[gamer])

    # Randomly select computer's choice
    computerselection = random.randint(0, 2)
    print(f"Computer chose: {symbol[computerselection]}")
    print(choices[computerselection])

    # Determine the winner
    if gamer == computerselection:
        print("It's a draw!")
    elif (gamer == 0 and computerselection == 2) or (gamer == 1 and computerselection == 0) or (gamer == 2 and computerselection == 1):
        print("You win!")
    else:
        print("Computer wins!")

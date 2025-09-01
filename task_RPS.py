import random
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
rps_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors \n"))
if user_choice < 0 or user_choice > 2:
    print("Invalid input! Please choose 0, 1, or 2.")
else:
    print(rps_list[user_choice])
    computer_choice = random.randint(0,2)
    print(f"computer chose {computer_choice}")
    print(rps_list[computer_choice])
    if user_choice == computer_choice:
        print("It's a DRAW")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You WIN!")
    else:
        print("Computer WINS!")

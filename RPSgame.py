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
print(rps_list[user_choice])
computer_choice = random.randint(0,2)
print(f"computer chose {computer_choice}")
print(rps_list[computer_choice])

if(user_choice>=3 or user_choice<0):
    print("Enter valid input")
elif (user_choice == 0 and computer_choice==2):
    print("Rock! You Won")
elif(user_choice == 2 and computer_choice == 0):
    print("Rock!" "Computer Wins")
if (user_choice == 0 and computer_choice==1):
    print("Paper!" "Computer Wins")
elif (user_choice == 1  and computer_choice == 0):
    print("Paper!" "You Won")
if (user_choice == 1 and computer_choice==2):
    print("Scissors" "Computer Wins")
elif (user_choice == 2 and computer_choice == 1):
    print("Scissors" "You Won")
elif (user_choice == computer_choice):
    print("DRAW")

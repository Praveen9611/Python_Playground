print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
cross_road = input('You\'re at a cross road. Where do you want to go? Type "left" or "right "').lower()
if (cross_road == "left"):
    swim_across = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across ")
    if (swim_across == "wait"):
        choose_doors = input("choose red, blue or yellow ")
        if (choose_doors == 'yellow'):
            print("You won")
else:
    print("game over")
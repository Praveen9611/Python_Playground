print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want! S, M or L; ")
if (size == "S"):
    bill = 100
elif (size == "M"):
    bill = 200
elif (size == "L"):
    bill = 300
else:
    print("ERROR! please give correct input")
pepporoni = input("Do you want pepperoni on your pizza? Y or N: ")
if (pepporoni == "Y"):
    bill += 50
elif (pepporoni == "M"):
    bill += 0
extra_cheese = input("Do you want extra cheese? Y or N: ")
if (extra_cheese == "Y"):
    bill += 20
elif (extra_cheese == "N"):
    bill += 0
print(f'YOUR FINAL BILL IS: {bill}.')
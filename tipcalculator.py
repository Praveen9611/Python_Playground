print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? ₹"))
tip = int(input("How much tip would you like to give? 10, 20, or 15 "))
split = int(input("How many people to split the bill?" ))
tip_as_percent = bill * (tip/100)
total_bill = bill + tip_as_percent
each_person = total_bill/ split
print(f"Each person should pay :₹{each_person} ")
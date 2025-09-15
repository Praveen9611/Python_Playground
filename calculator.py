from calculatorlogo import cal_logo
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calculator():
    print(cal_logo)
    should_accumulate = True
    key_value = {"+": add, "-": sub, "*": mul, "/": div}
    
    first_number = int(input("Enter first number: "))
    
    while should_accumulate:
        choice = input("Choose one operation '+', '-', '*', '/': ")
        second_number = int(input("Enter second number: "))
        
        result = key_value[choice](first_number, second_number)
        print(f"Result: {result}")
        
        repeat = input(f"Type 'y' to continue calculating with {result}, or 'n' to exit: ")
        
        if repeat == 'y':
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 5)
            calculator()

calculator()

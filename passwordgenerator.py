import random
letter = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
number = [0,1,2,3,4,5,6,7,8,9]

symbols = [
    '!','@','#','$','%','^','&','*','(',')',
    '-','_','=','+','[',']','{','}',';',':',
    '"',"'",'<','>',',','.','?','/','|','\\'
]
password = []
print("Welcome to th e PyPassword Generator!")
nf_letters = int(input("How many letters would you like in your password?\n"))
for i in range(nf_letters):
    password.append(random.choice(letter))
nf_symbols = int(input("How many symbols would you like?\n"))
for j in range(nf_symbols):
    password.append(random.choice(symbols))

nf_numbers = int(input("How many numbers would you like?\n"))
for k in range(nf_numbers):
    password.append(str(random.choice(number)))
random.shuffle(password)
pygenerator = "".join(password)
print(f"Your generated password is : {pygenerator}")
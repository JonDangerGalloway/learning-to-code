import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# EASY WAY

password = ""

for letter in range(0, nr_letters):
    randletters = (random.choice(letters))
    password = password + randletters

for symbol in range(0, nr_symbols):
    randsymbols = random.choice(symbols)
    password = password + randsymbols

for number in range(0, nr_numbers):
    randnumbers = random.choice(numbers)
    password = password + randnumbers

print(password)

# HARD WAY

passwordList = []

for letter in range(0, nr_letters):
    passwordList.append(random.choice(letters))


for symbol in range(0, nr_symbols):
    passwordList.append(random.choice(symbols))


for number in range(0, nr_numbers):
    passwordList.append(random.choice(numbers))

random.shuffle(passwordList)


password = ""
for char in passwordList:
    password += char
print(f"Your password is {password}")

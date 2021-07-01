print("\nWelcome to the LOVE CALCULATOR!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2
lower = names.lower()

t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")

true = t + r + u + e

l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")

love = l + o + v + e

strscore = str(true) + str(love)
score = int(strscore)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like Coke and Mentos!")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

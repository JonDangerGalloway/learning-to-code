print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza to you want? S, M, or L?    ")
add_pepperoni = input("Do you want pepperoni? Y or N?     ")
extra_cheese = input("Do you want extra cheese? Y or N?   ")

cost = 0

if size == "S":
    cost += 15
elif size == "M":
    cost += 20
else:
    cost += 25

if add_pepperoni == "Y":
    if size == "S":
        cost += 2
    else:
        cost += 3

if extra_cheese == "Y":
    cost += 1

print(f"Your total is ${cost}.")
print("Welcome to the tip calculator. \n")
bill = float(input("What is the total bill?   $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15?   "))
people = int(input("How many people are splitting the bill?   "))
tipPercent = (percent / 100) + 1
eachTotal = (bill / people) * tipPercent
#final = round(eachTotal, 2)
final = "{:.2f}".format(eachTotal)
print(f"Each person should pay ${final}.")
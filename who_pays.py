import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#names = ['jon', 'james', 'matt', 'luke', 'adam']
number = (len(names))
pickedNumber = random.randint(0, number - 1)
pickedName = names[pickedNumber]
print(f"{pickedName} is going to buy the meal today!")
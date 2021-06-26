print("Welcome to the BMI Calculator. \n")
height = input("Please enter your height in meters. \n")
weight = input("Please enter your weight in kg. \n")
BMI = float(weight) / float(height) ** 2
result = int(BMI)
print(f"Your BMI is {result}")
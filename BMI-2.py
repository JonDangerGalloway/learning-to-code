height = float(input("Enter your height in m: \n"))
weight = float(input("Enter your weight in kg \n"))

calc = weight / (height ** 2)
bmi = round(calc)

if bmi < 18.5:
    print(f"Your BMI is {bmi},you are UNDERWEIGHT")
elif bmi < 25:
    print(f"Your BMI is {bmi},you are NORMAL WEIGHT")
elif bmi < 30:
    print(f"Your BMI is {bmi},you are OVERWEIGHT")
elif bmi < 35:
    print(f"Your BMI is {bmi},you are OBESE")
else:
    print(f"Your BMI is {bmi},you are CLINICALLY OBESE")
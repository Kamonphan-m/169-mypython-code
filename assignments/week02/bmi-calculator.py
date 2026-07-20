# Question 1: BMI Calculator

weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print(f"BMI: {bmi:.1f}")

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal weight"
elif 25.0 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")
weight = float(input("Please enter you weight in kgs: "))
height = float(input("Please enter your height in meters: "))
BMI = weight / (height * height)

if BMI <= 18:
    print("You are underweight")
elif BMI <= 25:
    print("You have a healthy weight")
elif BMI > 25:
    print("You are obese")
print(BMI)

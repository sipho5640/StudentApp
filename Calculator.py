num1 = float(input("please enter your first number: "))
operator = input("Please enter the operator you want to use: ")
num2 = float(input("please enter your second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "%":
    print(num1 % num2)
else:
    print("INVALID OPERATOR")









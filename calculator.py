# Python Calculator

operator = input("Enter an operator (+ - * /): ")
numberOne = float(input("Enter the 1st number: "))
numberTwo = float(input("Enter the 2nd number: "))

if operator == "+":
    result = numberOne + numberTwo
    print(round(result))
elif operator == "-":
    result = numberOne - numberTwo
    print(round(result))
elif operator == "*":
    result = numberOne * numberTwo
    print(round(result))
elif operator == "/":
    result = numberOne / numberTwo
    print(round(result))
else:
    print(f"{operator} is not a valid operator!")
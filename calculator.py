# Python Calculator

# Taking user input for operator as like + - * /
operator = input("Enter an operator (+ - * /): ")
# Taking two user input for number one and number two calculate
numberOne = float(input("Enter the 1st number: "))
numberTwo = float(input("Enter the 2nd number: "))
# Checking operator and calculate based on operator
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
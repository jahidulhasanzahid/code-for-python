# Python Calculator

operator = input("Enter an operator (+ - * /): ")
numberOne = float(input("Enter the 1st number: "))
numberTwo = float(input("Enter the 2nd number: "))

if operator == "+":
    result = numberOne + numberTwo
    print(result)
elif operator == "-":
    result = numberOne - numberTwo
    print(result)
elif operator == "*":
    result = numberOne * numberTwo
    print(result)
elif operator == "/":
    result = numberOne / numberTwo
    print(result)
# This is a simple implementation of Python if else condition with a simple concept
print("Welcome to Python under pass. Your vehicle should be under 13 feet height to get permission to pass.")
myCarHeight = float(input("What is your car height? \nfeet: "))
if 1 <= myCarHeight <= 13:
    print("You are approved. Under pass is available for you.")
else:
    print("We are sorry! For security purpose we can't give approval to pass.")
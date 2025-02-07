# This is a tip calculator. Based on total bill and total percentage of tip, it will calculate tip for each person.
print("Welcome to the Tip calculator!")
# assign a variable and as it's for taking input for amount, so i set data type as float
totalBill = float(input("What is your total bill? \n$"))
# assign a variable with int data type for taking input what is the tip percentage they want to give
tipPercentage = int(input("How much tip do you want to give as percentage? example: 5, 10, 15, 20, 25 \n"))
# this assign variable is for knowing how many person want to share this bill
totalPerson = int(input("Total Person you want to share? \n"))

# calculating the total bill with percentage
totalTip = (totalBill * tipPercentage) / 100
totalBillWithTip = totalBill + totalTip
eachPersonFinalBill = round(totalBillWithTip / totalPerson, 2)
eachPersonFinalBill = "{:.2f}".format(eachPersonFinalBill)
print(f"Your total bill is ${totalBill}")
print(f"Total Tip is ${totalTip}")
print(f"Your final bill is ${totalBillWithTip}")
print(f"Each of person will get ${eachPersonFinalBill} tip")

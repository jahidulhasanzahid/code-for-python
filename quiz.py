# tuple
questions = ("What is Capital of Bangladesh?: ",
             "What is the Capital of USA?: ",
             "What is the Capital of Japan?: ",
             "What is the Capital of Canada?: ",
             "What is the Capital of Germany?: ")
# 2d tuple
options = (("A. Chattogram","B. Khulna","C. Rangpur","D. Dhaka"),
           ("A. New York","B. Washington, D.C","C. California","C. Texas"),
           ("A. Tokyo","B. Aomori","C. Yamagata","D. Saitama"),
           ("A. Alberta","B. Ottawa","C. Nunavut","D. Northwest Territories"),
           ("A. Berlin","B. Saarland","C. Brandenburg","D. Saxony"))

answers = ("D","A","A","B","A")
guesses = []
# take a variable with zeo value for score calculate and another variable for number of questions
score = 0
question_num = 0

# for loop for showing all questions and taking input from user
for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

# printing the results with answer and guess
print("-------------------------")
print("---------RESULT----------")
print("-------------------------")
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}")
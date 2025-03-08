# This is a language learning game, It's fun and easy to learn very common word which we use in our daily life.
import random

words = [
    {"spanish" : "el", "english" : "the"},
    {"spanish": "de", "english": "of"},
    {"spanish": "que", "english": "of"},
    {"spanish": "y", "english": "that"},
    {"spanish": "a", "english": "to"},
    {"spanish": "en", "english": "in"},
]
# you can add more words here, if you want

def quiz(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the english translation of `{word['spanish']}`?")
        answer = input("Your Answer : ").strip().lower()
        correct_answer = word['english'].lower()

        if answer == correct_answer:
            score += 1
        else:
            print(f"Wrong, The Correct answer is `{correct_answer}`.\n")

    print(f"Quiz completed! Your score is: `{score}/{len(words)}`")



def main():
    print("Welcome to the language learning app.")
    input("Press Enter to start quiz.....")
    quiz(words)

if __name__ == '__main__':
    main()
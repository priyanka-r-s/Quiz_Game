import random

print("Welcome to my computer Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()

print("Okay! Let's Play :)")
score = 0
questions_asked = 0
max_questions = 5

questions = [
    ["What CPU stands for?", "central processing unit"],
    ["Python was developed by whom?", "guido van rossum"],
    ["Collection of key–value pairs is which datatype?", "dictionary"],
    ["What is Exponent operator in Python?", "**"],
    ["What is Equality comparison operator?", "=="],
    ["What is the Keyword for conditional statement?", "if"],
    ["Which Loop used when iterations are known?", "for"],
    ["Which Keyword to skip iteration?", "continue"],
    ["Which Loop used when condition is checked?", "while"],
    ["Which Keyword to define a function?", "def"],
    ["String indexing starts from which index?", "0"],
    ["Which Method to add element at end in list?", "append()"],
    ["Which Keyword is used to handle exceptions?", "try"],
    ["Which keyword is used for block executed if error occurs?", "except"],
    ["Which Module is used for random numbers?", "random"]
]

while questions and questions_asked < max_questions:
    question = random.choice(questions)
    questions.remove(question)

    answer = input(question[0] + " ").lower()
    questions_asked += 1

    if answer == question[1]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice == "no":
        break

print("\nQuiz Over!")
print("Total Questions Played:", questions_asked)
print("Your final score is", score)
print("You got", (score / questions_asked) * 100, "%")

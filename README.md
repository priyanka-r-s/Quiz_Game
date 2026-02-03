# Quiz_Game
**Python Quiz Game**
**Project Description**
This is a console-based Python Quiz Game where questions are asked in random order.
The player can exit manually or the quiz will automatically stop after 5 questions.
At the end, the total score and percentage are displayed.

** Features**
Random question selection using random
No repeated questions
Maximum of 5 questions per game
Manual exit option during the quiz
Score and percentage calculation
Beginner-friendly Python code
 **How to Run the Project**
Make sure Python is installed on your system
Save the file as quiz.py
Open terminal / command prompt
Run the program using:
python quiz.py
** How the Quiz Works**
User is asked whether they want to play
Questions are selected randomly using random.choice()
Each question is asked only once
User can continue or exit after each question
Quiz ends after 5 questions or manual exit
Final score and percentage are displayed
**Logic Used**
random.choice() → selects a random question
list.remove() → avoids repeated questions
while loop → controls quiz flow
if-else → checks correct answers
Variables → store score and question count
** Output Example**
Correct!
Do you want to continue? (yes/no): yes
Quiz Over!
Total Questions Played: 5
Your final score is 4
You got 80.0 %
**Future Enhancements**
Add difficulty levels
Store questions in a file
Add timer for each question
Create GUI using Tkinter

from question_model import Question
from data import question_data
from quiz_brain import Quiz

questions = []
for question in question_data:
    questions.append(Question(question["text"], question["answer"]))


quiz = Quiz(questions)
while quiz.has_questions():
    ques = quiz.next_question()
    ans = input(f"\n\nQ{quiz.question_number}:{ques} (True/False):").capitalize()
    if ans == quiz.check_answer():
        print("You got it right!")
        print(f"The correct answer was: {quiz.check_answer()}")
        print(f"Your current score is: {quiz.get_score()}/{quiz.question_number}")
    else:
        print("That's wrong.")
        print(f"The correct answer was: {quiz.check_answer()}")
        print(f"Your current score is: {quiz.points}/{quiz.question_number}")
print("\n\nYou've completed the quiz")
print(f"Your final sore was: {quiz.points}/{quiz.question_number}")



from tkinter import *
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
if question_data is None:
    raise ValueError("question_data is None. Please check the data import.")

question_bank=[]
for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)


quiz=QuizBrain(question_bank)
quiz_ui=QuizInterface(quiz)

print("you have completd the quiz")
print(f"you final score was: {quiz.score}/{quiz.question_number}")


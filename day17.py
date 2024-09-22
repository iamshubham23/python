# class user:
#     def __init__(self,user_id,username):
#         self.id=user_id
#         self.username=username
#         self.followers=0
#         self.following=0
#         print("new user has been created")
#     def follow(self,user):
#         user.followers+=1
#         self.following+=1

# user_1=user("001","shubham")
# user_2=user("002","angela")

# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

#quiz
# class Question:
#     def __init__(self,q_text,q_answer):
#         self.text=q_text
#         self.answer=q_answer
# new_q=Question("mohan","False")      
# print(new_q.text)  

# from question_model import question
# from data import question_data
class Question:
    def __init__(self,q_text,q_answer):
        self.text=q_text
        self.answer=q_answer

question_data=[
    {"text":"A slugs blood is green","answer":"True"},
    {"text":"the loudest animal is the african elephant","answer":"False"},
    {"text":"Approximately one quater of human bones are in the feet","answer":"TRUE"}
]
question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
   

class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number +=1
        print(f"Q.{self.question_number}:{current_question.text} (True/False):")
quiz=QuizBrain(question_bank)
quiz.next_question()

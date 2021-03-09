from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question = Question(i["text"],i["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
  quiz.next_question()
  
print("You have completed the quiz!")
print(f"Your final score was {quiz.score}/{len(question_bank)}")
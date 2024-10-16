from question_model import Question
from data import question_data
from quizbrain import QuizBrain

question_bank = []

for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
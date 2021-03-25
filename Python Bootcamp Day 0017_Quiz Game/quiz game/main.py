from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
i = 0
for x in range(len(question_data)):
    question_text = question_data[i]["question"]
    question_answer = question_data[i]["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    i += 1

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have finished the quiz!")
percentage = round((quiz.score / quiz.question_number)*100,2)
print(f"Your final score is {quiz.score}/{quiz.question_number}: {percentage}%")


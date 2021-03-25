class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        #below logic will return True or False
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}")
        percentage = round((self.score / self.question_number)*100,2)
        print(f"Your current score is {self.score}/{self.question_number}: {percentage}%\n")


    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text}. True/False?: ")
        self.check_answer(user_answer, question.answer)

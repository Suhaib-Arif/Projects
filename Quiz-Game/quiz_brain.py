class QuizBrain:
    def __init__(self,question_bank):
        self.question_number=0
        self.question_list=question_bank
        self.score=0

    def still_has_questions(self):
        return not self.question_number == len(self.question_list)

    def next_question(self):
        current_question=self.question_list[self.question_number]
        current_answer=current_question.answer
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number} {current_question.text} (True/False)? : ").title()
        self.check_answer(user_answer,current_answer)

    def check_answer(self,user_answer,current_answer):
        if user_answer == current_answer:
            print("The answer was correct")
            self.score += 1
        else:
            print("The answer is wrong")
        print(f"The correct answer is {current_answer}")
        print(f"The score is {self.score}/{self.question_number}")
        print("")

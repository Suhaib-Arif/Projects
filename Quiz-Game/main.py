from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# new_q= Question()
question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_q = Question(text,answer)

    question_bank.append(new_q)

qb=QuizBrain(question_bank)
while qb.still_has_questions():
    qb.next_question()

print("You have completed the Quiz")
print(f"Your final score is {qb.score}/{qb.question_number}")

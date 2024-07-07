from question_model import Question
from data import question_data
from quiz_brain import Brain

question_bank = []
for question in question_data:
    question_t = question["question"]
    question_a = question["correct_answer"]
    question_c = question["category"]
    new_question = Question(question_t, question_a, question_c)
    question_bank.append(new_question)

quiz = Brain(question_bank)
quiz_on = True


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

from question_model import Question
from data import question_data, var
from quiz_brain import QuizBrain


question_bank=[]

# for item in question_data:
#     question_bank.append(Question(item["question"],item["correct_answer"]))
for item in var["results"]:
    question_bank.append(Question(item["question"],item["correct_answer"]))


qb=QuizBrain(question_bank)
while qb.current_question():
    print(f"Current  score is {qb.score}/{len(qb.question_list)}")

print(f"Final score {qb.score}")
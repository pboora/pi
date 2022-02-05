class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score=0


    def rightansw(self,test):
        return test.lower() == self.question_list[self.question_number].answer.lower()

    def current_question(self):
        test = input(f"Q {self.question_number + 1} {self.question_list[self.question_number].text} True/False ? ")
        if self.rightansw(test):
            self.score+=1
            print("Right Answer\n")
        else:
            print("Wrong Answer\n")

        print(f"Right Answer was {self.question_list[self.question_number].answer}")
        self.question_number+=1
        return  self.question_number < len(self.question_list)


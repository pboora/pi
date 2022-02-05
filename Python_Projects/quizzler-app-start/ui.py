THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import  QuizBrain
import time

class QuizInterface(QuizBrain):
    def __init__(self, qlist):
        super().__init__(qlist)
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        t_img = PhotoImage(file="./images/true.png")
        f_img = PhotoImage(file="./images/false.png")
        self.tr_but = Button(image=t_img, highlightthickness=0, command=self.t_click)
        self.fl_but = Button(image=f_img, highlightthickness=0, command=self.f_click)
        self.l_score = Label(text="Score : 0", bg=THEME_COLOR, fg="WHITE")
        self.l_score.grid(row=0,column=1)
        self.tr_but.grid(row=3, column=0)
        self.fl_but.grid(row=3, column=1)
        self.q_text = self.canvas.create_text(150, 125, text=self.next_question(), fill=THEME_COLOR, width=200, font=("arial", 20, "italic"))
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)
        self.window.mainloop()


    def t_click(self):
        print("Clicked True\n")
        self.feedback(self.check_answer('True'))
        self.update_score()

    def next_q(self):
        self.canvas.config(bg="WHITE")
        if self.still_has_questions():
            self.canvas.itemconfig(self.q_text, text=self.next_question())
        else:
            self.canvas.itemconfig(self.q_text, text="Game Over!")
            self.tr_but.config(state="disabled")
            self.fl_but.config(state="disabled")

    def f_click(self):
            print("Clicked False\n")
            self.feedback(self.check_answer('False'))
            self.update_score()

    def update_score(self):
        self.l_score.config(text=f" Score : {self.score}/{self.question_number}")

    def feedback(self,ans:bool):
        if ans:
            self.canvas.config(bg="GREEN")
        else:
            self.canvas.config(bg="RED")
        self.window.after(1000, self.next_q)

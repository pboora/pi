from turtle import Screen, Turtle
import turtle

import pandas
import pandas as pd

timmy = Turtle()
fl = pd.read_csv("50_states.csv")

screen = Screen()
screen.title("US States Games")

img_f = "blank_states_img.gif"
screen.addshape(img_f)
timmy.shape(img_f)


# def get_mouse_click_ccor(x, y):
#     print(x, y)

tim_t = Turtle()
tim_t.penup()
tim_t.hideturtle()


guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50  is Correct ", prompt="Name please").title()

    if answer_state == "Exit":
        st_lst = fl.state.to_list()
        # missed = []
        # for state in st_lst:
        #     if state not in guessed_state:
        #         missed.append(state)
        missed = [state for state in st_lst if state not in guessed_state]
        missed_data = pandas.DataFrame(missed)
        missed_data.to_csv("Learn_states.csv")

        # missed = (state for state in st_lst if state not in guessed_state)
        break
    chk_st = fl[fl.state == answer_state]
    if chk_st.empty:
        print(" Wrong Answer Try again")
    else:
        tim_t.goto(int(chk_st.x), int(chk_st.y))
        tim_t.write(chk_st.state.item())
        guessed_state.append(answer_state)



print(missed)

# turtle.onscreenclick(get_mouse_click_ccor)
turtle.mainloop()

screen.exitonclick()
from tkinter import *
from PIL import ImageTk, Image


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
# WORK_MIN = 4
# SHORT_BREAK_MIN = 2
# LONG_BREAK_MIN = 5
timer =None
mark =""
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

def on_reset():
    global reps, timer, mark
    reps = 0
    mark = ""
    windo.after_cancel(timer)
    timer_label["text"] = "Timer"
    ch_label.config(text=mark)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def on_start():
    global reps, mark
    reps += 1

    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_min = LONG_BREAK_MIN

    # while reps <= 8:
    if reps % 8 == 0:
        count_down(long_break_min, "LB")
        mark += "✅"
        ch_label.config(text=mark)

    elif reps % 2 ==0:
        mark += "✅"
        ch_label.config(text=mark)

        count_down(short_break_sec,"SB")

    else:
        count_down(work_sec, "Work")
    print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import math

def count_down(count, wp):
    global timer, mark
    c_min = math.floor(count/60)
    if c_min < 10:
        c_min = f"0{c_min}"
    c_sec = count % 60
    if c_sec < 10:
        c_sec = f"0{c_sec}"
    if count > 0:
        # timer_label.config(text=wp)
        if wp == "Work":
            canvas.itemconfig(tmr, text=f"{c_min}:{c_sec}")
            timer_label.config(text=f"Work ", fg=PINK)
        elif wp == "LB":
            canvas.itemconfig(tmr, text=f"{c_min}:{c_sec}")
            timer_label.config(text="Long Break", fg=GREEN)
        else:
            # for _ in range(int(reps / 2)):
            canvas.itemconfig(tmr, text=f"{c_min}:{c_sec}")
            timer_label.config(text="Short Break", fg=RED)
        timer = windo.after(1000, count_down, count-1, wp)
    else:
        if reps < 8:
            print(reps)
            on_start()

# ---------------------------- UI SETUP ------------------------------- #

windo = Tk()
windo.title("Pomodoro")
windo.config(padx=80, pady=40, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 75, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)
# img = ImageTk.PhotoImage(Image.open("tomato3.jpg"))
# l = Label(image=img)
# l.pack()

canvas = Canvas(width=450, height=550, bg=YELLOW, highlightthickness=0)
# t_img = PhotoImage(file="tomato.png")
t_img = PhotoImage(file="buddha.png")
canvas.create_image(225, 250, image=t_img)
tmr = canvas.create_text(225, 505, text="00:00", fill="blue", font=(FONT_NAME, 55, "bold"))
canvas.grid(column=1, row=1)





start_button = Button(text="Start", command=on_start)
start_button.grid(column=0, row=2)



reset_button = Button(text="Reset", command=on_reset)
reset_button.grid(column=2, row=2)

# ch_label = Label(text="✅")
ch_label = Label()
ch_label.grid(column=1, row=3)



windo.mainloop()
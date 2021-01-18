from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- #
# tie countdown to click of start button
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# need to keep listioning on window.mainloop()-
def count_down(count):
    #format count down
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
         count_sec = f"0{count_sec}"
   #update the timer_text with kwarg
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count> 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# create window
window = Tk()
# add some room around tomato , add padding to the window
# background color,and remove the box around tomato pic
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)
# set window title
window.title("Pomodoro")

########## create time Label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
# grind instead fo pack
title_label.grid(column=1, row=0)
########## create canvas to hold the picture of tomato, add bg color
canvas = Canvas(width=200, height=224, bg=YELLOW)
# need to make image a PhotoImage file first
tomato_img = PhotoImage(file="tomato.png")
# add image to the Canvas with create image
canvas.create_image(102, 112, image=tomato_img)
# add timer text to tomato, making a var so it can be watched and updated
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# specify layout of how canvas is going on the screen
canvas.grid(column=1, row=1)

######### create buttons
# kick off start_timer by passing in the function with command
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)
######### create check mark
check_marks = Label(fg=GREEN,bg=YELLOW )
check_marks.grid(column=1, row=3)







# so window shows up
window.mainloop()

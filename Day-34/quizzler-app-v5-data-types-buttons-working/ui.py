from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizeInterface:
    #pass in the paramiter quiz_brain into the QuizeInterface
    def __init__(self, quiz_brain: QuizBrain):
        # create a property set to quiz_brain we
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quzzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")

        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
# call next question from quiz_brain
    def get_next_question(self):
        #using next_question method - that came from quiz_brain/main.py
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text= q_text)
    def true_pressed(self):
        #pass over True when true press is called
        self.quiz.check_answer("True")

    def false_pressed(self):
        #pass over False when false press is called
        self.quiz.check_answer("False")
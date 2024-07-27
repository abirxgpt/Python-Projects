from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#D0B8A8"
FONTFORMAT = ("arial", 20, "italic")

class QuizUIModule:
    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.quiz_brain = quiz
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.card = PhotoImage(file="images/img.png")
        self.tick = PhotoImage(file="images/tick.png")
        self.mark = PhotoImage(file="images/mark.png")

        self.images = Canvas(width=500, height=500, bg=THEME_COLOR, highlightthickness=0)
        self.canvas_image = self.images.create_image(250, 250, image=self.card)
        self.canvas_title = self.images.create_text(
            250,
            250,
            width=380,
            text="QUIZ START FROM HERE",
            fill="grey",
            font=FONTFORMAT
        )
        self.images.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        self.tick_button = Button(image=self.tick, highlightthickness=0, bg=THEME_COLOR, command=self.true_answer)
        self.tick_button.grid(column=0, row=2)
        self.mark_button = Button(image=self.mark, highlightthickness=0, bg=THEME_COLOR, command=self.false_answer)
        self.mark_button.grid(column=1, row=2)
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.images.config(bg=THEME_COLOR)
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            question_text = self.quiz_brain.next_question()
            self.images.itemconfig(self.canvas_title, text=question_text)
        else:
            self.images.itemconfig(self.canvas_title, text=f"You've Completed the Quiz \nHere's your Score: {self.quiz_brain.score}")
            self.tick_button.config(state="disabled")
            self.mark_button.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)
    def false_answer(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.images.config(bg="green")
        else:
            self.images.config(bg="red")
        self.window.after(1000, self.next_question)

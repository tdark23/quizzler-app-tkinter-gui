from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface:
    # getting access to the quizz_brain and defining the data type
    # Always define the data type
    def __init__(self, quizz_brain: QuizBrain):
        # getting access to the quizz_brain which has been passed as a property
        self.quiz = quizz_brain
        self.window = Tk()
        self.window.title("Quizller")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="question", 
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()
    
    def get_next_question(self):
        # resetting the background of the canvas to white
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            # updating the score
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            # actually getting the next question
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quizz.")
            # deactivate the buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        '''This function is going to change the change the background color, depending of the answer'''
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # passing to the next question after 1s delay
        self.window.after(1000, self.get_next_question)

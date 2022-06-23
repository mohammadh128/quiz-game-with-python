from tkinter import *
from tkinter import messagebox as mb
import json, os
from util import mathEvaluation
import generate

class Quiz:
    def __init__(self, questions, options, answers):
        self.questions = questions
        self.options = options
        self.answers = answers
        self.q_no = 0
        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected = IntVar()
        self.display_title()
        self.display_question()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        # no of questions
        self.data_size = len(self.questions)
        self.correct = 0

    def display_result(self):
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, q_no):
        # checks for if the selected option is correct
        if self.opt_selected.get() == self.answers[q_no]:
            # if the option is correct it return true
            return True

    def next_btn(self):
        if self.opt_selected.get() == 0:
            return
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1

        # checks if the q_no size is equal to the data size
        if self.q_no == self.data_size:
            # if it is correct then it displays the score
            self.display_result()
            gui.destroy()
        else:
            # shows the next question
            self.display_title()
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="dark olive green", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=380)
        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))
        quit_button.place(x=700, y=50)

    # This method deselect the radio button on the screen
    # Then it is used to display the options available for the current
    # question which we obtain through the question number and Updates
    # each of the options for the current question of the radio button.

    def display_options(self):
        val = 0
        # deselecting the options
        self.opt_selected.set(0)
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        q_no = Label(gui, text=f"{self.q_no+1}. {self.questions[self.q_no]}", width=60,
                     font=('ariel', 16, 'bold'), anchor='w')
        q_no.place(x=70, y=100)

    def display_title(self):
        # The previous answer to be shown
        if self.q_no > 0:
            title = Label(gui, text=f"{self.questions[self.q_no-1]}={mathEvaluation(self.questions[self.q_no-1])}",
                        width=50, bg="gray25", fg="white", font=("ariel", 20, "bold"))
            title.place(x=0, y=2)

    def radio_buttons(self):
        q_list = []
        # position of the option
        y_pos = 150
        # adding the options to the list
        while len(q_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list)+1, font=("ariel", 14))
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40
        return q_list

gui = Tk()
gui.geometry("800x450")
gui.title("Math Quiz")

with open(os.path.join("data", "data.json")) as f:
    data = json.load(f)

quiz = Quiz(data['question'], data['options'], data['answer'])
gui.mainloop()
from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Quiz:
    def __init__(self):

        # Formatting variables...
        background_color = "#F4F6FC"

        self.starting_question = IntVar()
        self.starting_question.set(0)

        self.low_number = IntVar()
        self.low_number.set(0)

        self.high_number = IntVar()
        self.high_number.set(0)

        # Quiz frame
        self.quiz_frame = Frame(bg=background_color, height=300, width=300,
                                pady=10, padx=10)
        self.quiz_frame.grid(row=4)

        # Entry Frame
        self.entry_frame = Frame(bg=background_color, height=300, width=300,
                                 pady=10, padx=10)
        self.entry_frame.grid(row=2)

        self.error_frame = Frame(bg=background_color, height=300, width=300,
                                 pady=10, padx=10)
        self.error_frame.grid(row=3)

        # Heading (row 0)
        self.maths_label = Label(text="Math Quiz",
                                 font="Arial 32 bold",
                                 bg="#F4F6FC",
                                 padx=10, pady=10)
        self.maths_label.grid(row=0)

        # Label for when input is incorrect (row 5)
        self.amount_error_label = Label(self.error_frame, font="arial 10 italic",
                                        text="", bg=background_color)
        self.amount_error_label.grid(row=5, columnspan=6)
        # Label for numbers between (row 0)
        self.entry_label_1 = Label(self.entry_frame, text="Numbers Between", font="Arial 10",
                                   bg="#F4F6FC", padx=10, pady=1)
        self.entry_label_1.grid(row=0, columnspan=5)
        # entry for low number (row 1)
        self.low_num_entry = Entry(self.entry_frame, width=2,
                                   font="Arial 10 bold", bg="white")
        self.low_num_entry.grid(row=1, column=1)
        # Label between low and high entry (row 1)
        self.entry_label_2 = Label(self.entry_frame, text="and",
                                   font="Arial 10", bg="#F4F6FC",
                                   padx=10, pady=1)
        self.entry_label_2.grid(row=1, column=2)
        # entry for high number (row 1)
        self.high_num_entry = Entry(self.entry_frame, width=2,
                                    font="Arial 10 bold", bg="white")
        self.high_num_entry.grid(row=1, column=3)
        # label for amount of questions (row
        self.entry_label_2 = Label(self.entry_frame, text="Amount Of Questions",
                                   font="Arial 10", bg="#F4F6FC",
                                   padx=10, pady=1)
        self.entry_label_2.grid(row=5, columnspan=5)

        self.amount_entry = Entry(self.entry_frame, width=2,
                                  font="Arial 10 bold", bg="white")
        self.amount_entry.grid(row=6, column=2)

        # Game Buttons (row 2)
        self.game_buttons_frame = Frame(self.quiz_frame, bg="#F4F6FC")

        self.game_buttons_frame.grid(row=3, pady=10)

        self.question_amount_btn = Button(self.game_buttons_frame, text="Enter", font="Arial 10", width=10,
                                          bg="#D0CEE2", padx=10, pady=10, command=self.check_question)
        self.question_amount_btn.grid(row=0, )

        self.addition_btn = Button(self.game_buttons_frame,
                                   text="Addition", font="Arial 10", width=10,
                                   bg="#CCE5FF", padx=10, pady=10,
                                   command=lambda: self.to_game(1))
        self.addition_btn.grid(row=1, column=0)

        self.subtraction_btn = Button(self.game_buttons_frame,
                                      text="Subtraction", font="Arial 10", width=10,
                                      bg="#CCE5FF", padx=10, pady=10,
                                      command=lambda: self.to_game(2))
        self.subtraction_btn.grid(row=2, column=0)

        self.multiplication_btn = Button(self.game_buttons_frame,
                                         text="Multiplication", font="Arial 10", width=10,
                                         bg="#CCE5FF", padx=10, pady=10,
                                         command=lambda: self.to_game(3))
        self.multiplication_btn.grid(row=3, column=0)

        self.help_frame = Frame(self.quiz_frame)
        self.help_frame.grid(row=3)
        # Disables game buttons
        self.addition_btn.config(state=DISABLED)
        self.subtraction_btn.config(state=DISABLED)
        self.multiplication_btn.config(state=DISABLED)

        # stats / help button frame (row 5)
        self.stats_help_frame = Frame(self.quiz_frame)
        self.stats_help_frame.grid(row=4, pady=10)

        self.help_button = Button(self.stats_help_frame, font="Arial 12", bg="#FAD9D5",
                                  text="Help", width=12, command=self.help)
        self.help_button.grid(row=0, column=1)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure()

    def check_question(self):
        starting_question = self.amount_entry.get()
        low_number = self.low_num_entry.get()
        high_number = self.high_num_entry.get()

        # Set error background colour (and assum that there are no
        # error at the start
        error_back = "#ffafaf"
        has_error = "no"
        error_feedback = ""

        # change background to white (for testing purposes) ...
        self.amount_entry.config(bg="white")
        self.amount_error_label.config(text="")
        self.low_num_entry.config(bg="white")
        self.low_num_entry.config(text="")
        self.high_num_entry.config(bg="white")
        self.high_num_entry.config(text="")

        self.addition_btn.config(state=DISABLED)
        self.subtraction_btn.config(state=DISABLED)
        self.multiplication_btn.config(state=DISABLED)

        # Check to see if high number is too low
        try:
            starting_question = int(starting_question)

            if starting_question < 5:
                has_error = "yes"
                error_feedback = "unfortunately amount of questions is to low"
                self.amount_entry.config(bg=error_back)
            elif starting_question > 20:
                has_error = "yes"
                error_feedback = "unfortunately amount of questions is to high"
                self.amount_entry.config(bg=error_back)

        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes with whole numbers"
            self.amount_entry.config(bg=error_back)

        try:
            low_number = int(low_number, )

            if low_number < -100:
                has_error = "yes"
                error_feedback = "Your low number cannot be lower than -100"
                self.low_num_entry.config(bg=error_back)
            elif low_number > 99:
                has_error = "yes"
                error_feedback = "unfortunately your low number can not exceed 99 "
                self.low_num_entry.config(bg=error_back)

        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes with whole numbers"
            self.low_num_entry.config(bg=error_back)

        try:
            high_number = int(high_number)

            if high_number <= low_number:
                has_error = "yes"
                error_feedback = "Your high number needs to be greater then your low number"
                self.high_num_entry.config(bg=error_back)
            elif high_number > 100:
                has_error = "yes"
                error_feedback = "unfortunately your high number can not exceed 100 "
                self.high_num_entry.config(bg=error_back)

        except ValueError:
            has_error = "yes"
            error_feedback = "Please fill the boxes with whole numbers"
            self.high_num_entry.config(bg=error_back)

        if has_error == "yes":
            self.amount_error_label.config(text=error_feedback)

        else:
            self.starting_question.set(starting_question)
            self.low_number.set(low_number)
            self.high_number.set(high_number)
            self.addition_btn.config(state=NORMAL)
            self.subtraction_btn.config(state=NORMAL)
            self.multiplication_btn.config(state=NORMAL)
            self.low_num_entry.config(state=DISABLED)
            self.high_num_entry.config(state=DISABLED)
            self.amount_entry.config(state=DISABLED)

    def to_game(self, op):
        starting_question = self.amount_entry.get()
        low_number = self.low_num_entry.get()
        high_number = self.high_num_entry.get()


        Game(self, op, starting_question, low_number, high_number)


class Game:
    def __init__(self, partner, op, starting_question, low_number, high_number):
        starting_question = int(starting_question)
        questions_played = int(1)
        how_many_right = int(0)

        self.correct = IntVar()
        self.correct.set(0)

        low_number = int(low_number)
        high_number = int(high_number)
        self.history_questions = []
        background_color = "#F4F6FC"

        # checks for what game button you pressed
        op = int(op)

        if op == 1:
            hi_lo_num = random.randrange(low_number, high_number)
            hi_lo_num2 = random.randrange(low_number, high_number)
            questions = "{} + {}".format(hi_lo_num, hi_lo_num2)
            var_correct = hi_lo_num + hi_lo_num2
            self.correct.set(var_correct)
            op_text = "Addition"
        elif op == 2:
            hi_lo_num = random.randrange(low_number, high_number)
            hi_lo_num2 = random.randrange(low_number, high_number)
            questions = "{} - {}".format(hi_lo_num, hi_lo_num2)
            var_correct = hi_lo_num - hi_lo_num2
            self.correct.set(var_correct)
            op_text = "Subtraction"
        elif op == 3:
            hi_lo_num = random.randrange(low_number, high_number)
            hi_lo_num2 = random.randrange(low_number, high_number)
            questions = "{} x {}".format(hi_lo_num, hi_lo_num2)
            var_correct = hi_lo_num * hi_lo_num2
            self.correct.set(var_correct)
            op_text = "Multiplication"

        self.history_questions.append(questions)

        # disable button
        partner.addition_btn.config(state=DISABLED)
        partner.subtraction_btn.config(state=DISABLED)
        partner.multiplication_btn.config(state=DISABLED)
        partner.help_button.config(state=DISABLED)

        # Set up Geo game one
        self.game_box = Toplevel()

        # Set up GUI Frame
        self.game_frame = Frame(self.game_box, width=300, bg=background_color)
        self.game_frame.grid()
        # Set up Geo Instruction heading (row 0)
        self.heading = Label(self.game_frame, text=op_text,
                             font="arial 20 bold", bg=background_color)
        self.heading.grid(row=0)
        # Geo text (label, row 1)
        self.game = Label(self.game_frame,
                          text="Fill the boxes",
                          justify=LEFT, width=50, bg=background_color, wrap=200)
        self.game.grid(row=1)

        self.ask_questions_frame = Frame(self.game_frame, bg=background_color)
        self.ask_questions_frame.grid(row=1)

        self.get1_label = Label(self.ask_questions_frame,
                                text=questions,
                                font="arial 10 bold", fg="black", bg=background_color)
        self.get1_label.grid(row=1)

        self.game_entry = Entry(self.ask_questions_frame, font="arial 15 bold")
        self.game_entry.grid(row=2)

        self.dismiss_export_frame = Frame(self.game_frame, bg=background_color)
        self.dismiss_export_frame.grid(row=2)

        # Dismiss button (row 4)
        self.dismiss_btn = Button(self.dismiss_export_frame, text="Dismiss", width=10, bg="#FAD9D5",
                                  font="arial 10 bold", pady=7,
                                  command=partial(self.close_game, partner))
        self.dismiss_btn.grid(row=1)
        self.check_ans_btn = Button(self.dismiss_export_frame, text="Check Answer", font="arial 10 bold", fg="black",
                                    bg="#D0CEE2", pady=7, width=13,
                                    command=lambda: self.check_ans(low_number, high_number, op, starting_question,
                                                                   questions_played, how_many_right,
                                                                   self.history_questions))
        self.check_ans_btn.grid(row=1, column=1)

        self.game_box.protocol('WM_DELETE_WINDOW', partial(self.close_game, partner))

    def check_ans(self, low_number, high_number, op, starting_question, questions_played, how_many_right,
                  history_questions):
        answer = self.game_entry.get()
        self.game_entry.config(state=DISABLED)

        var_correct = self.correct.get()

        # change background to white (for testing purposes) ...
        self.check_ans_btn.config(bg="white")
        self.check_ans_btn.config(text="")

        try:
            answer = int(answer)
            correct = int(var_correct)
            self.history_questions.append(answer)
            # Gives feedback on you answer
            if answer != correct:
                self.feedback_label = Label(self.ask_questions_frame, text="Incorrect answer ",
                                            font="arial 10 bold", fg="black", bg="#F4F6FC", pady=8, width=25)
                self.feedback_label.grid(row=3)

            elif answer == correct:
                self.feedback_label = Label(self.ask_questions_frame, text=" Correct answer",
                                            font="arial 10 bold", fg="black", bg="#F4F6FC", pady=7, width=25)
                self.feedback_label.grid(row=3)
                how_many_right += 1

        except ValueError:

            self.feedback_label = Label(self.ask_questions_frame, text=" No answer was given",
                                        font="arial 10 bold", fg="black", bg="#F4F6FC", pady=7, width=25)
            self.feedback_label.grid(row=3)
            # add finished button over next and export button
        if questions_played >= starting_question:
            self.finished_btn = Label(self.dismiss_export_frame, text="Finished", font="arial 10 bold", fg="black",
                                      bg="#F4F6FC", pady=9, width=14)
            self.finished_btn.grid(row=1, column=1)
            self.export_btn = Button(self.dismiss_export_frame, text="Export", font="arial 10 bold", fg="black",
                                     bg="#D0CEE2", pady=7, width=10,
                                     command=lambda: self.export(low_number, high_number, questions_played,
                                                                 how_many_right, history_questions))
            self.export_btn.grid(row=1, column=2)
        else:
            self.check_ans_btn.config(text="")
            self.next_btn = Button(self.dismiss_export_frame, text="Next", font="arial 10 bold", fg="black",
                                   bg="#D0CEE2", pady=7, width=13,
                                   command=lambda: self.next(low_number, high_number, op, starting_question,
                                                             questions_played, how_many_right, history_questions))
            self.next_btn.grid(row=1, column=1)

        self.played_label = Label(self.ask_questions_frame, font="arial 10 bold", fg="black",
                                  bg="#F4F6FC", pady=7,
                                  text="Question:{}/{}".format(questions_played, starting_question))
        self.played_label.grid(row=0)

    def next(self, low_number, high_number, op, starting_question, questions_played, how_many_right, history_questions):
        starting_question = int(starting_question)
        self.game_entry.config(state=NORMAL)
        self.game_entry.delete(0, 'end')

        # Give next question based on what game button you pressed
        if op == 1:
            hi_lo_num = random.randrange(low_number, high_number)
            hi_lo_num2 = random.randrange(low_number, high_number)
            questions = "{} + {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            var_correct = hi_lo_num + hi_lo_num2
            self.correct.set(var_correct)
            questions_played += 1
        elif op == 2:
            hi_lo_num = random.randrange(low_number, high_number)
            hi_lo_num2 = random.randrange(low_number, high_number)
            questions = "{} - {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            var_correct = hi_lo_num - hi_lo_num2
            self.correct.set(var_correct)
            questions_played += 1
        elif op == 3:
            hi_lo_num = random.randrange(low_number, high_number)
            hi_lo_num2 = random.randrange(low_number, high_number)
            questions = "{} x {}".format(hi_lo_num, hi_lo_num2)
            self.get1_label.config(text=questions)
            var_correct = hi_lo_num * hi_lo_num2
            self.correct.set(var_correct)
            questions_played += 1

        self.history_questions.append(questions)

        # Button to check if input was correct or incorrect
        self.check_ans_btn = Button(self.dismiss_export_frame, text="Check Answer", font="arial 10 bold", fg="black",
                                    bg="#D0CEE2", pady=7, width=13,
                                    command=lambda: self.check_ans(low_number, high_number, op,
                                                                   starting_question, questions_played, how_many_right,
                                                                   history_questions))
        self.check_ans_btn.grid(row=1, column=1)

    def close_game(self, partner):
        # Put help button back to normal and keep everything the same
        partner.addition_btn.config(state=DISABLED)
        partner.question_amount_btn.config(state=NORMAL)
        partner.subtraction_btn.config(state=DISABLED)
        partner.multiplication_btn.config(state=DISABLED)
        partner.help_button.config(state=NORMAL)
        partner.low_num_entry.config(state=NORMAL)
        partner.high_num_entry.config(state=NORMAL)
        partner.amount_entry.config(state=NORMAL)

        self.game_box.destroy()

    def export(self, low_number, high_number, questions_played, how_many_right, history_questions):
        Export(self, low_number, high_number, questions_played, how_many_right, history_questions)


class Help:
    def __init__(self, partner):
        background_color = "#F4F6FC"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel()

        # If user press cross at top, closes export and 'releases' export button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background_color)
        self.help_frame.grid()
        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame,
                                 text="Help / Instruction",
                                 font="arial 20 bold", bg=background_color)
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               text="This is a math game "
                                    " It will help you to learn addition subtraction and multiplication \n"
                                    "\n"
                                    "How do you play?\n"
                                    "\n"
                                    "The top left box is for the lowest number you want your questions to be\n"
                                    "\n"
                                    "The top right is for the highest number you want your questions to be\n"
                                    "\n"
                                    "The bottom box is for how many want to play a min of 5 and a max of 20 \n "
                                    "\n"
                                    "You will need to click enter to continue to choose what type of questions"
                                    " you want to play \n ",
                               justify=LEFT, width=50, bg=background_color, wrap=400, font="arial 12")
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="#FAD9D5",
                                  font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class Export:
    def __init__(self, partner, low_number, high_number, questions_played, how_many_right, history_questions):


        background_color = "#F4F6FC"

        # disable export button
        partner.export_btn.config(state=DISABLED)

        # Set up child window (ie: export box)
        self.export_box = Toplevel()

        # If user press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background_color)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.how_heading = Label(self.export_frame,
                                 text="Export", fg="black",
                                 font="arial 20 bold", bg=background_color)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                                         "in the box below "
                                                         "button to save your "
                                                         "game history "
                                                         "to a text file.",
                                 font="arial 13 italic",
                                 justify=LEFT, width=50, bg=background_color, wrap=200)
        self.export_text.grid(row=1)

        # Help text (label, row 1)
        self.history_label = Label(self.export_frame, text="your low number was: {}""\n"
                                                           "your high number was: {}""\n"
                                                           "you have played {} questions""\n"
                                                           "you got {} correct out of {}  ""\n"
                                   .format(low_number, high_number, questions_played, how_many_right, questions_played),
                                   font="arial 13 italic",
                                   justify=LEFT, width=50, bg=background_color, wrap=200)
        self.history_label.grid(row=2)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                                         "you enter below "
                                                         "already exists, "
                                                         "its contents will "
                                                         "be replaced with "
                                                         "your game "
                                                         "history",
                                 justify=LEFT, bg=background_color, fg="black",
                                 font="arial 10 italic", wrap=225, padx=10,
                                 pady=10)
        self.export_text.grid(row=3, pady=10)

        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="arial 14 bold")
        self.filename_entry.grid(row=4, pady=10)

        # error massage labels (initially blank, row 4 )
        self.save_error_label = Label(self.export_frame, text=" ", fg="black",
                                      bg="#F4F6FC")
        self.save_error_label.grid(row=5)

        # Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=6, pady=10)

        # Save and Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="arial 10 bold", fg="black",
                                  bg="#D0CEE2", padx=10, pady=10,
                                  command=partial(lambda: self.save_history(partner, low_number, high_number,
                                                                            questions_played, how_many_right,
                                                                            history_questions)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="arial 10 bold", fg="black",
                                    bg="#F8CECC", padx=10, pady=10,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, low_number, high_number, questions_played, how_many_right, history_questions):

        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()


        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            f.write("your low number was: {}""\n".format(low_number))
            f.write("your high number was: {}""\n".format(high_number))
            f.write("you have played {} questions""\n".format(questions_played))
            f.write("you got {} correct out of {}  ""\n".format(how_many_right, questions_played))
            f.write("{} ""\n".format(history_questions))

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_btn.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    root.configure(background='#F4F6FC')
    something = Quiz()
    root.mainloop()
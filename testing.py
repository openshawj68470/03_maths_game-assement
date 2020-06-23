from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:

    def __init__(self):

        # Formatting variables
        background_color = "#F4F6FC"

        # Initialise list to hold Quiz results
        self.all_calc_list = []
        # Converter frame
        self.converter_frame = Frame(bg=background_color, height=300, width=300,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Stats",
                                          font="Arial 19 bold",
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # User instructions (row 1)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Text.txt",
                                          font="Arial 10 italic", justify=LEFT,
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=1)
        # Anwser label (row 4)
        self.conversion_label = Label(self.converter_frame, font="Arial 10 bold",
                                      bg=background_color, pady=10)
        self.conversion_label.grid(row=4)

        # history / Help button frame (row 5)
        self.history_help_frame = Frame(self.converter_frame)
        self.history_help_frame.grid(row=5, pady=10)

        self.history_button = Button(self.history_help_frame, font="Arial 12 bold",
                                     text="Export", width=15,bg="#D0CEE2",
                                     command=lambda: self.export(self.all_calc_list))
        self.history_button.grid(row=0, column=0)

        self.help_button = Button(self.history_help_frame, font="Arial 12 bold",
                                  text="Close", width=5, bg="#FAD9D5")
        self.help_button.grid(row=0, column=1)

    def export(self, calc_history):
        Export(self, calc_history)

class Export:
            def __init__(self, partner, calc_history):

                background = "#F4F6FC"

                # Set up child window (ie: export box)
                self.export_box = Toplevel()

                # If user press cross at top, closes export and 'releases' export button
                self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

                # set up GUI Frame
                self.export_frame = Frame(self.export_box, bg=background, height=300, width=300,
                                          pady=10)
                self.export_frame.grid()

                # set up Export heading (row 0)
                self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                         font="Arial 12 bold", bg=background)
                self.how_heading.grid(row=0)

                # Export text (label, row 1)
                self.export_text = Label(self.export_frame,
                                         text="Enter a filename in the box below and press the Save button"
                                              " to save your quiz results to a text file",
                                         justify=LEFT, width=40, bg=background, wrap=250)
                self.export_text.grid(row=1)

                # dismiss button (row 2)
                self.export_txt = Label(self.export_frame, text="If the file you enter below already exists, "
                                                                "its contents will be replaced with your "
                                                                "quiz results",
                                        bg=background, font="arial 10 bold",
                                        justify=LEFT, width=40, wrap=250)
                self.export_txt.grid(row=2, pady=10)

                # Temperature entry box (row 2)
                self.filename_entry = Entry(self.export_frame, width=20,
                                            font="Arial 14 bold", bg="white")
                self.filename_entry.grid(row=3)

                # Error message Labels (initially blank, row 4)
                self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                              bg=background)
                self.save_error_label.grid(row=4)

                self.save_dismiss_frame = Frame(self.export_frame)
                self.save_dismiss_frame.grid(row=5, pady=10)

                self.save_btn = Button(self.save_dismiss_frame, text="save",
                                       bg="#D0CEE2", width=15, font="Arial 12 bold",
                                       command=partial(lambda: self.save_history(partner, calc_history)))
                self.save_btn.grid(row=0, column=0)

                self.dismiss_btn = Button(self.save_dismiss_frame, text="close",
                                          bg="#FAD9D5", font="Arial 12 bold", width=5,
                                          command=partial(self.close_export, partner))
                self.dismiss_btn.grid(row=0, column=1)

            def save_history(self, partner, calc_history):

                valid_char = "[A-Za-z0-9]"
                has_error = "no"

                filename = self.filename_entry.get()
                print(filename)

                for letter in filename:
                    if re.match(valid_char, letter):
                        continue

                    elif letter == " ":
                        problem = "(no space allowed)"
                    else:
                        problem = ("(no {}'s allowed)".format(letter))
                        has_error = "yes"

                if filename == "":
                    problem = "can't be blank"
                    has_error = "yes"

                if has_error == "yes":
                    print("Invalid filename - {}".format(problem))
                    # Display error message
                    self.save_error_label.config(text="Invalid filename - {}".format(problem))
                    # Change entry box background to pink
                    self.filename_entry.config(bg="#ffafaf")
                    print()

                else:
                    print("You entered a valid filename")
                    # add .txt suffix!
                    filename = filename + ".txt"

                    # create file to hold data
                    f = open(filename, "w+")

                    # add new line at end of each item
                    for item in calc_history:
                        f.write(item + "\n")

                    # close file
                    f.close()

            def close_export(self, partner):
                # Put  export button back to normal...
                self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()

from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:

    def __init__(self):

        # Formatting variables
        background_color = "#ADD8E6"

        # Initialise list to hold calculation history
        self.all_calc_list = []
        # Converter frame
        self.converter_frame = Frame(bg=background_color, height=300, width=300,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=1,
                                      font="Arial 14 bold", bg="white")
        self.to_convert_entry.grid(row=2)

        self.to_convert_entry = Entry(self.converter_frame, width=1,
                                      font="Arial 14 bold", bg="white")
        self.to_convert_entry.grid(row=2, column=1)

        # maths Heading (row 0)
        self.maths_converter_label = Label(self.converter_frame, text="maths",
                                          font="Arial 19 bold",
                                          bg=background_color,
                                          padx=10, pady=10)
        self.maths_converter_label.grid(row=0)
        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=1,
                                      font="Arial 14 bold", bg="white")
        self.to_convert_entry.grid(row=2)

        self.to_convert_entry = Entry(self.converter_frame, width=1,
                                      font="Arial 14 bold", bg="white")
        self.to_convert_entry.grid(row=2, column=1)
        
        self.game_buttons_frame = Frame(self.converter_frame, bg="#ADD8E6")

        self.game_buttons_frame.grid(row=3, pady=10)

        self.to_a_button = Button(self.game_buttons_frame,
                                  text="Addition", font="Arial 10 bold",
                                  bg="yellow", padx=10, pady=10,
                                  command=lambda: self.game(1))
        self.to_a_button.grid(row=0, column=0)

        self.to_d_button = Button(self.game_buttons_frame,
                                  text="Division", font="Arial 10 bold",
                                  bg="red", padx=10, pady=10,
                                  command=lambda: self.game(2))
        self.to_d_button.grid(row=1, column=0)

        self.to_m_button = Button(self.game_buttons_frame,
                                  text="Multiplication", font="Arial 10 bold",
                                  bg="red", padx=10, pady=10,
                                  command=lambda: self.game(3))
        self.to_m_button.grid(row=2, column=0)


        # history / Info button frame (row 5)
        self.history_info_frame = Frame(self.converter_frame)
        self.history_info_frame.grid(row=4, pady=10)

        self.history_button = Button(self.history_info_frame, font="Arial 12 bold",
                                     text="Game Stats", width=15,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

        self.info_button = Button(self.history_info_frame, font="Arial 12 bold",
                                  text="Info", width=5, command=self.info)
        self.info_button.grid(row=0, column=1)

    def info(self):
        print("You asked for info")
        get_info = Info(self)
        get_info.info_text.configure(text="Info text goes here")

    def history(self, calc_history):
        History(self, calc_history)


class Info:
    def __init__(self, partner):
        background = "orange"

        # disable info button
        partner.info_button.config(state=DISABLED)

        # Set up child window (ie: info box)
        self.info_box = Toplevel()

        # If user press cross at top, closes info and 'releases' info button
        self.info_box.protocol('WM_DELETE_WINDOW', partial(self.close_info, partner))

        # set up GUI Frame
        self.info_frame = Frame(self.info_box, bg=background)
        self.info_frame.grid()
        # set up Info heading (row 0)
        self.how_heading = Label(self.info_frame, text="Info / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)
        # Info text (label, row 1)
        self.info_text = Label(self.info_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.info_text.grid(row=1)
        # dismiss button (row 2)
        self.dismiss_btn = Button(self.info_frame, text="dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_info, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_info(self, partner):
        # Put  info button back to normal...
        partner.info_button.config(state=NORMAL)
        self.info_box.destroy()


class History:
    def __init__(self, partner, calc_histroy):

        background = "green"

        # disable info button
        partner.history_button.config(state=DISABLED)

        # Set up child window (ie: info box)
        self.history_box = Toplevel()

        # If user press cross at top, closes info and 'releases' info button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        # set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()
        # set up Info heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation history",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)
        # Info text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent "
                                  "calculations. Please use the "
                                  "export button to create a text "
                                  "file of all your calculations for "
                                  "this session", font="arial 10 italic",
                                  justify=LEFT, width=40, bg=background, wrap=250)
        self.history_text.grid(row=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("maths")
    something = Converter()
    root.mainloop()

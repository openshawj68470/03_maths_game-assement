from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Quiz:

    def __init__(self):

        # Initialise list to hold calculation history
        self.all_stats_list = []

        # Formatting variables
        background_color = "#F4F6FC"

        # Quiz frame
        self.quiz_frame = Frame(bg=background_color, height=300, width=300,
                                pady=10, padx=10)
        self.quiz_frame.grid(row=4)

        # Entry Frame
        self.entry_frame = Frame(bg=background_color, height=300, width=300,
                                 pady=10,padx=10)
        self.entry_frame.grid(row=2)

        self.entry_frame_2 = Frame(bg=background_color, height=300, width=300,
                                 pady=10,padx=10)
        self.entry_frame_2.grid(row=3)

        # Heading (row 0)
        self.maths_label = Label(text="Math Quiz",
                                 font="Arial 32 bold",
                                 bg="#F4F6FC",
                                 padx=10, pady=10)
        self.maths_label.grid(row=0)

        # Entry (for numbers they wanna play between)(row 1)
        self.Entry_label_1 = Label(text="numbers between",font="Arial 10",
                                   bg="#F4F6FC", padx=10, pady=3)
        self.Entry_label_1.grid(row=1)

        self.Low_num_entry = Entry(self.entry_frame, width=2,
                                     font="Arial 10 bold", bg="white")
        self.Low_num_entry.grid(row=1)

        self.Entry_label_2 = Label(self.entry_frame, text="and",
                                 font="Arial 10", bg="#F4F6FC",
                                 padx=10, pady=1)
        self.Entry_label_2.grid(row=1, column=2)

        self.High_num_entry = Entry(self.entry_frame, width=2,
                                     font="Arial 10 bold", bg="white")
        self.High_num_entry.grid(row=1, column=3)

        self.Entry_label_2 = Label(self.entry_frame_2, text="Amount Of Questions",
                                 font="Arial 10", bg="#F4F6FC",
                                 padx=10, pady=1)
        self.Entry_label_2.grid(column=2)

        self.Num_quest_entry = Entry(self.entry_frame_2, width=2,
                                     font="Arial 10 bold", bg="white")
        self.Num_quest_entry.grid(row=1, column=2)

        # Game Buttons (row 2)
        self.game_buttons_frame = Frame(self.quiz_frame, bg="#F4F6FC")

        self.game_buttons_frame.grid(row=3, pady=10)

        self.Addition_button = Button(self.game_buttons_frame,
                                  text="Addition", font="Arial 10", width=10,
                                  bg="#CCE5FF", padx=10, pady=10,
                                  command=lambda: self.game(1))
        self.Addition_button.grid(row=0, column=0)

        self.Division_button = Button(self.game_buttons_frame,
                                  text="Division", font="Arial 10", width=10,
                                  bg="#CCE5FF", padx=10, pady=10,
                                  command=lambda: self.game(2))
        self.Division_button.grid(row=1, column=0)

        self.Multiplication_button = Button(self.game_buttons_frame,
                                  text="Multiplication", font="Arial 10", width=10,
                                  bg="#CCE5FF", padx=10, pady=10,
                                  command=lambda: self.game(3))
        self.Multiplication_button.grid(row=2, column=0)



        # stats / Info button frame (row 5)
        self.stats_info_frame = Frame(self.quiz_frame)
        self.stats_info_frame.grid(row=4, pady=10)

        self.stats_button = Button(self.stats_info_frame, font="Arial 12",
                                     text="Game Stats", width=15, bg="#D0CEE2",
                                     command=lambda: self.stats(self.all_stats_list))
        self.stats_button.grid(row=0, column=0)
        
        self.info_button = Button(self.stats_info_frame, font="Arial 12", bg="#FAD9D5",
                                  text="Info", width=5, command=self.info)
        self.info_button.grid(row=0, column=1)

    def info(self):
        print("You asked for info")
        get_info = Info(self)
        get_info.info_text.configure(text="Info text goes here")

    def stats(self, stats_list):
        Stats(self, stats_list)

    def (self, partner):
        Multiplication(self, partner)




class Info:
    def __init__(self, partner):
        background = "#F4F6FC"

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


class Stats:
    def __init__(self, partner, stats_list):

        background = "#F4F6FC"

        # disable info button
        partner.stats_button.config(state=DISABLED)

        # Set up child window (ie: info box)
        self.stats_box = Toplevel()

        # If user press cross at top, closes info and 'releases' info button
        self.stats_box.protocol('WM_DELETE_WINDOW',
                                partial(self.close_stats, partner))

        # set up GUI Frame
        self.stats_frame = Frame(self.stats_box, bg=background)
        self.stats_frame.grid()
        # Temperature Converter Heading (row 0)
        self.stats_label = Label(self.stats_frame, text="Stats",
                                 font="Arial 19 bold",
                                 bg=background,
                                 padx=10, pady=10)
        self.stats_label.grid(row=0)

        # User instructions (row 1)
        self.stats_label = Label(self.stats_frame,
                                 text="these are the statistics from"
                                      " your most recent quiz",
                                 font="Arial 10 italic", justify=LEFT,
                                 bg=background,
                                 padx=10, pady=10)
        self.stats_label.grid(row=1)

        self.stats_label = Label(self.stats_frame,
                                 text="",
                                 font="Arial 10 italic", justify=LEFT,
                                 bg=background,
                                 padx=10, pady=10)
        self.stats_label.grid(row=2)

        # history / Help button frame (row 5)
        self.Export_button_frame = Frame(self.stats_frame)
        self.Export_button_frame.grid(row=5, pady=10)

        self.dismiss_btn = Button(self.Export_button_frame, text="close",
                                  bg="#FAD9D5", font="Arial 12 bold", width=20,
                                  command=partial(self.close_stats, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_stats(self, partner):
        # Put stats button back to normal...
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("maths")
    something = Quiz()
    root.mainloop()

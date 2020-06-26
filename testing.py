class Multiplication:
    def __init__(self, partner):
        background = "#F4F6FC"

        # disable multiplication button
        partner.check.config(state=DISABLED)
        # Set up child window (ie: multiplication box)
        self.multiplication_box = Toplevel()

        # If user press cross at top, closes multiplication and 'releases' multiplication button
        self.multiplication_box.protocol('WM_DELETE_WINDOW', partial(self.close_multiplication, partner))

        # set up GUI Frame
        self.multiplication_frame = Frame(self.multiplication_box, bg=background)
        self.multiplication_frame.grid()
        # set up multiplication heading (row 0)
        self.how_heading = Label(self.multiplication_frame, text="multiplication / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)
        # multiplication text (label, row 1)
        self.multiplication_text = Label(self.multiplication_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.multiplication_text.grid(row=1)
        # dismiss button (row 2)
        self.dismiss_btn = Button(self.multiplication_frame, text="dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_multiplication, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_multiplication(self, partner):
        # Put  multiplication button back to normal...
        partner.multiplication_button.config(state=NORMAL)
        self.multiplication_box.destroy()
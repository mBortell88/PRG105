"""
This GUI program calculates the a car's gas mileage
With entry widgets the user can enter the number of gallons the car holds
and number of miles the car can drive on a full tank of gas
"""

import tkinter
import tkinter.font


class Mile_per_gal_GUI:

    def __init__(self):

        # create main window widget
        self.main_window = tkinter.Tk()

        # create canvas widget
        self.canvas = tkinter.Canvas(self.main_window, width=300, height=100)
        # self.canvas.configure(highlightthickness=0, borderwidth=0)

        # create font specifications
        myfont = tkinter.font.Font(family='Courier', size='10', weight='bold')

        # display text
        self.canvas.create_text(150, 40, fill='darkred', font=myfont, text="Miles per Gallon Calculator")

        # create frames to group widgets
        self.top_frame = tkinter.Frame()
        self.second_frame = tkinter.Frame()
        self.third_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # create top_frame widgets
        self.prompt_mi_label = tkinter.Label(self.top_frame, text="Enter the number of miles that can be driven on a full tank of gas: ")
        self.miles_entry = tkinter.Entry(self.top_frame, width=10)

        # pack the top_frame widgets
        self.prompt_mi_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # create the second_frame widgets
        self.prompt_gas_gal = tkinter.Label(self.second_frame, text="Enter the number of gallons in a full tank of gas: ")
        self.gas_gal_entry = tkinter.Entry(self.second_frame, width=10)

        # pack the second_frame widgets
        self.prompt_gas_gal.pack(side='left')
        self.gas_gal_entry.pack(side='left')

        # create the third_frame widgets
        self.descrip_label = tkinter.Label(self.third_frame, text="Converted miles per Gallon")
        # create the StringVar object to associate output label
        # use object set method to store string of blank characters
        self.mpg_value = tkinter.StringVar()
        # create label to associate with StringVar
        self.mpg_label = tkinter.Label(self.third_frame, textvariable=self.mpg_value)

        # pack third_frame widgets
        self.descrip_label.pack(side='left')
        self.mpg_label.pack(side='left')

        # create button widgets for bottom_frame
        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.calculate_mpg)
        self.exit_button = tkinter.Button(self.bottom_frame, text='Exit', command=self.main_window.destroy)

        # pack the button widgets
        self.calc_button.pack(side='left')
        self.exit_button.pack(side='left')

        # pack the canvas
        self.canvas.pack()

        # pack the frames
        self.top_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.bottom_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

        # calculate method is a callback function for Calculate button

    def calculate_mpg(self):
        # get values entered by user in entry widgets
        miles = float(self.miles_entry.get())
        gas_gallons = float(self.gas_gal_entry.get())

        # calculate by dividing miles by gallons
        mpg = miles / gas_gallons

        # convert to a string & store it in StringVar object
        # this will auto-update mpg_label widget
        self.mpg_value.set(mpg)

# create instance of MilesPerGal_GUI class/
calc_mpg = Mile_per_gal_GUI()

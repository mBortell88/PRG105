"""
this gui program has the user click the show_info button
the show info button will display my name and my school's
street address, city, state and zip code.
"""

import tkinter


class Name_Address:

    def __init__(self):

        # create the main window widget, root object
        self.main_window = tkinter.Tk()

        # StringVar object to display name, street, city, state & zip
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.cty_st_zp_value = tkinter.StringVar()

        # create frames to group widgets
        self.info_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        # create top frame widgets
        # labels to associate with StringVar object
        self.name_label = tkinter.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame, textvariable=self.street_value)
        self.cty_st_zp_label = tkinter.Label(self.info_frame, textvariable=self.cty_st_zp_value)

        # pack top frame widgets
        self.name_label.pack()
        self.street_label.pack()
        self.cty_st_zp_label.pack()

        # create button widgets
        self.show_info_button = tkinter.Button(self.button_frame, text='Show Info', command=self.show)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        # pack the buttons
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        # pack the frames
        self.info_frame.pack()
        self.button_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

    # callback function for the show_info_button
    def show(self):
        # set the variables to show in StringVar objects
        self.name_value.set('Maggie Bortell')
        self.street_value.set('8900 US Hwy 14')
        self.cty_st_zp_value.set('Crystal Lake, IL 60012')

# create instance of the Name_address class
show_name_address = Name_Address()

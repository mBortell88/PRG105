import tkinter
import tkinter.messagebox
import pickle

MY_FONT = ("System", 16)
SM_FONT = ("Verdana", 9)


def load_data():
        # use try/except for handling if file cannot be accessed
        try:
            input_file = open("directory.dat", 'rb')
            directory = pickle.load(input_file)  # accesses contents from file
        # use the IOError for file error
        except IOError:
            print("An error occurred trying to read/access the file.")
            directory = {}  # create empty directory
        return directory

contacts = load_data()


class MainWindow(tkinter.Tk):
    # MainWindow is the superclass
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title("Contact Information")  # title the window
        self.geometry('400x400')  # set size of main window

        # holds all the windows
        container = tkinter.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)  # row grid will cover the entire window
        container.grid_columnconfigure(0, weight=1)  # column grid will cover entire window

        self.frames = {}  # the windows navigate to

        for F in (MainMenu, LookUp, AddContact, Change, Modify, DeleteContact):  # for loop to navigate to windows
            frame = F(container, self)  # create the window
            self.frames[F] = frame  # store into frames
            frame.grid(row=0, column=0, sticky='nsew')  # grid to container

        self.show_frame(MainMenu)  # makes initial window the MainMenu

    def show_frame(self, x):  # x is the variable for the window
        frame = self.frames[x]
        frame.tkraise()


class MainMenu(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)  # inherits from parent Main_Window
        self.controller = controller
        menu_label = tkinter.Label(self, text='Main Menu', font=MY_FONT)
        menu_label.pack(pady=10, padx=10)  # centered

        # create labels for frames -
        # these will describe what each button does
        # and give instructions to the user

        instruct_label = tkinter.Label(self, text="\nPlease select a button with what you would like to do: ", font=SM_FONT)
        instruct_label.pack(side="top")

        # LOOKUP - label, buttons & packing them
        m_look_up_label = tkinter.Label(self, text="To search for a contact in the directory")
        m_look_up_button = tkinter.Button(self, text='Look-up', command=lambda: controller.show_frame(LookUp))
        m_look_up_label.pack()
        m_look_up_button.pack()

        #  ADD
        m_add_label = tkinter.Label(self, text="To add a new contact into the directory")
        m_add_button = tkinter.Button(self, text='Add New Contact', command=lambda: controller.show_frame(AddContact))
        m_add_label.pack()
        m_add_button.pack()

        # CHANGE
        m_change_label = tkinter.Label(self, text="To change or update a contact in the directory")
        m_change_button = tkinter.Button(self, text="Change/Update Contact", command=lambda: controller.show_frame(Change))
        m_change_label.pack()
        m_change_button.pack()

        # DELETE
        m_delete_label = tkinter.Label(self, text="To delete a contact from the contact directory")
        m_delete_button = tkinter.Button(self, text="Delete Contact", command=lambda: controller.show_frame(DeleteContact))
        m_delete_label.pack()
        m_delete_button.pack()

        #  create exit button and pack
        exit_button = tkinter.Button(self, text='Exit', command=lambda: save_exit())
        exit_button.pack()


class LookUp(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        lookup_label = tkinter.Label(self, text='Look-up Contact', font=MY_FONT)
        lookup_label.pack(pady=10, padx=10)

        # create description, label for entry & entry widget
        descrip_label = tkinter.Label(self, text="Look-up a contact in your directory", font=SM_FONT)
        look_up_label = tkinter.Label(self, text="Please Enter First Name to Locate Contact: ")
        look_up_entry = tkinter.Entry(self, width=25)
        descrip_label.pack()
        look_up_label.pack()

        # create button widgets
        look_up_button = tkinter.Button(self, text='Look-up', command=lambda: look_up())
        mm_button = tkinter.Button(self, text='Return to Main Menu', command=lambda: controller.show_frame(MainMenu))

        # pack entry and buttons
        look_up_entry.pack()
        look_up_button.pack()
        mm_button.pack()

        # call back function for look-up button
        def look_up():
            l_contact = look_up_entry.get().upper()
            if l_contact in contacts:
                result = contacts.get(l_contact)
                tkinter.messagebox.showinfo("Result", result)
            else:
                tkinter.messagebox.showinfo("Result", "Contact does not exist.")


class AddContact(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        add_label = tkinter.Label(self, text='Add New Contact', font=MY_FONT)
        add_label.pack(pady=10, padx=10)

        # create description, label for entry & entry widget
        a_descrip_label = tkinter.Label(self, text="Add a contact in your directory", font=SM_FONT)
        a_descrip_label.pack()
        # first name
        add_fname_label = tkinter.Label(self, text="Enter First Name: ")
        a_fname_entry = tkinter.Entry(self, width=25)
        add_fname_label.pack()
        a_fname_entry.pack()
        # last name
        add_lname_label = tkinter.Label(self, text="Enter Last Name: ")
        a_lname_entry = tkinter.Entry(self, width=25)
        add_lname_label.pack()
        a_lname_entry.pack()
        # residence address
        a_address_label = tkinter.Label(self, text="Enter Address: ")
        a_address_entry = tkinter.Entry(self, width=25)
        a_address_label.pack()
        a_address_entry.pack()
        # phone number
        add_phnum_label = tkinter.Label(self, text="Enter Phone Number: ")
        a_phnum_entry = tkinter.Entry(self, width=25)
        add_phnum_label.pack()
        a_phnum_entry.pack()
        # e-mail
        add_email_label = tkinter.Label(self, text="Enter E-mail: ")
        a_email_entry = tkinter.Entry(self, width=25)
        add_email_label.pack()
        a_email_entry.pack()

        # create button widgets & pack them
        add_button = tkinter.Button(self, text='Add', command=lambda: add_new())
        mm_button = tkinter.Button(self, text='Return to Main Menu', command=lambda: controller.show_frame(MainMenu))
        add_button.pack()
        mm_button.pack()

        # callback function for add button
        def add_new():
            a_name = a_fname_entry.get().upper()
            a_last = a_lname_entry.get().upper()
            a_address = a_address_entry.get().upper()
            a_phone = a_phnum_entry.get()
            a_email = a_email_entry.get().lower()

            if a_name not in contacts:
                contacts[a_name] = [a_last, a_address, a_phone, a_email]
                tkinter.messagebox.showinfo("Result", "Added to Contacts.")
            else:
                tkinter.messagebox.showinfo("Result", "Contact already exists.")


class Change(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        lookup_label = tkinter.Label(self, text='Look-up Contact to Update', font=MY_FONT)
        lookup_label.pack(pady=10, padx=10)

        # create description, label for entry & entry widget
        c_descrip_label = tkinter.Label(self, text="Change or Update a contact in your directory", font=SM_FONT)
        c_look_up_label = tkinter.Label(self, text="Please Enter First Name to Locate Contact: ")
        c_look_up_entry = tkinter.Entry(self, width=25)
        c_descrip_label.pack()
        c_look_up_label.pack()

        # create button widgets
        c_button = tkinter.Button(self, text='Look-up', command=lambda: c_look_up())
        c_mm_button = tkinter.Button(self, text='Return to Main Menu', command=lambda: controller.show_frame(MainMenu))

        # pack entry and buttons
        c_look_up_entry.pack()
        c_button.pack()
        c_mm_button.pack()

        # callback function for look-up button
        def c_look_up():
            c_contact = c_look_up_entry.get().upper()
            if c_contact in contacts:
                result = contacts.get(c_contact)
                tkinter.messagebox.showinfo("Result", result)
                controller.show_frame(Modify)  # Go to Modify window to make changes
            else:
                tkinter.messagebox.showinfo("Result", "Contact does not exist.")


class Modify(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        lookup_label = tkinter.Label(self, text='Update Contact Information', font=MY_FONT)
        lookup_label.pack(pady=10, padx=10)

        # first name
        c_fname_label = tkinter.Label(self, text="Enter First Name: ")
        c_fname_entry = tkinter.Entry(self, width=25)
        c_fname_label.pack()
        c_fname_entry.pack()
        # last name
        c_lname_label = tkinter.Label(self, text="Enter Last Name: ")
        c_lname_entry = tkinter.Entry(self, width=25)
        c_lname_label.pack()
        c_lname_entry.pack()
        # residence address
        c_address_label = tkinter.Label(self, text="Enter Address: ")
        c_address_entry = tkinter.Entry(self, width=25)
        c_address_label.pack()
        c_address_entry.pack()
        # phone number
        c_phnum_label = tkinter.Label(self, text="Enter Phone Number: ")
        c_phnum_entry = tkinter.Entry(self, width=25)
        c_phnum_label.pack()
        c_phnum_entry.pack()
        # e-mail
        c_email_label = tkinter.Label(self, text="Enter E-mail: ")
        c_email_entry = tkinter.Entry(self, width=25)
        c_email_label.pack()
        c_email_entry.pack()

        mod_button = tkinter.Button(self, text='Modify', command=lambda: modify())
        mod_button.pack()
        m_mm_button = tkinter.Button(self, text='Return to Main Menu', command=lambda: controller.show_frame(MainMenu))
        m_mm_button.pack()

        # callback function for modify button
        def modify():
            c_name = c_fname_entry.get().upper()
            c_last = c_lname_entry.get().upper()
            c_address = c_address_entry.get().upper()
            c_phone = c_phnum_entry.get()
            c_email = c_email_entry.get().lower()

            contacts[c_name] = [c_last, c_address, c_phone, c_email]
            tkinter.messagebox.showinfo("Result", "Modified Contact.")


class DeleteContact(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        lookup_label = tkinter.Label(self, text='Delete Contact', font=MY_FONT)
        lookup_label.pack(pady=10, padx=10)

        # create description, label for entry & entry widget
        d_descrip_label = tkinter.Label(self, text="Look-up a Contact to Delete", font=SM_FONT)
        d_look_up_label = tkinter.Label(self, text="Please Enter First Name to Locate Contact: ")
        d_look_up_entry = tkinter.Entry(self, width=25)
        d_descrip_label.pack()
        d_look_up_label.pack()

        # create button widgets
        d_button = tkinter.Button(self, text='Delete', command=lambda: delete_contact())
        d_mm_button = tkinter.Button(self, text='Return to Main Menu', command=lambda: controller.show_frame(MainMenu))

        # pack entry and buttons
        d_look_up_entry.pack()
        d_button.pack()
        d_mm_button.pack()

        # call back function for delete button
        def delete_contact():
            d_contact = d_look_up_entry.get().upper()
            if d_contact in contacts:
                del contacts[d_contact]
                tkinter.messagebox.showinfo("Result", "Contact Deleted.")
            else:
                tkinter.messagebox.showinfo("Result", "Contact does not exist.")


def save_exit():
    # open the directory file again for writing and set to variable
    with open('directory.dat', 'wb') as save_file:
        pickle.dump(contacts, save_file)
        save_file.close()
        tkinter.messagebox.showinfo('Contact Information', "Data Saved Successfully")
        app.destroy()

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()

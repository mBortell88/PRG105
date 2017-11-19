"""
this GUI program allows the user to select options from a list of
10 products from a coffee & tea shop.
The total will be calculated and displayed on the bottom
"""

import tkinter
import tkinter.font
import tkinter.messagebox
import products_prices


class Coffee_Tea:

    def __init__(self):
        # create the main window widget
        self.main_window = tkinter.Tk()
        self.main_window.minsize(600, 400)
        self.main_window.configure(background='saddle brown')

        # create instances of products_prices
        self.opt1 = products_prices.Products_prices("Dark Roast Coffee", "Dark color, bitter, smokey taste", 1, 13.99)
        self.opt2 = products_prices.Products_prices("Medium Roast Coffee", "Medium color, balanced flavor and aroma", 1, 13.99)
        self.opt3 = products_prices.Products_prices("Light Roast", "Light color, toasted grain taste", 1, 13.99)
        self.opt4 = products_prices.Products_prices("Green Tea", "Healthy, organic with a floral taste", 1, 11.99)
        self.opt5 = products_prices.Products_prices("Chai Tea", "Tea with aromatic Indian spices, and herbs", 1, 11.99)
        self.opt6 = products_prices.Products_prices("Black Tea", "Organic, Strong flavour", 1, 11.99)
        self.opt7 = products_prices.Products_prices("Oolong Tea", "Organic, traditional Chinese tea", 1, 11.99)
        self.opt8 = products_prices.Products_prices("Chamomile Tea", "Organic, fragrant, herbal tea", 1, 11.99)
        self.opt9 = products_prices.Products_prices("White Tea", "Light and sweet flavor", 1, 11.99)

        # create canvas widget
        self.canvas = tkinter.Canvas(self.main_window, width=600, height=80, background='lemon chiffon')

        # create font specifications
        myfont = tkinter.font.Font(family='Verdana', size='24', weight='bold', slant='italic')

        # display text
        self.canvas.create_text(275, 40, fill='darkblue', font=myfont, text="Coffee & Tea Shoppe")

        # pack the canvas
        self.canvas.pack()

        # create frames to group widgets
        self.instruct_frame = tkinter.Frame()
        self.f1_frame = tkinter.Frame()
        self.f2_frame = tkinter.Frame()
        self.f3_frame = tkinter.Frame()
        self.f4_frame = tkinter.Frame()
        self.f5_frame = tkinter.Frame()
        self.buttons_frame = tkinter.Frame()

        # create instructions label
        self.instruct_label = tkinter.Label(self.instruct_frame, text="\nClick the check boxes to select the product you wish to purchase. \nWhen completed, select the total button to see your total.\n")

        # create IntVar objects
        self.opt1_var1 = tkinter.IntVar()
        self.opt2_var2 = tkinter.IntVar()
        self.opt3_var3 = tkinter.IntVar()
        self.opt4_var4 = tkinter.IntVar()
        self.opt5_var5 = tkinter.IntVar()
        self.opt6_var6 = tkinter.IntVar()
        self.opt7_var7 = tkinter.IntVar()
        self.opt8_var8 = tkinter.IntVar()
        self.opt9_var9 = tkinter.IntVar()

        # set IntVar objects to 0
        self.opt1_var1.set(0)
        self.opt2_var2.set(0)
        self.opt3_var3.set(0)
        self.opt4_var4.set(0)
        self.opt5_var5.set(0)
        self.opt6_var6.set(0)
        self.opt7_var7.set(0)
        self.opt8_var8.set(0)
        self.opt9_var9.set(0)

        # create add buttons
        self.opt1_cb = tkinter.Checkbutton(self.f1_frame, text="Product: " + self.opt1.get_product() + '\nDescription: ' + self.opt1.get_prod_description() + '\nQuantity: ' + str(self.opt1.get_quantity()) + 'lbs' + '\nPrice: $' + str(self.opt1.get_price()), variable=self.opt1_var1, justify='left')
        self.opt2_cb = tkinter.Checkbutton(self.f1_frame, text="Product: " + self.opt2.get_product() + '\nDescription: ' + self.opt2.get_prod_description() + '\nQuantity: ' + str(self.opt2.get_quantity()) + 'lbs' + '\nPrice: $' + str(self.opt2.get_price()), variable=self.opt2_var2, justify='left')
        self.opt3_cb = tkinter.Checkbutton(self.f2_frame, text="Product: " + self.opt3.get_product() + '\nDescription: ' + self.opt3.get_prod_description() + '\nQuantity: ' + str(self.opt3.get_quantity()) + 'lbs' + '\nPrice: $' + str(self.opt3.get_price()), variable=self.opt3_var3, justify='left')
        self.opt4_cb = tkinter.Checkbutton(self.f3_frame, text="Product: " + self.opt4.get_product() + '\nDescription: ' + self.opt4.get_prod_description() + '\nQuantity: ' + str(self.opt4.get_quantity()) + ' carton' + '\nPrice: $' + str(self.opt4.get_price()), variable=self.opt4_var4, justify='left')
        self.opt5_cb = tkinter.Checkbutton(self.f3_frame, text="Product: " + self.opt5.get_product() + '\nDescription: ' + self.opt5.get_prod_description() + '\nQuantity: ' + str(self.opt4.get_quantity()) + ' carton' + '\nPrice: $' + str(self.opt5.get_price()), variable=self.opt5_var5, justify='left')
        self.opt6_cb = tkinter.Checkbutton(self.f4_frame, text="Product: " + self.opt6.get_product() + '\nDescription: ' + self.opt6.get_prod_description() + '\nQuantity: ' + str(self.opt6.get_quantity()) + ' carton' + '\nPrice: $' + str(self.opt6.get_price()), variable=self.opt6_var6, justify='left')
        self.opt7_cb = tkinter.Checkbutton(self.f4_frame, text="Product: " + self.opt7.get_product() + '\nDescription: ' + self.opt7.get_prod_description() + '\nQuantity: ' + str(self.opt7.get_quantity()) + ' carton' + '\nPrice: $' + str(self.opt7.get_price()), variable=self.opt7_var7, justify='left')
        self.opt8_cb = tkinter.Checkbutton(self.f5_frame, text="Product: " + self.opt8.get_product() + '\nDescription: ' + self.opt8.get_prod_description() + '\nQuantity: ' + str(self.opt8.get_quantity()) + ' carton' + '\nPrice: $' + str(self.opt8.get_price()), variable=self.opt8_var8, justify='left')
        self.opt9_cb = tkinter.Checkbutton(self.f5_frame, text="Product: " + self.opt9.get_product() + '\nDescription: ' + self.opt9.get_prod_description() + '\nQuantity: ' + str(self.opt9.get_quantity()) + ' carton' + '\nPrice: $' + str(self.opt9.get_price()), variable=self.opt9_var9, justify='left')

        # pack the instructions label
        self.instruct_label.pack()

        # pack top frame widgets
        self.opt1_cb.pack(anchor='e', side='left')
        self.opt2_cb.pack(anchor='w', side='right')
        self.opt3_cb.pack()
        self.opt4_cb.pack(anchor='e', side='left')
        self.opt5_cb.pack(anchor='w', side='right')
        self.opt6_cb.pack(anchor='e', side='left')
        self.opt7_cb.pack(anchor='w', side='right')
        self.opt8_cb.pack(anchor='e', side='left')
        self.opt9_cb.pack(anchor='w', side="right")

        # create button widgets
        self.total_button = tkinter.Button(self.buttons_frame, text='Total', command=self.purchase_total)
        self.quit_button = tkinter.Button(self.buttons_frame, text='Quit', command=self.main_window.destroy)

        # pack the buttons
        self.total_button.pack(side='left')
        self.quit_button.pack(side='right')

        # pack the frames
        self.instruct_frame.pack()
        self.f1_frame.pack(anchor='w')
        self.f2_frame.pack(anchor='w')
        self.f3_frame.pack(anchor='w')
        self.f4_frame.pack(anchor='w')
        self.f5_frame.pack(anchor='w')
        self.buttons_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

    # create the purchase total callback function
    def purchase_total(self):
        total_amt = 0
        if self.opt1_var1.get() == 1:
            total_amt += self.opt1.get_price()
        if self.opt2_var2.get() == 1:
            total_amt += self.opt2.get_price()
        if self.opt3_var3.get() == 1:
            total_amt += self.opt3.get_price()
        if self.opt4_var4.get() == 1:
            total_amt += self.opt4.get_price()
        if self.opt5_var5.get() == 1:
            total_amt += self.opt5.get_price()
        if self.opt6_var6.get() == 1:
            total_amt += self.opt6.get_price()
        if self.opt7_var7.get() == 1:
            total_amt += self.opt7.get_price()
        if self.opt8_var8.get() == 1:
            total_amt += self.opt8.get_price()
        if self.opt9_var9.get() == 1:
            total_amt += self.opt9.get_price()

        # convert the integer into a string
        total_print = str(total_amt)
        # display in a message box the total
        tkinter.messagebox.showinfo('Total', "The total purchase is $" + total_print)

# create instance of the Coffee_Tea class and call
coffee = Coffee_Tea()

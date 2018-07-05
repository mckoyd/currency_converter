from tkinter import *
from currency_converter import *

root = Tk()

# top_frame = Frame(root)
# top_frame.pack()
# bottom_frame = Frame(root)
# bottom_frame.pack(side=BOTTOM)

# button1 = Button(top_frame, text='Button 1', fg='red')
# button2 = Button(top_frame, text='Button 2', fg='blue')
# button3 = Button(top_frame, text='Button 3', fg='green')
# button4 = Button(bottom_frame, text='Button 4', fg='purple')

# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)

currency_name_label = Label(root, text='Enter currency name')
currency_name_input = Entry(root)
currency_name_label.grid(row=1, sticky=E)
currency_name_input.grid(row=1, column=1)

currency_amount_label = Label(root, text='Enter amount to convert')
currency_amount_input = Entry(root)
currency_amount_label.grid(row=2, sticky=E)
currency_amount_input.grid(row=2, column=1)


def get_values():
  name = currency_name_input.get()
  amount = float(currency_amount_input.get())
  amount_in_US = convert_to_source('USD', name, amount)
  amount_outside_US = convert_from_source('USD', name, amount)
  print(f'Amount converted to {name} is {amount_in_US} \nAmount converted from {name} is {amount_outside_US}')


convert_button = Button(root, text='CONVERT IT!', width=20, padx=5, command=get_values)
convert_button.grid(row=3, columnspan=2)



root.mainloop()
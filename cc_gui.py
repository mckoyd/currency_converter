from currency_converter import *
from tkinter import *


class Window(Frame):
  def __init__(self, master):
    Frame.__init__(self, master)
    self.master = master
    self.init_window()
  
  def init_window(self):
    self.master.title('Counting Money with The Real McKoy')
    self.grid()

    self.nav = Menu(self.master)
    self.master.config(menu=self.nav)
    self.file = Menu(self.nav)
    self.file.add_command(label='Exit', command=self.quit)
    self.nav.add_cascade(label='File', menu=self.file)
    self.sources = Menu(self.nav)
    CURRENCY_ABBREVIATIONS = Currency('list', 'USD').get_data()['currencies']
    for abbr in CURRENCY_ABBREVIATIONS:
      menu_label = f'{abbr} - {CURRENCY_ABBREVIATIONS[abbr]}'
      self.sources.add_command(label=menu_label, command=lambda text=menu_label: self.insert_source(text))
    self.nav.add_cascade(label='View Sources', menu=self.sources)

    heading = 'Counting Money with the Real McKoy'
    Label(self, text=heading).grid(row=0, columnspan=2, pady=15)

    self.currency_source_label = Label(self, text='Enter country source (ex: USD)')
    self.currency_source_input = Entry(self)
    self.currency_source_label.grid(row=1, sticky=E)
    self.currency_source_input.grid(row=1, column=1)
    self.currency_name_label = Label(self, text='Enter currency name')
    self.currency_name_input = Entry(self)
    self.currency_name_label.grid(row=2, sticky=E)
    self.currency_name_input.grid(row=2, column=1)
    self.currency_amount_label = Label(self, text='Enter amount to convert')
    self.currency_amount_input = Entry(self)
    self.currency_amount_label.grid(row=3, sticky=E)
    self.currency_amount_input.grid(row=3, column=1)

    self.convert_button = Button(self, text='CONVERT IT!', width=15, padx=5, 
    fg='green', command=self.conversion_display)
    
    self.convert_button.grid(row=4, columnspan=2, pady=15)

    self.dark_theme_button = Button(self, text='DARK THEME',
    width=15, padx=5, fg='green', command=self.get_dark_theme)
    self.dark_theme_button.grid(row=5, columnspan=2)
  
  def get_conversion(self):
    source = self.currency_source_input.get()
    name = self.currency_name_input.get()
    amount = float(self.currency_amount_input.get())
    amount_in_US = convert_to_source(source, name, amount)
    amount_outside_US = convert_from_source(source, name, amount)
    return f'Amount converted to {name} is {amount_in_US} \nAmount converted from {name} is {amount_outside_US}'

  def conversion_display(self):
    results = self.get_conversion()
    results_view = Text(self)
    results_view.grid(row=6, columnspan=2)
    results_view.tag_configure('center', justify='center')
    results_view.insert(END, results)
    results_view.tag_add("center", "1.0", "end")


  def insert_source(self, text):
    if (self.currency_source_input.get()):
      self.currency_source_input.delete(0, 'end')
      self.currency_source_input.insert(0, self.sources.entrycget(self.sources.index(text), 'label')[:3])
    else:
      self.currency_source_input.insert(0, self.sources.entrycget(self.sources.index(text), 'label')[:3])

  def get_dark_theme(self):
    self.master.tk_setPalette(background='#000')


root = Tk()
app = Window(root)
root.mainloop()
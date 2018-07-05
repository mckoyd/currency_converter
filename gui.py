from tkinter import *

class Window(Frame):
  def __init__(self, master):
    Frame.__init__(self, master)
    self.master = master
    self.init_window()
  
  def init_window(self):
    self.master.title('Counting Money with The Real McKoy')
    self.pack(fill=BOTH, expand=1)

    # Making a menu bar
    # Start with the actual menu bar using Menu
    nav = Menu(self.master)
    self.master.config(menu=nav)
    
    # Attach a menu onto the menu bar (ex here is File)
    file = Menu(nav)
    # Construct the commands for this particular option
    # ex here is to exit the program
    file.add_command(label='Exit', command=self.close_program)
    # Add the file menu to the main menu
    nav.add_cascade(label='File', menu=file)



    # quitButton = Button(self, text='Close', command=self.close_program)
    # quitButton.place(x=0, y=0)
  
  def close_program(self):
    exit()


root = Tk()
root.geometry('400x300')
app = Window(root)
root.mainloop()
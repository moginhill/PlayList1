from tkinter import *
from tkinter import messagebox

class GuiTesting:

    def __init__(self, master):
        self.master = master
        master.title('Testing Window')

        self.tLabel = Label(master, text='First TextBox')
        self.tLabel.grid(row=0, column=0, columnspan=1)
        self.text = Text(master, height=1)
        self.text.grid(row=0, column=1, columnspan=2)

        messagebox.askyesno('Would you like to continue on your last playlist')

        self.greeter = Button(master, text='Add', command=self.greet)
        self.greeter.grid(row=5, column=0, columnspan=2)


    def greet(self):
        print('you pressed a button')


#outside of class def
root = Tk()
gui = GuiTesting(root)
root.mainloop()
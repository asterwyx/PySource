import tkinter.messagebox as messagebox
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.name_input = Entry(self)
        self.name_input.pack()
        self.alter_button = Button(self, text="Hello", command=self.hello)
        self.alter_button.pack()

    def hello(self):
        name = self.name_input.get() or "world"
        messagebox.showinfo('Message', "Hello, %s" % name)


if __name__ == '__main__':
    app = Application()  # 实例化
    app.master.title("Hello, world")
    app.mainloop()

from tkinter import *


class Application(Frame):  # 从Frame派生一个Application类，这是所有Widget的父容器
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello_label = Label(self, text="Hello, world!")
        self.hello_label.pack()
        self.quit_button = Button(self, text="Quit", command=self.quit)
        self.quit_button.pack()


app = Application()  # 实例化Application
app.master.title("Hello, world")  # 设置主窗口标题
app.mainloop()  # 打开主消息循环

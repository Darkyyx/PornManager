import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox


class Application (tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.show_widget()

    def show_widget(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "测试正常信息"
        self.hi_there["command"] = self.show_info
        self.hi_there.pack(side="top")

        self.hi_error = tk.Button(self)
        self.hi_error['text'] = "测试错误信息"
        self.hi_error["command"] = self.show_error
        self.hi_error.pack(side="top")

        self.hi_waring = tk.Button(self)
        self.hi_waring['text'] = "测试警告信息"
        self.hi_waring["command"] = self.show_warning
        self.hi_waring.pack(side="top")

        self.input_field = Entry(self)
        self.input_field.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")

    def show_error(self):
        messagebox.showerror('Error', '错误')

    def show_warning(self):
        messagebox.showwarning('Warning', '警告')

    def show_info(self):
        messagebox.showinfo('Info', '正常')

root = tk.Tk()
app = Application(master=root)
app.master.title("AVMS")
app.master.minsize(800, 600)
app.master.maxsize(1920, 1080)
app.mainloop()

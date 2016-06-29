# -*- coding: utf-8 -*-

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
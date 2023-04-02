#make a tkinter gui
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import subprocess
import time

#make a class for the gui
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Test")
        self.geometry("500x500")
        self.resizable(0,0)
        self.configure(bg="white")
        self.create_widgets()

    def create_widgets(self):
        self.button1 = ttk.Button(self, text="Test", command=self.test)
        self.button1.place(x=100, y=100)

    def test(self):
        print("test")

if __name__ == "__main__":
    app = App()
    app.mainloop()
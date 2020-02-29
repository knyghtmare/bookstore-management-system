#!/usr/bin/env python3
import sys
from tkinter import *
from tkinter.ttk import *
from src_dir.frontend import Application
import src_dir.backend


if __name__ == "__main__":
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry("500x450")
    # preventing a resize
    # root.resizable(False, False)


    # instantiate the class
    app = Application(master=root)
    # loop it
    app.mainloop()
    # destroy it once you
    # are done
    root.destroy()

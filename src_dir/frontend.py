from tkinter import *
from tkinter.ttk import *
from src_dir.backend import (view_entries, update_entry,
                             delete_entry, insert_entry,
                             search_entry)
import src_dir.backend


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # the variables
        self.title_text = StringVar()
        self.author_text = StringVar()
        self.selected_tuple = IntVar()
        self.isbn_int = IntVar()
        self.price_int = IntVar()
        self.id_int = IntVar()
        self.setup_all()

    def view_command(self):
        self.list1.delete(0, END)
        for row in view_entries():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in search_entry(
            self.title_text.get(),
            self.author_text.get(),
            self.price_int.get(),
            self.isbn_int.get()
            ):
            self.list1.insert(END,row)

    def add_command(self):
        insert_entry(
            self.id_int.get(),
            self.title_text.get(),
            self.author_text.get(),
            self.price_int.get(),
            self.isbn_int.get()
        )
        list1.delete(0, END)
        list1.insert(
            END,
            (self.id_int.get(),
            self.title_text.get(),
            self.author_text.get(),
            self.price_int.get(),
            self.isbn_int.get())
        )

    def get_selected_row(self, event):
        self.index = self.list1.curselection()[0]
        self.selected_tuple = self.list1.get(index)
        self.e1.delete(0, END)
        self.e1.insert(END, self.selected_tuple[1])
        self.e2.delete(0, END)
        self.e2.insert(END, self.selected_tuple[2])
        self.e3.delete(0, END)
        self.e3.insert(END, self.selected_tuple[3])
        self.e4.delete(0, END)
        self.e4.insert(END, self.selected_tuple[4])
        self.e5.delete(0, END)
        self.e5.insert(END, self.selected_tuple[0])

    def update_command(self):
        update_entry(
            self.id_int.get(),
            self.title_text.get(),
            self.author_text.get(),
            self.price_int.get(),
            self.isbn_int.get()
            )

    def delete_command(self):
        delete_entry(self.selected_tuple[0])

    def setup_all(self):
        # the labels
        self.label1 = Label(self.master, text="Title", width=12)
        self.label1.grid(row=0, column=0)
        self.label2 = Label(self.master, text="Author", width=12)
        self.label2.grid(row=0, column=2)
        self.label3 = Label(self.master, text="Price", width=12)
        self.label3.grid(row=1, column=0)
        self.label4 = Label(self.master, text="ISBN", width=12)
        self.label4.grid(row=1, column=2)
        self.label5 = Label(self.master, text="Book ID", width=12)
        self.label5.grid(row=2, column=0)
        # entry fields
        self.e1 = Entry(self.master, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)
        self.e2 = Entry(self.master, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)
        self.e3 = Entry(self.master, textvariable=self.price_int)
        self.e3.grid(row=1, column=1)
        self.e4 = Entry(self.master, textvariable=self.isbn_int)
        self.e4.grid(row=1, column=3)
        self.e5 = Entry(self.master, textvariable=self.id_int)
        self.e5.grid(row=2, column=1)
        # listbox
        self.list1 = Listbox(self.master, height=6, width=36)
        self.list1.grid(row=3, column=0, rowspan=6, columnspan=2)
        # scrollbar
        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=2, rowspan=6)
        self.list1.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.list1.yview)
        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)
        # buttons
        self.button1 = Button(self.master, text="View All", width=12, command=self.view_command)
        self.button1.grid(row=3, column=3)
        self.button2 = Button(self.master, text="Search Entry", width=12, command=self.search_command)
        self.button2.grid(row=4, column=3)
        self.button3 = Button(self.master, text="Add Entry", width=12, command=self.add_command)
        self.button3.grid(row=5, column=3)
        self.button4 = Button(self.master, text="Update Entry", width=12, command=self.update_command)
        self.button4.grid(row=6, column=3)
        self.button5 = Button(self.master, text="Delete Entry", width=12, command=self.delete_command)
        self.button5.grid(row=7, column=3)
        self.button6 = Button(self.master, text="Close App", width=12, command=self.quit)
        self.button6.grid(row=8, column=3)

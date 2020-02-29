import random
from PySide2 import QtCore, QtWidgets, QtGui
from src_dir.backend import *

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.width = 400
        self.height = 450
        self.init_widgets()
        self.init_layout()

    def init_widgets(self):
        # labels
        self.bookTitle = QtWidgets.QLabel("Book Title")
        self.bookTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.bookAuthor = QtWidgets.QLabel("Book Author")
        self.bookAuthor.setAlignment(QtCore.Qt.AlignCenter)
        self.bookPrice = QtWidgets.QLabel("Book Price")
        self.bookPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.bookISBN = QtWidgets.QLabel("ISBN")
        self.bookISBN.setAlignment(QtCore.Qt.AlignCenter)
        # entry fields
        self.bookTitleEntry = QtWidgets.QLineEdit("Enter book Title")
        self.bookAuthorEntry = QtWidgets.QLineEdit("Enter Author name")
        self.bookPriceEntry = QtWidgets.QLineEdit("Enter Price")
        self.bookISBNEntry = QtWidgets.QLineEdit("Enter ISBN")
        # buttons
        self.buttonOne = QtWidgets.QPushButton("View All Books")
        self.buttonTwo = QtWidgets.QPushButton("Search for Book")
        self.buttonThree = QtWidgets.QPushButton("Add a Book")
        self.buttonFour = QtWidgets.QPushButton("Update a Book")
        self.buttonFive = QtWidgets.QPushButton("Remove a Book")
        self.buttonSix = QtWidgets.QPushButton("Exit the App")
        # listbox
        self.listbox = QtWidgets.QListWidget()
        return self

    def init_layout(self):
        self.layout = QtWidgets.QGridLayout()
        # labels
        self.layout.addWidget(self.bookTitle, 0, 0)
        self.layout.addWidget(self.bookAuthor, 1, 0)
        self.layout.addWidget(self.bookPrice, 2, 0)
        self.layout.addWidget(self.bookISBN, 3, 0)
        # entry fields
        self.layout.addWidget(self.bookTitleEntry, 0, 1)
        self.layout.addWidget(self.bookAuthorEntry, 1, 1)
        self.layout.addWidget(self.bookPriceEntry, 2, 1)
        self.layout.addWidget(self.bookISBNEntry, 3, 1)

        self.setLayout(self.layout)
        return self

    def init_events(self):
        # self.button.clicked.connect(self.magic)
        pass

    # def magic(self):
    #    self.text.setText(random.choice(self.hello))

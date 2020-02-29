import sys
from PySide2 import QtCore, QtWidgets, QtGui
from src_dir.frontend import MyWidget


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())

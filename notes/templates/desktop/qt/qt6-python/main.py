#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt6 import QtWidgets
from gui import Gui
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wnd = Gui()
    wnd.show()
    sys.exit(app.exec())


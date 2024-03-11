#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QApplication
from gui import Gui
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Gui()
    wnd.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow,QMessageBox
from Ui_gui import Ui_Gui

class Gui(QMainWindow,Ui_Gui):
    def __init__(self, parent=None):
        super(Gui, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(200,100);

    @Slot()
    def on_btnMsg_clicked(self):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle("Template")
        msgbox.setText("Template Qt PySide")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec()

    @Slot()
    def on_btnQuit_clicked(self):
        sys.exit()


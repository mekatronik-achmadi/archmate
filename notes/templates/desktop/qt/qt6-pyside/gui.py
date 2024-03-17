# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QMainWindow,QMessageBox
from ui_gui import Ui_Gui

class Gui(QMainWindow,Ui_Gui):
    def __init__(self, parent=None):
        super(Gui, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(200,100)

        self.btnMsg.clicked.connect(self.btnMsg_clicked)
        self.btnQuit.clicked.connect(self.btnQuit_clicked)

    def btnMsg_clicked(self):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle("Template")
        msgbox.setText("Template Qt PySide")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec()

    def btnQuit_clicked(self):
        sys.exit()


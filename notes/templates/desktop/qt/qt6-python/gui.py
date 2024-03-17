# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Ui_gui import Ui_Gui
import sys

class Gui(QMainWindow,Ui_Gui):

    def __init__(self,parent=None):
        super(Gui, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(200, 100)

        self.btnMsg.clicked.connect(self.btnMsg_clicked)
        self.btnQuit.clicked.connect(self.btnQuit_clicked)

    def btnMsg_clicked(self):
       msgBox = QMessageBox()
       msgBox.setIcon(QMessageBox.Icon.Information)
       msgBox.setWindowTitle("Template")
       msgBox.setText("Template Python Qt")
       msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
       msgBox.exec()

    def btnQuit_clicked(self):
        sys.exit()


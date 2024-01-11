# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from Ui_gui import Ui_Gui
import sys

class Gui(QMainWindow,Ui_Gui):

    def __init__(self,parent=None):
        super(Gui, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(200, 100)

    @pyqtSlot()
    def on_btnMsg_clicked(self):
       msgBox = QMessageBox()
       msgBox.setIcon(QMessageBox.Information)
       msgBox.setWindowTitle("Template")
       msgBox.setText("Template Python Qt")
       msgBox.setStandardButtons(QMessageBox.Ok)
       msgBox.exec()

    @pyqtSlot()
    def on_btnQuit_clicked(self):
        sys.exit()


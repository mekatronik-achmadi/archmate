#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import sys

from Ui_appGui import frmMain

class MainGui(frmMain):
    def __init__(self,parent=None):
        super().__init__(parent)

    def on_btnMsg_clicked(self,event):
        wx.MessageBox("Template C++ wxGTK","Template",wx.ICON_INFORMATION)

    def on_btnQuit_clicked( self, event ):
        sys.exit()

if __name__ == "__main__":
    app = wx.App()

    gui = MainGui()
    gui.Show()

    app.MainLoop()

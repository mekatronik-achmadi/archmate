#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import sys

from Ui_appGui import frmMain

class MainGui(frmMain):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.mBtnMsg.Bind(wx.EVT_BUTTON, self.btnMsg_clicked)
        self.mBtnQuit.Bind(wx.EVT_BUTTON,self.btnQuit_clicked)

    def btnMsg_clicked(self,event):
        wx.MessageBox("Template C++ wxGTK","Template",wx.ICON_INFORMATION)

    def btnQuit_clicked( self, event ):
        sys.exit()

if __name__ == "__main__":
    app = wx.App()

    gui = MainGui()
    gui.Show()

    app.MainLoop()

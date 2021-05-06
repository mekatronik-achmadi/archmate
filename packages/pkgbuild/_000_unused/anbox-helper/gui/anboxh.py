#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtCore, QtWidgets
from anboxh_ui import Ui_WinAnboxH

class AnboxH_main(QtWidgets.QMainWindow):
    def __init__ (self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_WinAnboxH()
        self.ui.setupUi(self)
        
        self.ui.btnFM.clicked.connect(self.file_fm)
        self.ui.btnSend.clicked.connect(self.file_send)
        self.ui.btnScan.clicked.connect(self.file_scan)
        self.ui.btnBrowse.clicked.connect(self.open_send)
        self.ui.btnReset.clicked.connect(self.reset_send)
        self.ui.btnMgr.clicked.connect(self.session_mgr)
        self.ui.btnStop.clicked.connect(self.session_stop)
        self.ui.btnStart.clicked.connect(self.session_start)

    def file_fm(self):
        bashcmd="anbox launch --action=android.intent.action.MAIN --package=com.android.documentsui --component=com.android.documentsui.FilesActivity --uri=content://com.android.externalstorage.documents/root/primary --type=vnd.android.document/root"
        os.system(bashcmd)

    def file_send(self):
        localfile= str(self.ui.txtLocal.text())
        if not localfile:
            return
        remotepath = str(self.ui.txtRemote.text())
        if not remotepath:
            return

        bashcmd="anbox-push"
        bashcmd+=" "
        bashcmd+=localfile
        bashcmd+=" "
        bashcmd+=remotepath

        os.system(bashcmd)

    def file_scan(self):
        localfile= str(self.ui.txtLocal.text())
        if not localfile:
            return
            
        remotepath = str(self.ui.txtRemote.text())
        if not remotepath:
            return

        bashcmd="anbox-scan"
        bashcmd+=" "
        bashcmd+=localfile
        bashcmd+=" "
        bashcmd+=remotepath

        os.system(bashcmd)

    def open_send(self):
        fileName,_=QtWidgets.QFileDialog.getOpenFileName(self,"Select File")
        if not fileName:
            return
        self.ui.txtLocal.setText(fileName)

    def reset_send(self):
        self.ui.txtRemote.setText("/sdcard/")

    def session_mgr(self):
        bashcmd="anbox launch --package=org.anbox.appmgr --component=org.anbox.appmgr.AppViewActivity"
        os.system(bashcmd)

    def session_start(self):
        bashcmd="anbox-start"
        os.system(bashcmd)

    def session_stop(self):
        bashcmd="anbox-stop"
        os.system(bashcmd)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_main_app = AnboxH_main()
    my_main_app.show()
    sys.exit(app.exec_())

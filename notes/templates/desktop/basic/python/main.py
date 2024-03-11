#!/usr/bin/python
# -*- coding: utf-8 -*-

class Template():

    def __init__(self):
        self.strMsg = "Template Python"

    def showMsg(self):
        print(self.strMsg)

if __name__ == "__main__":
    app = Template()
    app.showMsg()


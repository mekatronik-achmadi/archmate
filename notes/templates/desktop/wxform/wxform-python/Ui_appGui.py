# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frmMain
###########################################################################

class frmMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 250,150 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bMain = wx.BoxSizer( wx.VERTICAL )

		self.txtTitle = wx.StaticText( self, wx.ID_ANY, u"Template WxWidget", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.txtTitle.Wrap( -1 )

		bMain.Add( self.txtTitle, 1, wx.ALL|wx.EXPAND, 5 )

		self.mBtnMsg = wx.Button( self, wx.ID_ANY, u"Message", wx.DefaultPosition, wx.DefaultSize, 0 )
		bMain.Add( self.mBtnMsg, 1, wx.ALL|wx.EXPAND, 5 )

		self.mBtnQuit = wx.Button( self, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bMain.Add( self.mBtnQuit, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bMain )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass



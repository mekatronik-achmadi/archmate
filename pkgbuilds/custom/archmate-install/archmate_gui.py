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
## Class frmArchInstall
###########################################################################

class frmArchInstall ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Arch Linux Mate Install", pos = wx.DefaultPosition, size = wx.Size( 640,420 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 640,420 ), wx.DefaultSize )

		bMain = wx.BoxSizer( wx.HORIZONTAL )


		bMain.Add( ( 5, 0), 0, wx.EXPAND, 5 )

		bInstall = wx.BoxSizer( wx.VERTICAL )

		sbHostUser = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Host and Name" ), wx.VERTICAL )

		bHost = wx.BoxSizer( wx.HORIZONTAL )

		self.m_lblHost = wx.StaticText( sbHostUser.GetStaticBox(), wx.ID_ANY, u"Hostname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblHost.Wrap( -1 )

		bHost.Add( self.m_lblHost, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_txtHost = wx.TextCtrl( sbHostUser.GetStaticBox(), wx.ID_ANY, u"archmate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bHost.Add( self.m_txtHost, 1, wx.ALL, 5 )


		sbHostUser.Add( bHost, 1, wx.EXPAND, 5 )

		bUser = wx.BoxSizer( wx.HORIZONTAL )

		self.m_lblUser = wx.StaticText( sbHostUser.GetStaticBox(), wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblUser.Wrap( -1 )

		bUser.Add( self.m_lblUser, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_txtUser = wx.TextCtrl( sbHostUser.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bUser.Add( self.m_txtUser, 1, wx.ALL, 5 )


		sbHostUser.Add( bUser, 1, wx.EXPAND, 5 )


		bInstall.Add( sbHostUser, 0, wx.EXPAND, 5 )


		bInstall.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		sbDisk = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Target Disk" ), wx.VERTICAL )

		bRoot = wx.BoxSizer( wx.HORIZONTAL )

		self.m_lblRoot = wx.StaticText( sbDisk.GetStaticBox(), wx.ID_ANY, u"Root", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblRoot.Wrap( -1 )

		bRoot.Add( self.m_lblRoot, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_txtRoot = wx.TextCtrl( sbDisk.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bRoot.Add( self.m_txtRoot, 1, wx.ALL, 5 )

		self.m_chkRoot = wx.CheckBox( sbDisk.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_chkRoot.SetValue(True)
		bRoot.Add( self.m_chkRoot, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbDisk.Add( bRoot, 1, wx.EXPAND, 5 )

		bHome = wx.BoxSizer( wx.HORIZONTAL )

		self.m_lblHome = wx.StaticText( sbDisk.GetStaticBox(), wx.ID_ANY, u"Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblHome.Wrap( -1 )

		bHome.Add( self.m_lblHome, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_txtHome = wx.TextCtrl( sbDisk.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bHome.Add( self.m_txtHome, 1, wx.ALL, 5 )

		self.m_chkHome = wx.CheckBox( sbDisk.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bHome.Add( self.m_chkHome, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbDisk.Add( bHome, 1, wx.EXPAND, 5 )

		bEFI = wx.BoxSizer( wx.HORIZONTAL )

		self.m_lblEFI = wx.StaticText( sbDisk.GetStaticBox(), wx.ID_ANY, u"EFI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblEFI.Wrap( -1 )

		bEFI.Add( self.m_lblEFI, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_txtEFI = wx.TextCtrl( sbDisk.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bEFI.Add( self.m_txtEFI, 1, wx.ALL, 5 )

		self.m_chkEFI = wx.CheckBox( sbDisk.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bEFI.Add( self.m_chkEFI, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbDisk.Add( bEFI, 1, wx.EXPAND, 5 )

		bGRUB = wx.BoxSizer( wx.HORIZONTAL )

		self.m_lblGRUB = wx.StaticText( sbDisk.GetStaticBox(), wx.ID_ANY, u"GRUB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblGRUB.Wrap( -1 )

		bGRUB.Add( self.m_lblGRUB, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_txtGRUB = wx.TextCtrl( sbDisk.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bGRUB.Add( self.m_txtGRUB, 1, wx.ALL, 5 )

		self.m_chkGRUB = wx.CheckBox( sbDisk.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_chkGRUB.SetValue(True)
		bGRUB.Add( self.m_chkGRUB, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbDisk.Add( bGRUB, 1, wx.EXPAND, 5 )


		bInstall.Add( sbDisk, 0, wx.EXPAND, 5 )


		bInstall.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		sbMethod = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Extract Method" ), wx.VERTICAL )

		bMethod = wx.BoxSizer( wx.HORIZONTAL )

		self.m_chkUnsfs = wx.CheckBox( sbMethod.GetStaticBox(), wx.ID_ANY, u"Unsquashfs", wx.DefaultPosition, wx.DefaultSize, 0 )
		bMethod.Add( self.m_chkUnsfs, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_chkSfs = wx.CheckBox( sbMethod.GetStaticBox(), wx.ID_ANY, u"Rsync", wx.DefaultPosition, wx.DefaultSize, 0 )
		bMethod.Add( self.m_chkSfs, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		sbMethod.Add( bMethod, 1, wx.EXPAND, 5 )


		bInstall.Add( sbMethod, 0, wx.EXPAND, 5 )


		bInstall.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		sbCmd = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Commands" ), wx.VERTICAL )

		bCmd = wx.BoxSizer( wx.HORIZONTAL )

		self.m_btnHelp = wx.Button( sbCmd.GetStaticBox(), wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		bCmd.Add( self.m_btnHelp, 1, wx.ALL, 5 )

		self.m_btnParted = wx.Button( sbCmd.GetStaticBox(), wx.ID_ANY, u"Partition Editor", wx.DefaultPosition, wx.DefaultSize, 0 )
		bCmd.Add( self.m_btnParted, 1, wx.ALL, 5 )

		self.m_btnInstall = wx.Button( sbCmd.GetStaticBox(), wx.ID_ANY, u"Install", wx.DefaultPosition, wx.DefaultSize, 0 )
		bCmd.Add( self.m_btnInstall, 1, wx.ALL, 5 )


		sbCmd.Add( bCmd, 1, wx.EXPAND, 5 )


		bInstall.Add( sbCmd, 0, wx.EXPAND, 5 )


		bInstall.Add( ( 0, 10), 1, wx.EXPAND, 5 )


		bMain.Add( bInstall, 1, wx.EXPAND, 5 )


		bMain.Add( ( 10, 0), 0, wx.EXPAND, 5 )

		bConsole = wx.BoxSizer( wx.VERTICAL )

		sbConsole = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Install Log" ), wx.VERTICAL )

		self.m_lblLog = wx.StaticText( sbConsole.GetStaticBox(), wx.ID_ANY, u"Idle", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblLog.Wrap( -1 )

		sbConsole.Add( self.m_lblLog, 0, wx.ALL, 5 )

		self.m_txtConsole = wx.TextCtrl( sbConsole.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
		sbConsole.Add( self.m_txtConsole, 1, wx.ALL|wx.EXPAND, 5 )


		bConsole.Add( sbConsole, 1, wx.EXPAND, 5 )


		bConsole.Add( ( 0, 10), 0, wx.EXPAND, 5 )


		bMain.Add( bConsole, 1, wx.EXPAND, 5 )


		bMain.Add( ( 5, 0), 0, wx.EXPAND, 5 )


		self.SetSizer( bMain )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_chkHome.Bind( wx.EVT_CHECKBOX, self.OnChkHome )
		self.m_chkUnsfs.Bind( wx.EVT_CHECKBOX, self.OnChkUnsfs )
		self.m_chkSfs.Bind( wx.EVT_CHECKBOX, self.OnChkSfs )
		self.m_btnHelp.Bind( wx.EVT_BUTTON, self.OnBtnHelp )
		self.m_btnParted.Bind( wx.EVT_BUTTON, self.OnBtnParted )
		self.m_btnInstall.Bind( wx.EVT_BUTTON, self.OnBtnInstall )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnChkHome( self, event ):
		event.Skip()

	def OnChkUnsfs( self, event ):
		event.Skip()

	def OnChkSfs( self, event ):
		event.Skip()

	def OnBtnHelp( self, event ):
		event.Skip()

	def OnBtnParted( self, event ):
		event.Skip()

	def OnBtnInstall( self, event ):
		event.Skip()



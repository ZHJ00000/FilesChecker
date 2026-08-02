# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from GetBitmapPath import *
import wx.richtext
import wx.html

import gettext
_ = gettext.gettext

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"FilesChecker"), pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 1000,600 ), wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Start Chec&k\tCtrl+Enter"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem1 )

        self.m_menu1.AppendSeparator()

        self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Add &File...\tCtrl+F"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem2 )

        self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Add C&hecksum...\tCtrl+H"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem3 )

        self.m_menu1.AppendSeparator()

        self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"&Open Task List...\tCtrl+O"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem4 )

        self.m_menuItem5 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"&Save Task List...\tCtrl+S"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem5 )

        self.m_menu1.AppendSeparator()

        self.m_menuItem6 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"&Export Check Result...\tCtrl+E"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem6 )

        self.m_menu1.AppendSeparator()

        self.m_menuItem7 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"&Clear List"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem7 )

        self.m_menu1.AppendSeparator()

        self.m_menuItem8 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"Work &Directory...\tAlt+D"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem8 )

        self.m_menu1.AppendSeparator()

        self.m_menuItem9 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"&Settings...\tCtrl+Alt+S"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem9 )

        self.m_menuItem10 = wx.MenuItem( self.m_menu1, wx.ID_EXIT, _(u"E&xit\tAlt+F4"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem10 )

        self.m_menubar1.Append( self.m_menu1, _(u"&Task") )

        self.m_menu2 = wx.Menu()
        self.m_menuItem11 = wx.MenuItem( self.m_menu2, wx.ID_ANY, _(u"Software &Update..."), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem11 )

        self.m_menuItem12 = wx.MenuItem( self.m_menu2, wx.ID_ABOUT, _(u"&About"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.Append( self.m_menuItem12 )

        self.m_menubar1.Append( self.m_menu2, _(u"&Help") )

        self.SetMenuBar( self.m_menubar1 )

        self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
        m_choice1Choices = [ _(u"Mode 1"), _(u"Mode 2") ]
        self.m_choice1 = wx.Choice( self.m_toolBar1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        self.m_toolBar1.AddControl( self.m_choice1 )
        m_choice2Choices = [ _(u"MD5"), _(u"SHA-1"), _(u"SHA-224"), _(u"SHA-256"), _(u"SHA-384"), _(u"SHA-512"), _(u"SHA3-224"), _(u"SHA3-256"), _(u"SHA3-384"), _(u"SHA3-512"), _(u"BLAKE2b"), _(u"BLAKE2s"), _(u"CRC-32") ]
        self.m_choice2 = wx.Choice( self.m_toolBar1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        self.m_toolBar1.AddControl( self.m_choice2 )
        self.m_button1 = wx.Button( self.m_toolBar1, wx.ID_ANY, _(u"Add &File..."), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toolBar1.AddControl( self.m_button1 )
        self.m_button2 = wx.Button( self.m_toolBar1, wx.ID_ANY, _(u"Add C&hecksum..."), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toolBar1.AddControl( self.m_button2 )
        self.m_button3 = wx.Button( self.m_toolBar1, wx.ID_ANY, _(u"Start Chec&k"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toolBar1.AddControl( self.m_button3 )
        self.m_toolBar1.Realize()

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT )
        bSizer1.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_menu3 = wx.Menu()
        self.m_menuItem13 = wx.MenuItem( self.m_menu3, wx.ID_ANY, _(u"Show &Details"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.m_menuItem13 )

        self.m_menu3.AppendSeparator()

        self.m_menuItem14 = wx.MenuItem( self.m_menu3, wx.ID_ANY, _(u"Re-Select &File..."), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.m_menuItem14 )

        self.m_menuItem15 = wx.MenuItem( self.m_menu3, wx.ID_ANY, _(u"Edit C&hecksum..."), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.m_menuItem15 )

        self.m_menu3.AppendSeparator()

        self.m_menuItem16 = wx.MenuItem( self.m_menu3, wx.ID_ANY, _(u"Copy &File Address"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.m_menuItem16 )

        self.m_menuItem17 = wx.MenuItem( self.m_menu3, wx.ID_ANY, _(u"Copy C&hecksum"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.m_menuItem17 )

        self.m_menu3.AppendSeparator()

        self.m_menuItem18 = wx.MenuItem( self.m_menu3, wx.ID_ANY, _(u"&Delete"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.Append( self.m_menuItem18 )

        self.Bind( wx.EVT_RIGHT_DOWN, self.MainOnContextMenu )

        self.m_statusBar1 = self.CreateStatusBar( 2, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.exit )
        self.Bind( wx.EVT_MENU, self.start_check, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.add_file, id = self.m_menuItem2.GetId() )
        self.Bind( wx.EVT_MENU, self.add_checksum, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.open_task, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.save_task, id = self.m_menuItem5.GetId() )
        self.Bind( wx.EVT_MENU, self.export, id = self.m_menuItem6.GetId() )
        self.Bind( wx.EVT_MENU, self.clear_list, id = self.m_menuItem7.GetId() )
        self.Bind( wx.EVT_MENU, self.work_directory, id = self.m_menuItem8.GetId() )
        self.Bind( wx.EVT_MENU, self.open_settings, id = self.m_menuItem9.GetId() )
        self.Bind( wx.EVT_MENU, self.exit, id = self.m_menuItem10.GetId() )
        self.Bind( wx.EVT_MENU, self.ota, id = self.m_menuItem11.GetId() )
        self.Bind( wx.EVT_MENU, self.about, id = self.m_menuItem12.GetId() )
        self.m_choice1.Bind( wx.EVT_CHOICE, self.switch_mode )
        self.m_button1.Bind( wx.EVT_BUTTON, self.add_file )
        self.m_button2.Bind( wx.EVT_BUTTON, self.add_checksum )
        self.m_button3.Bind( wx.EVT_BUTTON, self.start_check )
        self.m_listCtrl1.Bind( wx.EVT_LIST_COL_CLICK, self.setsort )
        self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_RIGHT_CLICK, self.right_menu )
        self.Bind( wx.EVT_MENU, self.show_detail, id = self.m_menuItem13.GetId() )
        self.Bind( wx.EVT_MENU, self.reselect_file, id = self.m_menuItem14.GetId() )
        self.Bind( wx.EVT_MENU, self.edit_checksum, id = self.m_menuItem15.GetId() )
        self.Bind( wx.EVT_MENU, self.copy_file_address, id = self.m_menuItem16.GetId() )
        self.Bind( wx.EVT_MENU, self.copy_checksum, id = self.m_menuItem17.GetId() )
        self.Bind( wx.EVT_MENU, self.delete_item, id = self.m_menuItem18.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def exit( self, event ):
        event.Skip()

    def start_check( self, event ):
        event.Skip()

    def add_file( self, event ):
        event.Skip()

    def add_checksum( self, event ):
        event.Skip()

    def open_task( self, event ):
        event.Skip()

    def save_task( self, event ):
        event.Skip()

    def export( self, event ):
        event.Skip()

    def clear_list( self, event ):
        event.Skip()

    def work_directory( self, event ):
        event.Skip()

    def open_settings( self, event ):
        event.Skip()


    def ota( self, event ):
        event.Skip()

    def about( self, event ):
        event.Skip()

    def switch_mode( self, event ):
        event.Skip()




    def setsort( self, event ):
        event.Skip()

    def right_menu( self, event ):
        event.Skip()

    def show_detail( self, event ):
        event.Skip()

    def reselect_file( self, event ):
        event.Skip()

    def edit_checksum( self, event ):
        event.Skip()

    def copy_file_address( self, event ):
        event.Skip()

    def copy_checksum( self, event ):
        event.Skip()

    def delete_item( self, event ):
        event.Skip()

    def MainOnContextMenu( self, event ):
        self.PopupMenu( self.m_menu3, event.GetPosition() )


###########################################################################
## Class Settings
###########################################################################

class Settings ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Settings"), pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_listbook1 = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT|wx.LB_LEFT )
        self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, _(u"When Starting the Software") ), wx.VERTICAL )

        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText1 = wx.StaticText( self.sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"Default Check Mode: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        gSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_choice3Choices = [ _(u"Mode 1"), _(u"Mode 2") ]
        self.m_choice3 = wx.Choice( self.sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        gSizer1.Add( self.m_choice3, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.sbSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )


        bSizer3.Add( self.sbSizer1, 0, wx.EXPAND|wx.ALL, 5 )

        self.sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, _(u"Operation After Completion") ), wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self.sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Run Command: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.sbSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

        gSizer2 = wx.GridSizer( 0, 4, 0, 0 )

        self.m_radioBtn1 = wx.RadioButton( self.sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"None"), wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        gSizer2.Add( self.m_radioBtn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_radioBtn2 = wx.RadioButton( self.sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Shutdown"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_radioBtn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_radioBtn3 = wx.RadioButton( self.sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Reboot"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_radioBtn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_radioBtn4 = wx.RadioButton( self.sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Custom..."), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_radioBtn4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.sbSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self.sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sbSizer2.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer3.Add( self.sbSizer2, 0, wx.EXPAND|wx.ALL, 5 )

        self.sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, _(u"Automatically Save Check Result") ), wx.VERTICAL )

        self.m_checkBox1 = wx.CheckBox( self.sbSizer3.GetStaticBox(), wx.ID_ANY, _(u"Automatically Save Check Result"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sbSizer3.Add( self.m_checkBox1, 0, wx.ALL, 5 )

        fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_textCtrl4 = wx.TextCtrl( self.sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 425,-1 ), 0 )
        self.m_textCtrl4.Enable( False )

        fgSizer5.Add( self.m_textCtrl4, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        self.m_button6 = wx.Button( self.sbSizer3.GetStaticBox(), wx.ID_ANY, _(u"..."), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        self.m_button6.Enable( False )

        fgSizer5.Add( self.m_button6, 0, wx.ALL, 5 )


        self.sbSizer3.Add( fgSizer5, 1, wx.EXPAND, 5 )


        bSizer3.Add( self.sbSizer3, 0, wx.EXPAND|wx.ALL, 5 )

        self.sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, _(u"Other") ), wx.VERTICAL )

        self.m_checkBox2 = wx.CheckBox( self.sbSizer4.GetStaticBox(), wx.ID_ANY, _(u"Display The Checksum in Uppercase"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sbSizer4.Add( self.m_checkBox2, 0, wx.ALL, 5 )


        bSizer3.Add( self.sbSizer4, 0, wx.EXPAND|wx.ALL, 5 )


        self.m_scrolledWindow1.SetSizer( bSizer3 )
        self.m_scrolledWindow1.Layout()
        bSizer3.Fit( self.m_scrolledWindow1 )
        self.m_listbook1.AddPage( self.m_scrolledWindow1, _(u"Routine"), True )
        self.m_scrolledWindow2 = wx.ScrolledWindow( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow2.SetScrollRate( 5, 5 )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, _(u"Task List") ), wx.VERTICAL )

        gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText3 = wx.StaticText( self.sbSizer5.GetStaticBox(), wx.ID_ANY, _(u"Use encoding when saving task list: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        gSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_choice4Choices = []
        self.m_choice4 = wx.Choice( self.sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
        self.m_choice4.SetSelection( 0 )
        gSizer3.Add( self.m_choice4, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.sbSizer5.Add( gSizer3, 1, wx.EXPAND, 5 )

        self.m_checkBox3 = wx.CheckBox( self.sbSizer5.GetStaticBox(), wx.ID_ANY, _(u"Compatible with Old Versions"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sbSizer5.Add( self.m_checkBox3, 0, wx.ALL, 5 )


        bSizer4.Add( self.sbSizer5, 0, wx.EXPAND|wx.ALL, 5 )

        self.sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, _(u"Check Result") ), wx.VERTICAL )

        gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText4 = wx.StaticText( self.sbSizer6.GetStaticBox(), wx.ID_ANY, _(u"Use encoding when exporting check result: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        gSizer4.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_choice5Choices = []
        self.m_choice5 = wx.Choice( self.sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
        self.m_choice5.SetSelection( 0 )
        gSizer4.Add( self.m_choice5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


        self.sbSizer6.Add( gSizer4, 1, wx.EXPAND, 5 )


        bSizer4.Add( self.sbSizer6, 0, wx.EXPAND|wx.ALL, 5 )

        self.m_button4 = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, _(u"&Restore Default Settings"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        self.m_scrolledWindow2.SetSizer( bSizer4 )
        self.m_scrolledWindow2.Layout()
        bSizer4.Fit( self.m_scrolledWindow2 )
        self.m_listbook1.AddPage( self.m_scrolledWindow2, _(u"Files"), False )
        self.m_scrolledWindow3 = wx.ScrolledWindow( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow3.SetScrollRate( 5, 5 )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_infoCtrl1 = wx.InfoBar( self.m_scrolledWindow3 )
        self.m_infoCtrl1.SetShowHideEffects( wx.SHOW_EFFECT_NONE, wx.SHOW_EFFECT_NONE )
        self.m_infoCtrl1.SetEffectDuration( 500 )
        bSizer5.Add( self.m_infoCtrl1, 0, wx.EXPAND|wx.ALL, 5 )

        self.sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, _(u"Language Setting") ), wx.VERTICAL )

        m_listBox1Choices = []
        self.m_listBox1 = wx.ListBox( self.sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
        self.sbSizer7.Add( self.m_listBox1, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer5.Add( self.sbSizer7, 1, wx.EXPAND|wx.ALL, 5 )


        self.m_scrolledWindow3.SetSizer( bSizer5 )
        self.m_scrolledWindow3.Layout()
        bSizer5.Fit( self.m_scrolledWindow3 )
        self.m_listbook1.AddPage( self.m_scrolledWindow3, _(u"Language"), False )

        bSizer2.Add( self.m_listbook1, 1, wx.EXPAND |wx.ALL, 5 )

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
        self.m_sdbSizer1Apply = wx.Button( self, wx.ID_APPLY )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Apply )
        self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
        m_sdbSizer1.Realize()

        bSizer2.Add( m_sdbSizer1, 0, wx.EXPAND|wx.ALL, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.close )
        self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.run_command_choice_none )
        self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.run_command_choice_shutdown )
        self.m_radioBtn3.Bind( wx.EVT_RADIOBUTTON, self.run_command_choice_reboot )
        self.m_radioBtn4.Bind( wx.EVT_RADIOBUTTON, self.run_command_choice_custom )
        self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.ascr_check )
        self.m_button6.Bind( wx.EVT_BUTTON, self.getascrpath )
        self.m_button4.Bind( wx.EVT_BUTTON, self.files_setting_restore )
        self.m_sdbSizer1Apply.Bind( wx.EVT_BUTTON, self.apply )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def close( self, event ):
        event.Skip()

    def run_command_choice_none( self, event ):
        event.Skip()

    def run_command_choice_shutdown( self, event ):
        event.Skip()

    def run_command_choice_reboot( self, event ):
        event.Skip()

    def run_command_choice_custom( self, event ):
        event.Skip()

    def ascr_check( self, event ):
        event.Skip()

    def getascrpath( self, event ):
        event.Skip()

    def files_setting_restore( self, event ):
        event.Skip()

    def apply( self, event ):
        event.Skip()


###########################################################################
## Class ChecksumDialog
###########################################################################

class ChecksumDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Add Checksum"), pos = wx.DefaultPosition, size = wx.Size( 300,150 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )


        bSizer6.Add( ( 0, 5), 0, wx.EXPAND, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        bSizer6.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"Checksum Type: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )

        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
        m_sdbSizer2.Realize()

        bSizer6.Add( m_sdbSizer2, 0, wx.EXPAND|wx.ALL, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_textCtrl2.Bind( wx.EVT_TEXT, self.gettype )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def gettype( self, event ):
        event.Skip()


###########################################################################
## Class About
###########################################################################

class About ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"About"), pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_customControl1 = wx.GenericStaticBitmap(self, wx.ID_ANY, wx.BitmapBundle.FromBitmap(wx.Bitmap(GetBitmapPath())), wx.DefaultPosition, wx.Size(50, 50), 0)
        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


        fgSizer1.Add( self.m_customControl1, 0, wx.ALL, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"FilesChecker"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer8.Add( self.m_staticText6, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, _(u"Version: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer8.Add( self.m_staticText7, 0, wx.RIGHT|wx.LEFT, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"Build: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer8.Add( self.m_staticText8, 0, wx.RIGHT|wx.LEFT, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"Copyright ©2026 ZHJ."), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer8.Add( self.m_staticText9, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )


        fgSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )


        bSizer7.Add( fgSizer1, 0, wx.EXPAND|wx.ALL, 5 )

        self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        bSizer7.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer7 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class Calculation
###########################################################################

class Calculation ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Checksum Calculation"), pos = wx.DefaultPosition, size = wx.Size( 500,250 ), style = wx.CAPTION|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, _(u"Elapsed time: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        fgSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"00:00:00"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        fgSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, _(u"File: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        fgSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        fgSizer2.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, _(u"Size: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        fgSizer2.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )

        fgSizer2.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, _(u"Speed: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        fgSizer2.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        fgSizer2.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, _(u"Progress: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        fgSizer2.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.GA_HORIZONTAL )
        self.m_gauge1.SetValue( 0 )
        self.m_gauge1.SetMinSize( wx.Size( 350,-1 ) )

        fgSizer2.Add( self.m_gauge1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, _(u"Overall progress: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        fgSizer2.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_gauge2 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.GA_HORIZONTAL )
        self.m_gauge2.SetValue( 0 )
        self.m_gauge2.SetMinSize( wx.Size( 350,-1 ) )

        fgSizer2.Add( self.m_gauge2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer9.Add( fgSizer2, 1, wx.EXPAND, 5 )

        m_sdbSizer3 = wx.StdDialogButtonSizer()
        self.m_sdbSizer3OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer3.AddButton( self.m_sdbSizer3OK )
        self.m_sdbSizer3Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer3.AddButton( self.m_sdbSizer3Cancel )
        m_sdbSizer3.Realize()

        bSizer9.Add( m_sdbSizer3, 0, wx.EXPAND|wx.ALL, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.cancel )
        self.m_sdbSizer3Cancel.Bind( wx.EVT_BUTTON, self.cancel )
        self.m_sdbSizer3OK.Bind( wx.EVT_BUTTON, self.pause )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def cancel( self, event ):
        event.Skip()


    def pause( self, event ):
        event.Skip()


###########################################################################
## Class EncodingPicker
###########################################################################

class EncodingPicker ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Open Text Document"), pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, _(u"Please select the encoding."), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )

        bSizer11.Add( self.m_staticText20, 0, wx.ALL, 5 )

        m_listBox2Choices = []
        self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
        bSizer11.Add( self.m_listBox2, 1, wx.ALL|wx.EXPAND, 5 )


        gSizer5.Add( bSizer11, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, _(u"Preview: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        bSizer12.Add( self.m_staticText21, 0, wx.ALL, 5 )

        self.m_richText2 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        bSizer12.Add( self.m_richText2, 1, wx.EXPAND |wx.ALL, 5 )


        gSizer5.Add( bSizer12, 1, wx.EXPAND, 5 )


        bSizer10.Add( gSizer5, 1, wx.EXPAND, 5 )

        m_sdbSizer4 = wx.StdDialogButtonSizer()
        self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
        self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
        m_sdbSizer4.Realize()

        bSizer10.Add( m_sdbSizer4, 0, wx.EXPAND|wx.ALL, 5 )


        self.SetSizer( bSizer10 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_listBox2.Bind( wx.EVT_LISTBOX, self.update_preview )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def update_preview( self, event ):
        event.Skip()


###########################################################################
## Class Details
###########################################################################

class Details ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Details"), pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        self.m_richText3 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        bSizer13.Add( self.m_richText3, 1, wx.EXPAND |wx.ALL, 5 )

        m_sdbSizer5 = wx.StdDialogButtonSizer()
        self.m_sdbSizer5OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer5.AddButton( self.m_sdbSizer5OK )
        m_sdbSizer5.Realize()

        bSizer13.Add( m_sdbSizer5, 0, wx.EXPAND|wx.ALL, 5 )


        self.SetSizer( bSizer13 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class OTA
###########################################################################

class OTA ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Software Update"), pos = wx.DefaultPosition, size = wx.Size( 600,450 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_customControl2 = wx.GenericStaticBitmap(self, wx.ID_ANY, wx.BitmapBundle.FromBitmap(wx.Bitmap(GetBitmapPath())), wx.DefaultPosition, wx.Size(50, 50), 0)
        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


        fgSizer3.Add( self.m_customControl2, 0, wx.ALL, 5 )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, _(u"FilesChecker"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        bSizer15.Add( self.m_staticText22, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )

        self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, _(u"Current Version: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )

        bSizer15.Add( self.m_staticText23, 0, wx.RIGHT|wx.LEFT, 5 )

        self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, _(u"Lastest Version: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )

        bSizer15.Add( self.m_staticText24, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )


        fgSizer3.Add( bSizer15, 1, wx.EXPAND, 5 )


        bSizer14.Add( fgSizer3, 0, wx.EXPAND, 5 )

        self.m_htmlWin1 = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
        bSizer14.Add( self.m_htmlWin1, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, _(u"Connecting..."), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText30.Wrap( -1 )

        self.m_staticText30.Hide()

        bSizer14.Add( self.m_staticText30, 0, wx.ALL, 5 )

        self.m_gauge3 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge3.SetValue( 0 )
        self.m_gauge3.Hide()

        bSizer14.Add( self.m_gauge3, 0, wx.ALL|wx.EXPAND, 5 )

        m_sdbSizer6 = wx.StdDialogButtonSizer()
        self.m_sdbSizer6OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer6.AddButton( self.m_sdbSizer6OK )
        self.m_sdbSizer6Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer6.AddButton( self.m_sdbSizer6Cancel )
        m_sdbSizer6.Realize()

        bSizer14.Add( m_sdbSizer6, 0, wx.EXPAND|wx.ALL, 5 )


        self.SetSizer( bSizer14 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class ItemDialog
###########################################################################

class ItemDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Add Item"), pos = wx.DefaultPosition, size = wx.Size( 400,180 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer4.SetFlexibleDirection( wx.BOTH )
        fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, _(u"File: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )

        fgSizer4.Add( self.m_staticText25, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer6.SetFlexibleDirection( wx.BOTH )
        fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
        fgSizer6.Add( self.m_textCtrl5, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.EXPAND, 5 )

        self.m_button7 = wx.Button( self, wx.ID_ANY, _(u"..."), wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        fgSizer6.Add( self.m_button7, 0, wx.ALL, 5 )


        fgSizer4.Add( fgSizer6, 1, wx.EXPAND, 5 )

        self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, _(u"Expected Checksum: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )

        fgSizer4.Add( self.m_staticText26, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        fgSizer4.Add( self.m_textCtrl3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

        self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, _(u"Checksum Type: "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27.Wrap( -1 )

        fgSizer4.Add( self.m_staticText27, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText28.Wrap( -1 )

        fgSizer4.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer16.Add( fgSizer4, 0, wx.EXPAND, 5 )

        m_sdbSizer7 = wx.StdDialogButtonSizer()
        self.m_sdbSizer7OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer7.AddButton( self.m_sdbSizer7OK )
        self.m_sdbSizer7Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer7.AddButton( self.m_sdbSizer7Cancel )
        m_sdbSizer7.Realize()

        bSizer16.Add( m_sdbSizer7, 0, wx.EXPAND|wx.ALL, 5 )


        self.SetSizer( bSizer16 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button7.Bind( wx.EVT_BUTTON, self.getpath )
        self.m_textCtrl3.Bind( wx.EVT_TEXT, self.gettype )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def getpath( self, event ):
        event.Skip()

    def gettype( self, event ):
        event.Skip()


###########################################################################
## Class OpenTaskDialog
###########################################################################

class OpenTaskDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Open Task List"), pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer17 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, _(u"Paste or load task list from file. "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText29.Wrap( -1 )

        bSizer17.Add( self.m_staticText29, 0, wx.ALL, 5 )

        self.m_richText4 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        bSizer17.Add( self.m_richText4, 1, wx.EXPAND |wx.ALL, 5 )

        gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_button5 = wx.Button( self, wx.ID_ANY, _(u"Load &File..."), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer6.Add( self.m_button5, 0, wx.ALL, 5 )

        m_sdbSizer8 = wx.StdDialogButtonSizer()
        self.m_sdbSizer8OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer8.AddButton( self.m_sdbSizer8OK )
        m_sdbSizer8.Realize()

        gSizer6.Add( m_sdbSizer8, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer17.Add( gSizer6, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer17 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button5.Bind( wx.EVT_BUTTON, self.load )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def load( self, event ):
        event.Skip()



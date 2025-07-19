# coding=utf-8
# Copyright ©2025 ZHJ.

import wx, wx.xrc, wx.adv, wx.richtext, wx.html  # pip install wxPython
import sys
import os
import glob
import hashlib
import threading
import time
import datetime
import pyperclip  # pip install pyperclip
from importlib import reload
import locale
import zlib
import platform
import ctypes
import markdown  # pip install Markdown
import subprocess
import json
import shutil
sysver = []
for i in platform.version().split('.'):
    sysver.append(int(i))
# Use DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 in Windows 10 1703 and above, Otherwise,
# use DPI_AWARENESS_CONTEXT_SYSTEM_AWARE
if tuple(sysver) >= (10, 0, 15063):
    ctypes.windll.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))
else:
    ctypes.windll.user32.SetProcessDPIAware()
locale = locale.getlocale()[0]


ischeck = False
command = ''
export = ''
isexport = False
#os.chdir(os.path.dirname(sys.argv[0]))
version = (3, 1, 2)
with open(os.path.join(os.path.dirname(sys.argv[0]), "Encodings.txt"), 'r', encoding='utf-8') as f:
    encodinglist = f.readlines()
encodingslist = [[], []]
for i in range(len(encodinglist)):
    encodinglist[i] = encodinglist[i].rstrip().split('==>')
    encodingslist[0].append(encodinglist[i][0])
    encodingslist[1].append(encodinglist[i][1])
del encodinglist
def find_encoding_key(coding, encodingslist=encodingslist):
    coding = coding.upper().replace('_', '-')
    if coding in encodingslist[1]:
        return coding
    else:
        if coding in encodingslist[0]:
            return encodingslist[1][encodingslist[0].index(coding)]
        else:
            return None

def intask(file, encoding):
    try:
        with open(file, 'r', encoding=encoding, errors='replace') as file:
            l = file.readlines()
    except Exception as err:
        tf = False
        toastone = wx.MessageDialog(None, language.s56() + type(err).__name__ + ': ' + str(err), language.s81(),
                                    wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
        toastone.SetOKLabel(language.s57())
        if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
            toastone.Destroy()
    else:
        for i in range(0, len(l)):
            l[i] = l[i].rstrip()
        for i in range(0, len(l)):
            a = l[i].split('##')
            b = ''
            for j in range(len(a)):
                if '#' in a[j]:
                    b = b + a[j].partition('#')[0]
                    break
                else:
                    if j != len(a) - 1:
                        b = b + a[j] + '#'
                    else:
                        b = b + a[j]
            l[i] = b
            del a
            del b
        while '' in l:
            l.remove('')
        tf = False
        if len(l) == 0:
            toastone = wx.MessageDialog(None, language.s58(), language.s81(),
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
            toastone.SetOKLabel(language.s57())
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
        else:
            for i in range(0, len(l)):
                l[i] = l[i].rstrip()
            l[0] = l[0].lower()
            if l[0] == 'md5':
                frame.m_choice1.SetSelection(0)
                tf = True
            elif l[0] == 'sha1' or l[0] == 'sha-1':
                frame.m_choice1.SetSelection(1)
                tf = True
            elif l[0] == 'sha224' or l[0] == 'sha-224':
                frame.m_choice1.SetSelection(2)
                tf = True
            elif l[0] == 'sha256' or l[0] == 'sha-256':
                frame.m_choice1.SetSelection(3)
                tf = True
            elif l[0] == 'sha384' or l[0] == 'sha-384':
                frame.m_choice1.SetSelection(4)
                tf = True
            elif l[0] == 'sha512' or l[0] == 'sha-512':
                frame.m_choice1.SetSelection(5)
                tf = True
            elif l[0] == 'sha3-224':
                frame.m_choice1.SetSelection(6)
                tf = True
            elif l[0] == 'sha3-256':
                frame.m_choice1.SetSelection(7)
                tf = True
            elif l[0] == 'sha3-384':
                frame.m_choice1.SetSelection(8)
                tf = True
            elif l[0] == 'sha3-512':
                frame.m_choice1.SetSelection(9)
                tf = True
            elif l[0] == 'blake2b':
                frame.m_choice1.SetSelection(10)
                tf = True
            elif l[0] == 'blake2s':
                frame.m_choice1.SetSelection(11)
                tf = True
            elif l[0] == 'crc32' or l[0] == 'crc-32':
                frame.m_choice1.SetSelection(12)
                tf = True
            else:
                toastone = wx.MessageDialog(None, language.s58(), language.s81(),
                                            wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                toastone.SetOKLabel(language.s57())
                if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                    toastone.Destroy()
                tf = False
    if tf:
        ll = []
        for i in range(len(l)):
            ll.append(l[i].lower())
        try:
            if ll[1] != '<file>' and ll[1] != '<hash>':
                tf = False
                toastone = wx.MessageDialog(None, language.s59(), language.s81(),
                                            wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                toastone.SetOKLabel(language.s57())
                if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                    toastone.Destroy()
        except IndexError:
            toastone = wx.MessageDialog(None, language.s61(), language.s62(),
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_WARNING)
            toastone.SetOKLabel(language.s57())
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
            tf = False
    if tf:
        foha = ''
        count = frame.m_listCtrl2.GetItemCount()
        for i in range(1, len(l)):
            if ll[i] == '<file>':
                foha = 1
            elif ll[i] == '<hash>':
                foha = 2
            else:
                if foha == 1:
                    if l[i][0] == '"' and l[i][len(l[i]) - 1] == '"':
                        data1 = list(l[i])
                        del data1[0]
                        del data1[len(data1) - 1]
                        l[i] = ''
                        for ii in range(len(data1)):
                            l[i] = l[i] + data1[ii]
                    fs = glob.glob(l[i])
                    if len(fs) == 0:
                        index = frame.m_listCtrl2.InsertItem(frame.m_listCtrl2.GetItemCount(),
                                                             str(frame.m_listCtrl2.GetItemCount() + 1))
                        frame.m_listCtrl2.SetItem(index, 1, '')
                        frame.m_listCtrl2.SetItem(index, 2, l[i])
                        frame.m_listCtrl2.SetItem(index, 3, '')
                        information.append('/')
                    else:
                        for i in range(0, len(fs)):
                            if os.path.isfile(fs[i]) == False:
                                fs[i] = ''
                        while '' in fs:
                            fs.remove('')
                        for fah in fs:
                            index = frame.m_listCtrl2.InsertItem(frame.m_listCtrl2.GetItemCount(),
                                                                 str(frame.m_listCtrl2.GetItemCount() + 1))
                            frame.m_listCtrl2.SetItem(index, 1, '')
                            frame.m_listCtrl2.SetItem(index, 2, fah)
                            frame.m_listCtrl2.SetItem(index, 3, '')
                            information.append('/')
                elif foha == 2:
                    l[i] = l[i].lower()
                    index = frame.m_listCtrl2.InsertItem(frame.m_listCtrl2.GetItemCount(),
                                                         str(frame.m_listCtrl2.GetItemCount() + 1))
                    frame.m_listCtrl2.SetItem(index, 1, '')
                    frame.m_listCtrl2.SetItem(index, 2, '')
                    frame.m_listCtrl2.SetItem(index, 3, l[i])
                    information.append('/')
        if count == frame.m_listCtrl2.GetItemCount():
            toastone = wx.MessageDialog(None, language.s61(), language.s62(),
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_WARNING)
            toastone.SetOKLabel(language.s57())
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
        frame.sort(None)

class OperationCancelledError(Exception):
    pass

class FileDrop(wx.FileDropTarget):
    def __init__(self):
        wx.FileDropTarget.__init__(self)

    def OnDropFiles(self, x, y, filePath):
        global information
        for i in filePath:
            if os.path.isdir(i) == False:
                index = frame.m_listCtrl2.InsertItem(frame.m_listCtrl2.GetItemCount(),
                                                     str(frame.m_listCtrl2.GetItemCount() + 1))
                frame.m_listCtrl2.SetItem(index, 1, '')
                frame.m_listCtrl2.SetItem(index, 2, i)
                frame.m_listCtrl2.SetItem(index, 3, '')
                information.append('/')
        frame.sort(None)
        return False

class FileDrop2(wx.FileDropTarget):
    def __init__(self):
        wx.FileDropTarget.__init__(self)

    def OnDropFiles(self, x, y, filePath):
        if os.path.isfile(filePath[0]):
            frame.additem.m_filePicker2.SetPath(filePath[0])
        return False


class main(wx.Frame):

    def __init__(self, parent):
        global file, information, update
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=language.s1(), pos=wx.DefaultPosition,
                          size=wx.Size(1000, 600),
                          style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE_BOX | wx.TAB_TRAVERSAL)
        self.SetSize(wx.Size(int('%.0f' % (1000 * self.GetDPI()[0] / 96)),
                                       int('%.0f' % (600 * self.GetDPI()[0] / 96))))
        self.SetClientSize(wx.Size(int('%.0f' % (1000 * self.GetDPI()[0] / 96)),
                                       int('%.0f' % (600 * self.GetDPI()[0] / 96))))

        self.SetSizeHints(wx.Size(int('%.0f' % (1000 * self.GetDPI()[0] / 96)),
                                       int('%.0f' % (600 * self.GetDPI()[0] / 96))),
                          wx.Size(-1, -1))
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        self.m_menubar2 = wx.MenuBar(0)
        self.m_menu3 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(self.m_menu3, wx.ID_ANY, language.s2() + "\tCtrl+Enter", language.s97(),
                                       wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_menuItem1)

        self.m_menu3.AppendSeparator()

        self.m_menuItem2 = wx.MenuItem(self.m_menu3, wx.ID_ANY, language.s3() + "\tCtrl+F", language.s98(),
                                       wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_menuItem2)

        self.m_menuItem8 = wx.MenuItem(self.m_menu3, wx.ID_ANY, language.s4() + "\tCtrl+H", language.s99(),
                                       wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_menuItem8)

        self.m_menu3.AppendSeparator()

        self.m_menuItem4 = wx.MenuItem(self.m_menu3, wx.ID_ANY, language.s5() + "\tCtrl+O", language.s100(),
                                       wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_menuItem4)

        self.m_menuItem5 = wx.MenuItem(self.m_menu3, wx.ID_ANY, language.s6() + "\tCtrl+S", language.s101(),
                                       wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_menuItem5)

        self.m_menu3.AppendSeparator()

        self.m_menuItem9 = wx.MenuItem(self.m_menu3, wx.ID_ANY, language.s7() + "\tCtrl+E", language.s102(),
                                       wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_menuItem9)

        self.m_menu3.AppendSeparator()

        self.m_menuItem3 = wx.MenuItem(self.m_menu3, wx.ID_ANY, language.s8(), wx.EmptyString,
                                       wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_menuItem3)

        self.m_menu3.AppendSeparator()

        self.m_menuItem172 = wx.MenuItem(self.m_menu3, wx.ID_ANY, language.s129() + "\tAlt+D", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_menuItem172)

        self.m_menu3.AppendSeparator()

        self.m_menuItem10 = wx.MenuItem(self.m_menu3, wx.ID_ANY, language.s9() + "\tCtrl+Alt+S", language.s103(),
                                        wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_menuItem10)

        self.m_menu3.AppendSeparator()

        self.m_menuItem6 = wx.MenuItem(self.m_menu3, wx.ID_ANY, language.s10() + "\tAlt+F4", language.s104(),
                                       wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_menuItem6)

        self.m_menubar2.Append(self.m_menu3, language.s11())

        self.m_menu5 = wx.Menu()
        self.m_menuItem171 = wx.MenuItem(self.m_menu5, wx.ID_ANY, language.s116(), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu5.Append(self.m_menuItem171)
        self.m_menuItem7 = wx.MenuItem(self.m_menu5, wx.ID_ANY, language.s12(), language.s105(), wx.ITEM_NORMAL)
        self.m_menu5.Append(self.m_menuItem7)

        self.m_menubar2.Append(self.m_menu5, language.s13())

        self.SetMenuBar(self.m_menubar2)

        self.m_toolBar1 = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        m_choice4Choices = language.s130()
        self.m_choice4 = wx.Choice(self.m_toolBar1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0)
        self.m_choice4.SetSelection(setting['DefaultCheckMode'])
        self.mode = self.m_choice4.GetSelection()
        self.m_toolBar1.AddControl(self.m_choice4)
        m_choice1Choices = ["MD5", "SHA-1", "SHA-224", "SHA-256", "SHA-384", "SHA-512", "SHA3-224", "SHA3-256",
                            "SHA3-384", "SHA3-512", "BLAKE2b", "BLAKE2s", "CRC-32"]
        self.m_choice1 = wx.Choice(self.m_toolBar1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        self.m_toolBar1.AddControl(self.m_choice1)
        self.m_button1 = wx.Button(self.m_toolBar1, wx.ID_ANY, language.s14(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_toolBar1.AddControl(self.m_button1)
        self.m_button6 = wx.Button(self.m_toolBar1, wx.ID_ANY, language.s15(), wx.DefaultPosition, wx.DefaultSize,
                                   0)
        self.m_toolBar1.AddControl(self.m_button6)
        self.m_button3 = wx.Button(self.m_toolBar1, wx.ID_ANY, language.s16(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_toolBar1.AddControl(self.m_button3)
        self.m_toolBar1.Realize()

        if self.m_choice4.GetSelection() == 1:
            self.m_menuItem2.SetItemLabel(language.s131() + '\tCtrl+F')
            self.m_menu3.Remove(self.m_menuItem8)
            self.m_menuItem2.SetHelp(language.s132())
            self.m_button1.SetLabel(language.s133())
            self.m_button6.Show(False)
            self.m_toolBar1.RemoveTool(self.m_button6.GetId())
            self.m_toolBar1.Realize()

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_listCtrl2 = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition,
                                       wx.Size(int('%.0f' % (1000 * self.GetDPI()[0] / 96)),
                                               int('%.0f' % (485 * self.GetDPI()[0] / 96))),
                                       wx.LC_HRULES | wx.LC_REPORT)
        self.m_listCtrl2.SetMinSize(
            wx.Size(int('%.0f' % (1000 * self.GetDPI()[0] / 96)),
                                               int('%.0f' % (485 * self.GetDPI()[0] / 96))))

        bSizer2.Add(self.m_listCtrl2, 1, wx.ALL | wx.EXPAND, 5)
        if self.m_choice4.GetSelection() == 0:
            self.m_listCtrl2.InsertColumn(0, language.s17())
            self.m_listCtrl2.InsertColumn(1, language.s18())
            self.m_listCtrl2.InsertColumn(2, language.s19())
            self.m_listCtrl2.InsertColumn(3, language.s20())
            self.m_listCtrl2.SetColumnWidth(0, int('%.0f' % (50 * self.GetDPI()[0] / 96)))  # 设置每一列的宽度
            self.m_listCtrl2.SetColumnWidth(1, int('%.0f' % (50 * self.GetDPI()[0] / 96)))
            self.m_listCtrl2.SetColumnWidth(2, int('%.0f' % (425 * self.GetDPI()[0] / 96)))
            self.m_listCtrl2.SetColumnWidth(3, int('%.0f' % (445 * self.GetDPI()[0] / 96)))
            fileDrop = FileDrop()
            self.m_listCtrl2.SetDropTarget(fileDrop)
        elif self.m_choice4.GetSelection() == 1:
            self.m_listCtrl2.InsertColumn(0, language.s17())
            self.m_listCtrl2.InsertColumn(1, language.s19())
            self.m_listCtrl2.InsertColumn(2, language.s134())
            self.m_listCtrl2.InsertColumn(3, language.s135())
            self.m_listCtrl2.SetColumnWidth(0, int('%.0f' % (50 * self.GetDPI()[0] / 96)))  # 设置每一列的宽度
            self.m_listCtrl2.SetColumnWidth(1, int('%.0f' % (425 * self.GetDPI()[0] / 96)))
            self.m_listCtrl2.SetColumnWidth(2, int('%.0f' % (425 * self.GetDPI()[0] / 96)))
            self.m_listCtrl2.SetColumnWidth(3, int('%.0f' % (75 * self.GetDPI()[0] / 96)))

        information = []

        self.SetSizer(bSizer2)
        self.Layout()
        self.m_statusBar3 = self.CreateStatusBar(2, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.SetStatusText('')
        self.SetStatusText(os.getcwd(), 1)

        self.m_menu4 = wx.Menu()
        self.m_menuItem12 = wx.MenuItem(self.m_menu4, wx.ID_ANY, language.s76(), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu4.Append(self.m_menuItem12)

        self.m_menu4.AppendSeparator()

        self.m_menuItem16 = wx.MenuItem(self.m_menu4, wx.ID_ANY, language.s77(), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu4.Append(self.m_menuItem16)

        self.m_menuItem17 = wx.MenuItem(self.m_menu4, wx.ID_ANY, language.s78(), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu4.Append(self.m_menuItem17)

        self.m_menu4.AppendSeparator()

        self.m_menuItem13 = wx.MenuItem(self.m_menu4, wx.ID_ANY, language.s79(), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu4.Append(self.m_menuItem13)

        self.m_menuItem14 = wx.MenuItem(self.m_menu4, wx.ID_ANY, language.s80(), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu4.Append(self.m_menuItem14)

        self.m_menu4.AppendSeparator()

        self.m_menuItem15 = wx.MenuItem(self.m_menu4, wx.ID_ANY, language.s38(), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu4.Append(self.m_menuItem15)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.exit)
        self.Bind(wx.EVT_MENU, self.startcheck, id=self.m_menuItem1.GetId())
        self.Bind(wx.EVT_MENU, self.addfile, id=self.m_menuItem2.GetId())
        self.Bind(wx.EVT_MENU, self.addhash, id=self.m_menuItem8.GetId())
        self.Bind(wx.EVT_MENU, self.inputtask, id=self.m_menuItem4.GetId())
        self.Bind(wx.EVT_MENU, self.outputtask, id=self.m_menuItem5.GetId())
        self.Bind(wx.EVT_MENU, self.outputreport, id=self.m_menuItem9.GetId())
        self.Bind(wx.EVT_MENU, self.clear, id=self.m_menuItem3.GetId())
        self.Bind(wx.EVT_MENU, self.setting, id=self.m_menuItem10.GetId())
        self.Bind(wx.EVT_MENU, self.work_directory, id=self.m_menuItem172.GetId())
        self.Bind(wx.EVT_MENU, self.exit, id=self.m_menuItem6.GetId())
        self.Bind(wx.EVT_MENU, self.getupdate, id=self.m_menuItem171.GetId())
        self.Bind(wx.EVT_MENU, self.about, id=self.m_menuItem7.GetId())
        self.m_choice4.Bind(wx.EVT_CHOICE, self.switchmode)
        self.m_button1.Bind(wx.EVT_BUTTON, self.addfile)
        self.m_button6.Bind(wx.EVT_BUTTON, self.addhash)
        self.m_button3.Bind(wx.EVT_BUTTON, self.startcheck)
        self.m_listCtrl2.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.rightmenu)
        self.m_listCtrl2.Bind(wx.EVT_LIST_COL_CLICK, self.setsort)
        #self.m_listCtrl2.Bind(wx.EVT_LIST_INSERT_ITEM, self.sort)
        self.Bind(wx.EVT_MENU, self.showinformation, id=self.m_menuItem12.GetId())
        self.Bind(wx.EVT_MENU, self.editfile, id=self.m_menuItem16.GetId())
        self.Bind(wx.EVT_MENU, self.edithash, id=self.m_menuItem17.GetId())
        self.Bind(wx.EVT_MENU, self.copyfile, id=self.m_menuItem13.GetId())
        self.Bind(wx.EVT_MENU, self.copyhash, id=self.m_menuItem14.GetId())
        self.Bind(wx.EVT_MENU, self.delete, id=self.m_menuItem15.GetId())


    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def exit(self, event):
        global iscancel
        if ischeck:
            toastone = wx.MessageDialog(None, language.s65(), language.s1(),
                                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)
            toastone.SetYesNoLabels(language.s63(), language.s64())
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
                iscancel = True
                lockfile.close()
                os.remove(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'LOCK'))
                sys.exit(0)
        else:
            lockfile.close()
            os.remove(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'LOCK'))
            sys.exit(0)

    def export(self, path):
        try:
            with open(path, 'w', encoding=setting['ExportResultEncoding']) as file:
                if self.m_choice4.GetSelection() == 0:
                    file.write(
                        language.s17() + ',' + language.s18() + ',' + language.s19() + ',' + language.s20() + '\n')
                elif self.m_choice4.GetSelection() == 1:
                    file.write(
                        language.s17() + ',' + language.s19() + ',' + language.s134() + ',' + language.s135() + '\n')
                for i in range(0, frame.m_listCtrl2.GetItemCount()):
                    for ii in range(0, 4):
                        if ii == 3:
                            file.write('"' + frame.m_listCtrl2.GetItemText(i, 3) + '"\n')
                        else:
                            file.write('"' + frame.m_listCtrl2.GetItemText(i, ii) + '",')
        except Exception as err:
            toastone = wx.MessageDialog(None, language.s75(type(err).__name__ + ': ' + str(err)), language.s81(),
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
            toastone.SetOKLabel(language.s57())
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()

    def startcheck(self, event):
        check = MyDialog4(None)
        def timeformat(seconds):
            hours = 0
            minutes = 0
            if seconds >= 60:
                minutes = seconds // 60
                seconds = seconds % 60
            if minutes >= 60:
                hours = minutes // 60
                minutes = minutes % 60
            if hours < 10:
                hours = '0' + str(hours)
            if minutes < 10:
                minutes = '0' + str(minutes)
            if seconds < 10:
                seconds = '0' + str(seconds)
            return str(hours) + ':' + str(minutes) + ':' + str(seconds)

        def intformat(int):
            l = list(str(int))
            for i in range(0, len(l) // 3):
                if len(l) + 1 - (i + 1) * 4 != 0:
                    l.insert(len(l) + 1 - (i + 1) * 4, ',')
            string = ''
            for i in l:
                string = string + i
            return string

        def filehash(self, path, algorithm):
            global Time, Time2, allsize, allsize1, information, size, ispause, iscancel
            size = os.path.getsize(path)  # 获取文件大小，单位是字节（byte）
            size1 = size
            if iscancel:
                raise OperationCancelledError(language.s112())
            with open(path, 'rb') as f:  # 以二进制模式读取文件
                Time1 = time.time()
                while size >= 1048576:  # 当文件大于1MB时将文件分块读取
                    if iscancel:
                        raise OperationCancelledError(language.s112())
                    if ispause:
                        while ispause:
                            if iscancel:
                                raise OperationCancelledError(language.s112())
                    Time3 = time.time()
                    algorithm.update(f.read(1024 * 1024))
                    size -= 1048576
                    allsize1 += 1048576
                    progress = ((size1 - size) / size1)
                    allprogress = (allsize1 / allsize)
                    Time1 = time.time()
                    check.m_staticText1.SetLabelText(language.s66() + timeformat(int((Time1 - Time) // 1)))
                    check.m_staticText4.SetLabelText(language.s67() + intformat(size1 - size) + ' ' + language.s73())
                    if (1048576 / (Time1 - Time3)) >= 1099511627776:  #1TB
                        check.m_staticText5.SetLabelText(language.s68() + str('%.2f' % (progress * 100)) + '% (' + str(
                            '%.2f' % (1048576 / (Time1 - Time3) / 1099511627776)) + ' TB/s)')
                    elif (1048576 / (Time1 - Time3)) >= 1073741824:  #1GB
                        check.m_staticText5.SetLabelText(language.s68() + str('%.2f' % (progress * 100)) + '% (' + str(
                            '%.2f' % (1048576 / (Time1 - Time3) / 1073741824)) + ' GB/s)')
                    elif (1048576 / (Time1 - Time3)) >= 1048576:  #1MB
                        check.m_staticText5.SetLabelText(language.s68() + str('%.2f' % (progress * 100)) + '% (' + str(
                            '%.2f' % (1048576 / (Time1 - Time3) / 1048576)) + ' MB/s)')
                    elif (1048576 / (Time1 - Time3)) >= 1024:  #1KB
                        check.m_staticText5.SetLabelText(language.s68() + str('%.2f' % (progress * 100)) + '% (' + str(
                            '%.2f' % (1048576 / (Time1 - Time3) / 1024)) + ' KB/s)')
                    else:
                        check.m_staticText5.SetLabelText(language.s68() + str('%.2f' % (progress * 100)) + '% (' + str(
                            '%.2f' % (1048576 / (Time1 - Time3))) + ' ' + language.s73() + '/s)')
                    check.m_gauge1.SetValue(int('%.0f' % (progress * 10000)))
                    check.m_staticText6.SetLabelText(language.s69() + str('%.2f' % (allprogress * 100)) + '%')
                    check.m_gauge2.SetValue(int('%.0f' % (allprogress * 10000)))
                algorithm.update(f.read())
            check.m_staticText5.SetLabelText(language.s68() + '100.00%')
            check.m_gauge1.SetValue(10000)
            allsize1 += size
            allprogress = (allsize1 / allsize)
            check.m_staticText4.SetLabelText(language.s67() + intformat(size1) + ' ' + language.s73())
            check.m_staticText6.SetLabelText(language.s69() + str('%.2f' % (allprogress * 100)) + '%')
            check.m_gauge2.SetValue(int('%.0f' % (allprogress * 10000)))
            information.append(timeformat(int(Time1 - Time2) // 1))
            Time2 = time.time()
            return algorithm.hexdigest()  # 输出计算结果

        def filecrc32(self, path):
            global Time, Time2, allsize, allsize1, information, size, ispause, iscancel
            size = os.path.getsize(path)  # 获取文件大小，单位是字节（byte）
            size1 = size
            crc = 0
            if iscancel:
                raise OperationCancelledError(language.s112())
            with open(path, 'rb') as f:  # 以二进制模式读取文件
                Time1 = time.time()
                while size >= 1048576:  # 当文件大于1MB时将文件分块读取
                    if iscancel:
                        raise OperationCancelledError(language.s112())
                    if ispause:
                        while ispause:
                            if iscancel:
                                raise OperationCancelledError(language.s112())
                    Time3 = time.time()
                    block = f.read(1024 * 1024)
                    size -= 1048576
                    allsize1 += 1048576
                    progress = ((size1 - size) / size1)
                    allprogress = (allsize1 / allsize)
                    Time1 = time.time()
                    check.m_staticText1.SetLabelText(language.s66() + timeformat(int((Time1 - Time) // 1)))
                    check.m_staticText4.SetLabelText(language.s67() + intformat(size1 - size) + ' ' + language.s73())
                    if (1048576 / (Time1 - Time3)) >= 1099511627776:  # 1TB
                        check.m_staticText5.SetLabelText(language.s68() + str('%.2f' % (progress * 100)) + '% (' + str(
                            '%.2f' % (1048576 / (Time1 - Time3) / 1099511627776)) + ' TB/s)')
                    elif (1048576 / (Time1 - Time3)) >= 1073741824:  # 1GB
                        check.m_staticText5.SetLabelText(language.s68() + str('%.2f' % (progress * 100)) + '% (' + str(
                            '%.2f' % (1048576 / (Time1 - Time3) / 1073741824)) + ' GB/s)')
                    elif (1048576 / (Time1 - Time3)) >= 1048576:  # 1MB
                        check.m_staticText5.SetLabelText(language.s68() + str('%.2f' % (progress * 100)) + '% (' + str(
                            '%.2f' % (1048576 / (Time1 - Time3) / 1048576)) + ' MB/s)')
                    elif (1048576 / (Time1 - Time3)) >= 1024:  # 1KB
                        check.m_staticText5.SetLabelText(language.s68() + str('%.2f' % (progress * 100)) + '% (' + str(
                            '%.2f' % (1048576 / (Time1 - Time3) / 1024)) + ' KB/s)')
                    else:
                        check.m_staticText5.SetLabelText(language.s68() + str('%.2f' % (progress * 100)) + '% (' + str(
                            '%.2f' % (1048576 / (Time1 - Time3))) + ' ' + language.s73() + '/s)')
                    check.m_gauge1.SetValue(int('%.0f' % (progress * 10000)))
                    check.m_staticText6.SetLabelText(language.s69() + str('%.2f' % (allprogress * 100)) + '%')
                    check.m_gauge2.SetValue(int('%.0f' % (allprogress * 10000)))
                    crc = zlib.crc32(block, crc)
                block = f.read()
                if block:
                    crc = zlib.crc32(block, crc)
            check.m_staticText5.SetLabelText(language.s68() + '100.00%')
            check.m_gauge1.SetValue(10000)
            allsize1 += size
            allprogress = (allsize1 / allsize)
            check.m_staticText4.SetLabelText(language.s67() + intformat(size1) + ' ' + language.s73())
            check.m_staticText6.SetLabelText(language.s69() + str('%.2f' % (allprogress * 100)) + '%')
            check.m_gauge2.SetValue(int('%.0f' % (allprogress * 10000)))
            information.append(timeformat(int(Time1 - Time2) // 1))
            Time2 = time.time()
            if len(str(hex(crc))[2:].lower()) < 8:
                return '0' * (8 - len(str(hex(crc))[2:].lower())) + str(hex(crc))[2:].lower()
            else:
                return str(hex(crc))[2:].lower()  # 输出计算结果

        def gethash():
            global Time, Time2, allsize, allsize1, ischeck, information, size, count, ispause, iscancel
            ischeck = True
            ispause = False
            iscancel = False
            self.SetStatusText(language.s82())
            self.m_menuItem1.Enable(False)
            self.m_menuItem2.Enable(False)
            self.m_menuItem8.Enable(False)
            self.m_menuItem4.Enable(False)
            self.m_menuItem9.Enable(False)
            self.m_menuItem3.Enable(False)
            self.m_menuItem10.Enable(False)
            self.m_menuItem172.Enable(False)
            self.m_menuItem171.Enable(False)
            self.m_choice1.Enable(False)
            self.m_choice4.Enable(False)
            self.m_button1.Enable(False)
            self.m_button6.Enable(False)
            self.m_button3.Enable(False)
            self.m_listCtrl2.Enable(False)
            listitems = []
            if self.m_choice4.GetSelection() == 0:
                for i in range(0, self.m_listCtrl2.GetItemCount()):
                    if self.m_listCtrl2.GetItemText(i, 1) == '':
                        listitems.append([int(self.m_listCtrl2.GetItemText(i, 0)), self.m_listCtrl2.GetItemText(i, 1),
                                          self.m_listCtrl2.GetItemText(i, 2), self.m_listCtrl2.GetItemText(i, 3)])
                    else:
                        listitems.append(
                            [int(self.m_listCtrl2.GetItemText(i, 0)), int(self.m_listCtrl2.GetItemText(i, 1)),
                             self.m_listCtrl2.GetItemText(i, 2), self.m_listCtrl2.GetItemText(i, 3)])
            elif self.m_choice4.GetSelection() == 1:
                for i in range(0, self.m_listCtrl2.GetItemCount()):
                    listitems.append(
                        [int(self.m_listCtrl2.GetItemText(i, 0)), self.m_listCtrl2.GetItemText(i, 1),
                         self.m_listCtrl2.GetItemText(i, 2), self.m_listCtrl2.GetItemText(i, 3)])
            listitems = sorted(listitems, key=lambda x: x[0],
                               reverse=False)
            count = 0
            count1 = 0
            allsize = 0
            allsize1 = 0
            size = 0
            information = []
            for i in range(0, frame.m_listCtrl2.GetItemCount()):
                if self.m_choice4.GetSelection() == 0:
                    if listitems[i][2] != '':
                        count = count + 1
                        try:
                            allsize = allsize + os.path.getsize(listitems[i][2])
                        except Exception:
                            continue
                elif self.m_choice4.GetSelection() == 1:
                    count = count + 1
                    try:
                        allsize = allsize + os.path.getsize(listitems[i][1])
                    except Exception:
                        continue


            if count != 0:
                check.Show()
            check.SetTitle('(' + str(count1) + '/' + str(count) + ')' + language.s70())
            check.m_staticText1.SetLabelText(language.s66() + '00:00:00')
            Time = time.time()
            Time2 = Time
            if self.m_choice4.GetSelection() == 0:
                columns = (2, 3)
            else:
            #elif self.m_choice4.GetSelection() == 1:
                columns = (1, 3)
            for i in range(0, frame.m_listCtrl2.GetItemCount()):
                size = 0
                if self.m_choice4.GetSelection() == 0 and listitems[i][columns[0]] == '':
                    information.append('')
                else:
                    count1 = count1 + 1
                    check.SetTitle('(' + str(count1) + '/' + str(count) + ') ' + language.s70())
                    check.m_staticText2.SetLabelText(language.s71() + listitems[i][columns[0]])
                    try:
                        if os.path.getsize(listitems[i][columns[0]]) >= 1099511627776:  # 1TB
                            check.m_staticText3.SetLabelText(language.s72() + str(
                                '%.2f' % (os.path.getsize(
                                    listitems[i][columns[0]]) / 1099511627776)) + ' TB (' + intformat(
                                os.path.getsize(listitems[i][columns[0]])) + ' ' + language.s73() + ')')
                        elif os.path.getsize(listitems[i][columns[0]]) >= 1073741824:  # 1GB
                            check.m_staticText3.SetLabelText(language.s72() + str(
                                '%.2f' % (os.path.getsize(
                                    listitems[i][columns[0]]) / 1073741824)) + ' GB (' + intformat(
                                os.path.getsize(listitems[i][columns[0]])) + ' ' + language.s73() + ')')
                        elif os.path.getsize(listitems[i][columns[0]]) >= 1048576:  # 1MB
                            check.m_staticText3.SetLabelText(language.s72() + str(
                                '%.2f' % (os.path.getsize(
                                    listitems[i][columns[0]]) / 1048576)) + ' MB (' + intformat(
                                os.path.getsize(listitems[i][columns[0]])) + ' ' + language.s73() + ')')
                        elif os.path.getsize(listitems[i][columns[0]]) >= 1024:  # 1KB
                            check.m_staticText3.SetLabelText(language.s72() + str(
                                '%.2f' % (os.path.getsize(
                                    listitems[i][columns[0]]) / 1024)) + ' KB (' + intformat(
                                os.path.getsize(listitems[i][columns[0]])) + ' ' + language.s73() + ')')
                        else:
                            check.m_staticText3.SetLabelText(language.s72() + str(
                                intformat(os.path.getsize(
                                    listitems[i][columns[0]]))) + ' ' + language.s73())
                        if self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'MD5':
                            listitems[i][columns[1]] = filehash(check, listitems[i][columns[0]],
                                                                     hashlib.md5())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA-1':
                            listitems[i][columns[1]] = filehash(check, listitems[i][columns[0]],
                                                                     hashlib.sha1())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA-224':
                            listitems[i][columns[1]] = filehash(check, listitems[i][columns[0]],
                                                                     hashlib.sha224())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA-256':
                            listitems[i][columns[1]] = filehash(check, listitems[i][columns[0]],
                                                                     hashlib.sha256())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA-384':
                            listitems[i][columns[1]] = filehash(check, listitems[i][columns[0]],
                                                                     hashlib.sha384())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA-512':
                            listitems[i][columns[1]] = filehash(check, listitems[i][columns[0]],
                                                                     hashlib.sha512())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA3-224':
                            listitems[i][columns[1]] = filehash(check, listitems[i][columns[0]],
                                                                     hashlib.sha3_224())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA3-256':
                            listitems[i][columns[1]] = filehash(check, listitems[i][columns[0]],
                                                                     hashlib.sha3_256())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA3-384':
                            listitems[i][columns[1]] = filehash(check, listitems[i][columns[0]],
                                                                     hashlib.sha3_384())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA3-512':
                            listitems[i][columns[1]] = filehash(check, listitems[i][columns[0]],
                                                                     hashlib.sha3_512())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'BLAKE2b':
                            listitems[i][columns[1]] = filehash(check, listitems[i][columns[0]],
                                                                     hashlib.blake2b())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'BLAKE2s':
                            listitems[i][columns[1]] = filehash(check, listitems[i][columns[0]],
                                                                     hashlib.blake2s())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'CRC-32':
                            listitems[i][columns[1]] = filecrc32(check, listitems[i][columns[0]])
                    except Exception as err:
                        information.append(type(err).__name__ + ': ' + str(err))
                        allsize1 = allsize1 + size
                        Time2 = time.time()
                        listitems[i][columns[1]] = language.s81()
                        continue
            ischeck = False
            check.Destroy()
            self.SetStatusText(language.s83())
            if self.m_choice4.GetSelection() == 0:
                group = []
                for i in range(0, self.m_listCtrl2.GetItemCount()):
                    tf = False
                    if listitems[i][3] != language.s81():
                        for ii in range(0, len(group)):
                            if listitems[i][3] == group[ii]:
                                listitems[i][1] = ii
                                tf = True
                                break
                        if not tf:
                            group.append(listitems[i][3])
                            listitems[i][1] = len(group) - 1
            elif self.m_choice4.GetSelection() == 1:
                for i in range(0, self.m_listCtrl2.GetItemCount()):
                    if listitems[i][3] != language.s81():
                        if listitems[i][3] == listitems[i][2]:
                            listitems[i][3] = 1
                        else:
                            listitems[i][3] = 0
            if self.m_listCtrl2.GetSortIndicator() != -1:
                listitems = sorted(listitems, key=lambda x: x[self.m_listCtrl2.GetSortIndicator()],
                                   reverse=not self.m_listCtrl2.IsAscendingSortIndicator())
            for i in range(0, len(listitems)):
                self.m_listCtrl2.SetItem(i, 0, str(listitems[i][0]))
                self.m_listCtrl2.SetItem(i, 1, str(listitems[i][1]))
                self.m_listCtrl2.SetItem(i, 2, str(listitems[i][2]))
                self.m_listCtrl2.SetItem(i, 3, str(listitems[i][3]))
                if self.m_choice4.GetSelection() == 1:
                    if str(listitems[i][3]) == '1':
                        self.m_listCtrl2.SetItemBackgroundColour(i, wx.Colour(198, 239, 206))    #Green
                    elif str(listitems[i][3]) == language.s81():
                        self.m_listCtrl2.SetItemBackgroundColour(i, wx.Colour(255, 235, 156))    #Yellow
                    elif str(listitems[i][3]) == '0':
                        self.m_listCtrl2.SetItemBackgroundColour(i, wx.Colour(255, 199, 206))    #Red
            self.m_menuItem1.Enable(True)
            self.m_menuItem2.Enable(True)
            self.m_menuItem8.Enable(True)
            self.m_menuItem4.Enable(True)
            self.m_menuItem9.Enable(True)
            self.m_menuItem3.Enable(True)
            self.m_menuItem10.Enable(True)
            self.m_menuItem172.Enable(True)
            self.m_menuItem171.Enable(True)
            self.m_choice1.Enable(True)
            self.m_choice4.Enable(True)
            self.m_button1.Enable(True)
            self.m_button6.Enable(True)
            self.m_button3.Enable(True)
            self.m_listCtrl2.Enable(True)
            self.SetStatusText('')
            if isexport:
                self.SetStatusText(language.s84() + export)
                main.export(self, export)
            if command != '':
                self.SetStatusText(language.s85() + command)
                try:
                    os.startfile(command)
                except FileNotFoundError:
                    try:
                        os.popen(command)
                    except Exception as err:
                        toastone = wx.MessageDialog(None, language.s75(type(err).__name__ + ': ' + str(err)),
                                                    language.s81(),
                                                    wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                        toastone.SetOKLabel(language.s57())
                        if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                            toastone.Destroy()
                except Exception as err:
                    toastone = wx.MessageDialog(None, language.s75(type(err).__name__ + ': ' + str(err)),
                                                language.s81(),
                                                wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                    toastone.SetOKLabel(language.s57())
                    if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                        toastone.Destroy()
            self.SetStatusText('')

        thread1 = threading.Thread(target=gethash, args=(), daemon=True)
        thread1.start()

    def addfile(self, event):
        global information
        if self.m_choice4.GetSelection() == 0:
            dlg = wx.FileDialog(self, message=language.s22(),
                                defaultDir='',
                                defaultFile='',
                                wildcard=language.s23(),
                                style=wx.FD_OPEN | wx.FD_MULTIPLE)
            if dlg.ShowModal() == wx.ID_OK:
                fahs = dlg.GetPaths()
                dlg.Destroy()
                for fah in fahs:
                    index = frame.m_listCtrl2.InsertItem(frame.m_listCtrl2.GetItemCount(),
                                                         str(frame.m_listCtrl2.GetItemCount() + 1))
                    frame.m_listCtrl2.SetItem(index, 1, '')
                    frame.m_listCtrl2.SetItem(index, 2, fah)
                    frame.m_listCtrl2.SetItem(index, 3, '')
                    information.append('/')
                frame.sort(None)
        elif self.m_choice4.GetSelection() == 1:
            self.additem = MyDialog8(None)
            self.additem.Show(True)

    def addhash(self, event):
        addhash = MyDialog2(None, language.s42())
        addhash.Show()

    def inputtask(self, event):
        global file
        if self.m_choice4.GetSelection() == 0:
            dlg = wx.FileDialog(self, message=language.s49(),
                                defaultDir='',
                                defaultFile='',
                                wildcard=language.s48(),
                                style=wx.FD_OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                file = dlg.GetPath()
                dlg.Destroy()
                try:
                    with open(file, 'rb') as f:
                        coding = f.readline().decode('ascii').rstrip()
                except UnicodeDecodeError:
                    with open(file, 'rb') as f:
                        coding = f.readline()
                    if coding.startswith(b'\xef\xbb\xbf'):
                        try:
                            intask(file, 'utf-8')
                        except UnicodeDecodeError:
                            encodingpick = MyDialog5(None, 'utf-8')
                            encodingpick.Show()
                    elif coding.startswith(b'\x00\x00\xfe\xff') or coding.startswith(b'\xff\xfe\x00\x00'):
                        try:
                            intask(file, 'utf-32')
                        except UnicodeDecodeError:
                            encodingpick = MyDialog5(None, 'utf-32')
                            encodingpick.Show()
                    elif coding.startswith(b'\xfe\xff') or coding.startswith(b'\xff\xfe'):
                        try:
                            intask(file, 'utf-16')
                        except UnicodeDecodeError:
                            encodingpick = MyDialog5(None, 'utf-16')
                            encodingpick.Show()
                    elif coding.startswith(b'\x2b\x2f\x76'):
                        try:
                            intask(file, 'utf-7')
                        except UnicodeDecodeError:
                            encodingpick = MyDialog5(None, 'utf-7')
                            encodingpick.Show()
                    elif coding.startswith(b'\x84\x31\x95\x33'):
                        try:
                            intask(file, 'gb18030')
                        except UnicodeDecodeError:
                            encodingpick = MyDialog5(None, 'gb18030')
                            encodingpick.Show()
                    else:
                        encodingpick = MyDialog5(None, 'utf-8')
                        encodingpick.Show()
                else:
                    if coding[:9] == '# coding=':
                        try:
                            with open(file, 'r', encoding=coding[9:]) as f:
                                f.read()
                        except (UnicodeDecodeError, LookupError):
                            encodingpick = MyDialog5(None, coding[9:])
                            encodingpick.Show()
                        else:
                            intask(file, coding[9:])
                    elif coding[:8] == '#coding=':
                        try:
                            with open(file, 'r', encoding=coding[8:]) as f:
                                f.read()
                        except (UnicodeDecodeError, LookupError):
                            encodingpick = MyDialog5(None, coding[8:])
                            encodingpick.Show()
                        else:
                            intask(file, coding[8:])
                    else:
                        encodingpick = MyDialog5(None, 'utf-8')
                        encodingpick.Show()
        elif self.m_choice4.GetSelection() == 1:
            self.inputshafile = MyDialog9(None)
            self.inputshafile.Show()

    def outputtask(self, event):
        dlg = wx.FileDialog(self, message=language.s60(),
                            defaultDir='',
                            defaultFile='',
                            wildcard=language.s48(),
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText(language.s86() + dlg.GetPath())
            try:
                with open(dlg.GetPath(), 'w', encoding=setting['SaveTaskEncoding']) as file:
                    dlg.Destroy()
                    if self.m_choice4.GetSelection() == 0:
                        f = '# coding=' + setting['SaveTaskEncoding'] + '\n' + frame.m_choice1.GetString(
                            frame.m_choice1.GetSelection()) + '\n'
                        if frame.m_listCtrl2.GetItemCount() != 0:
                            foha = ''
                            for i in range(0, frame.m_listCtrl2.GetItemCount()):
                                if frame.m_listCtrl2.GetItemText(i, 2) == '' and foha != 2:
                                    foha = 2
                                    f = f + '<hash>\n' + frame.m_listCtrl2.GetItemText(i, 3) + '\n'
                                elif frame.m_listCtrl2.GetItemText(i, 2) == '' and foha == 2:
                                    f = f + frame.m_listCtrl2.GetItemText(i, 3) + '\n'
                                elif frame.m_listCtrl2.GetItemText(i, 2) != '' and foha != 1:
                                    foha = 1
                                    f = f + '<file>\n' + frame.m_listCtrl2.GetItemText(i, 2).replace('#', '##') + '\n'
                                elif frame.m_listCtrl2.GetItemText(i, 2) != '' and foha == 1:
                                    f = f + frame.m_listCtrl2.GetItemText(i, 2).replace('#', '##') + '\n'
                    elif self.m_choice4.GetSelection() == 1:
                        f = ''
                        for i in range(0, frame.m_listCtrl2.GetItemCount()):
                            if frame.m_listCtrl2.GetItemText(i, 2):
                                f += frame.m_listCtrl2.GetItemText(i, 2) + ' ' + frame.m_listCtrl2.GetItemText(i, 1) + '\n'
                            else:
                                f += '<empty> ' + frame.m_listCtrl2.GetItemText(i, 1) + '\n'
                    file.write(f)
            except Exception as err:
                toastone = wx.MessageDialog(None, language.s75(type(err).__name__ + ': ' + str(err)), language.s81(),
                                            wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                toastone.SetOKLabel(language.s57())
                if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                    toastone.Destroy()
            self.SetStatusText('')

    def outputreport(self, event):
        dlg = wx.FileDialog(self, message=language.s60(),
                            defaultDir='',
                            defaultFile='',
                            wildcard=language.s33(),
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            dlg.Destroy()
            self.SetStatusText(language.s84() + path)
            main.export(self, path)
            self.SetStatusText('')

    def clear(self, event):
        global information
        self.m_listCtrl2.DeleteAllItems()
        information = []

    def work_directory(self, event):
        dlg = wx.DirDialog(self, message=language.s136(),
                           defaultPath='',
                           style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            os.chdir(dlg.GetPath())
            self.SetStatusText(os.getcwd(), 1)

    def setting(self, event):
        setting = MyDialog1(None)
        setting.Show()

    def about(self, event):
        addhash = MyDialog3(None)
        addhash.Show()

    def rightmenu(self, event):
        self.m_menuItem13.Enable(True)
        self.m_menuItem14.Enable(True)
        self.m_menuItem16.Enable(True)
        self.m_menuItem17.Enable(True)
        if self.m_choice4.GetSelection() == 0:
            if self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 2) == '':
                self.m_menuItem13.Enable(False)
                self.m_menuItem16.Enable(False)
            if self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(),
                                            3) == '' or self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(),
                                                                                      3) == language.s81():
                self.m_menuItem14.Enable(False)
            if self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 2) != '':
                self.m_menuItem17.Enable(False)
        elif self.m_choice4.GetSelection() == 1:
            if self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(),
                                            2) == '':
                self.m_menuItem14.Enable(False)
        self.PopupMenu(self.m_menu4)

    def showinformation(self, event):
        informationdialog = MyDialog6(None)
        informationdialog.Show()

    def editfile(self, event):
        global information
        dlg = wx.FileDialog(self, message=language.s87(),
                            defaultDir=os.path.dirname(
                                self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 2)),
                            defaultFile='',
                            wildcard=language.s23(),
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            fahs = dlg.GetPath()
            dlg.Destroy()
            if self.m_choice4.GetSelection() == 0:
                self.m_listCtrl2.SetItem(self.m_listCtrl2.GetFocusedItem(), 1, '')
                self.m_listCtrl2.SetItem(self.m_listCtrl2.GetFocusedItem(), 2, fahs)
            elif self.m_choice4.GetSelection() == 1:
                self.m_listCtrl2.SetItem(self.m_listCtrl2.GetFocusedItem(), 1, fahs)
                self.m_listCtrl2.SetItemBackgroundColour(self.m_listCtrl2.GetFocusedItem(), wx.Colour(-1, -1, -1))
            self.m_listCtrl2.SetItem(self.m_listCtrl2.GetFocusedItem(), 3, '')
            information[int(self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 0))-1] = '/'
            self.sort(None)

    def edithash(self, event):
        addhash = MyDialog2(None, language.s88())
        addhash.Show()

    def copyfile(self, event):
        if self.m_choice4.GetSelection() == 0:
            pyperclip.copy(self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 2))
        elif self.m_choice4.GetSelection() == 1:
            pyperclip.copy(self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 1))
        self.SetStatusText(language.s89())

    def copyhash(self, event):
        if self.m_choice4.GetSelection() == 0:
            pyperclip.copy(self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 3))
        elif self.m_choice4.GetSelection() == 1:
            pyperclip.copy(self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 2))
        self.SetStatusText(language.s89())

    def delete(self, event):
        global information
        del information[int(self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 0)) - 1]
        self.m_listCtrl2.DeleteItem(self.m_listCtrl2.GetFocusedItem())
        listitems = []
        for i in range(0, self.m_listCtrl2.GetItemCount()):
            if self.m_listCtrl2.GetItemText(i, 1) == '':
                listitems.append([int(self.m_listCtrl2.GetItemText(i, 0)), -1,
                                  self.m_listCtrl2.GetItemText(i, 2), self.m_listCtrl2.GetItemText(i, 3)])
            else:
                listitems.append([int(self.m_listCtrl2.GetItemText(i, 0)), int(self.m_listCtrl2.GetItemText(i, 1)),
                                  self.m_listCtrl2.GetItemText(i, 2), self.m_listCtrl2.GetItemText(i, 3)])
        listitems = sorted(listitems, key=lambda x: x[0],
                           reverse=False)
        for i in range(0, self.m_listCtrl2.GetItemCount()):
            listitems[i][0] = i + 1
        if self.m_listCtrl2.GetSortIndicator() != -1:
            listitems = sorted(listitems, key=lambda x: x[self.m_listCtrl2.GetSortIndicator()],
                               reverse=not self.m_listCtrl2.IsAscendingSortIndicator())
        for i in range(0, len(listitems)):
            self.m_listCtrl2.SetItem(i, 0, str(listitems[i][0]))
            if listitems[i][1] == -1:
                self.m_listCtrl2.SetItem(i, 1, '')
            else:
                self.m_listCtrl2.SetItem(i, 1, str(listitems[i][1]))
            self.m_listCtrl2.SetItem(i, 2, listitems[i][2])
            self.m_listCtrl2.SetItem(i, 3, listitems[i][3])

    def setsort(self, event):
        if self.m_listCtrl2.GetSortIndicator() == -1 or self.m_listCtrl2.GetSortIndicator() != event.GetColumn():
            self.m_listCtrl2.ShowSortIndicator(event.GetColumn(), True)
        else:
            self.m_listCtrl2.ShowSortIndicator(event.GetColumn(), not self.m_listCtrl2.IsAscendingSortIndicator())
        self.sort(None)

    def sort(self, event):
        listitems = []
        if self.m_listCtrl2.GetSortIndicator() != -1:
            if self.m_choice4.GetSelection() == 0:
                for i in range(0, self.m_listCtrl2.GetItemCount()):
                    if self.m_listCtrl2.GetItemText(i, 1) == '':
                        listitems.append([int(self.m_listCtrl2.GetItemText(i, 0)), -1,
                                          self.m_listCtrl2.GetItemText(i, 2), self.m_listCtrl2.GetItemText(i, 3)])
                    else:
                        listitems.append(
                            [int(self.m_listCtrl2.GetItemText(i, 0)), int(self.m_listCtrl2.GetItemText(i, 1)),
                             self.m_listCtrl2.GetItemText(i, 2), self.m_listCtrl2.GetItemText(i, 3)])
                listitems = sorted(listitems, key=lambda x: x[self.m_listCtrl2.GetSortIndicator()],
                                   reverse=not self.m_listCtrl2.IsAscendingSortIndicator())
                for i in range(0, len(listitems)):
                    self.m_listCtrl2.SetItem(i, 0, str(listitems[i][0]))
                    if listitems[i][1] == -1:
                        self.m_listCtrl2.SetItem(i, 1, '')
                    else:
                        self.m_listCtrl2.SetItem(i, 1, str(listitems[i][1]))
                    self.m_listCtrl2.SetItem(i, 2, listitems[i][2])
                    self.m_listCtrl2.SetItem(i, 3, listitems[i][3])
            elif self.m_choice4.GetSelection() == 1:
                for i in range(0, self.m_listCtrl2.GetItemCount()):
                    if self.m_listCtrl2.GetItemText(i, 3) == '':
                        listitems.append(
                            [int(self.m_listCtrl2.GetItemText(i, 0)), self.m_listCtrl2.GetItemText(i, 1),
                             self.m_listCtrl2.GetItemText(i, 2), -1])
                    elif self.m_listCtrl2.GetItemText(i, 3) == language.s81():
                        listitems.append(
                            [int(self.m_listCtrl2.GetItemText(i, 0)), self.m_listCtrl2.GetItemText(i, 1),
                             self.m_listCtrl2.GetItemText(i, 2), -2])
                    else:
                        listitems.append([int(self.m_listCtrl2.GetItemText(i, 0)), self.m_listCtrl2.GetItemText(i, 1),
                                          self.m_listCtrl2.GetItemText(i, 2), int(self.m_listCtrl2.GetItemText(i, 3))])
                listitems = sorted(listitems, key=lambda x: x[self.m_listCtrl2.GetSortIndicator()],
                                   reverse=not self.m_listCtrl2.IsAscendingSortIndicator())
                for i in range(0, len(listitems)):
                    self.m_listCtrl2.SetItem(i, 0, str(listitems[i][0]))
                    if listitems[i][3] == -1:
                        self.m_listCtrl2.SetItem(i, 3, '')
                        self.m_listCtrl2.SetItemBackgroundColour(i, wx.Colour(-1, -1, -1))
                    elif listitems[i][3] == -2:
                        self.m_listCtrl2.SetItem(i, 3, language.s81())
                        self.m_listCtrl2.SetItemBackgroundColour(i, wx.Colour(255, 235, 156))    #Yellow
                    else:
                        self.m_listCtrl2.SetItem(i, 3, str(listitems[i][3]))
                        if str(listitems[i][3]) == '1':
                            self.m_listCtrl2.SetItemBackgroundColour(i, wx.Colour(198, 239, 206))    #Green
                        elif str(listitems[i][3]) == '0':
                            self.m_listCtrl2.SetItemBackgroundColour(i, wx.Colour(255, 199, 206))    #Red
                    self.m_listCtrl2.SetItem(i, 1, listitems[i][1])
                    self.m_listCtrl2.SetItem(i, 2, listitems[i][2])

        #self.m_listCtrl2.IsAscendingSortIndicator()
        #self.m_listCtrl2.GetSortIndicator()

    def switchmode(self, event):
        if self.m_choice4.GetSelection() != self.mode:
            if self.m_listCtrl2.GetItemCount():
                toastone = wx.MessageDialog(None, language.s137(), language.s1(),
                                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)
                toastone.SetYesNoLabels(language.s63(), language.s64())
                if toastone.ShowModal() == wx.ID_NO:  # 如果点击了提示框的否按钮
                    toastone.Destroy()
                    self.m_choice4.SetSelection(self.mode)
                    return None
            self.m_listCtrl2.DeleteAllItems()
            self.m_listCtrl2.RemoveSortIndicator()
            self.m_listCtrl2.DeleteAllColumns()
            if self.m_choice4.GetSelection() == 0:
                self.m_listCtrl2.InsertColumn(0, language.s17())
                self.m_listCtrl2.InsertColumn(1, language.s18())
                self.m_listCtrl2.InsertColumn(2, language.s19())
                self.m_listCtrl2.InsertColumn(3, language.s20())
                self.m_listCtrl2.SetColumnWidth(0, int('%.0f' % (50 * self.GetDPI()[0] / 96)))  # 设置每一列的宽度
                self.m_listCtrl2.SetColumnWidth(1, int('%.0f' % (50 * self.GetDPI()[0] / 96)))
                self.m_listCtrl2.SetColumnWidth(2, int('%.0f' % (425 * self.GetDPI()[0] / 96)))
                self.m_listCtrl2.SetColumnWidth(3, int('%.0f' % (445 * self.GetDPI()[0] / 96)))
                fileDrop = FileDrop()
                self.m_listCtrl2.SetDropTarget(fileDrop)
                self.m_menuItem2.SetItemLabel(language.s3() + '\tCtrl+F')
                self.m_menu3.Insert(3, self.m_menuItem8)
                self.m_menuItem2.SetHelp(language.s98())
                self.m_button1.SetLabel(language.s14())
                self.m_button6.Show(True)
                self.m_toolBar1.InsertControl(3, self.m_button6)
                self.m_toolBar1.Realize()
            elif self.m_choice4.GetSelection() == 1:
                self.m_listCtrl2.InsertColumn(0, language.s17())
                self.m_listCtrl2.InsertColumn(1, language.s19())
                self.m_listCtrl2.InsertColumn(2, language.s134())
                self.m_listCtrl2.InsertColumn(3, language.s135())
                self.m_listCtrl2.SetColumnWidth(0, int('%.0f' % (50 * self.GetDPI()[0] / 96)))  # 设置每一列的宽度
                self.m_listCtrl2.SetColumnWidth(1, int('%.0f' % (425 * self.GetDPI()[0] / 96)))
                self.m_listCtrl2.SetColumnWidth(2, int('%.0f' % (425 * self.GetDPI()[0] / 96)))
                self.m_listCtrl2.SetColumnWidth(3, int('%.0f' % (75 * self.GetDPI()[0] / 96)))
                self.m_listCtrl2.SetDropTarget(None)
                self.m_menuItem2.SetItemLabel(language.s131() + '\tCtrl+F')
                self.m_menu3.Remove(self.m_menuItem8)
                self.m_menuItem2.SetHelp(language.s132())
                self.m_button1.SetLabel(language.s133())
                self.m_button6.Show(False)
                self.m_toolBar1.RemoveTool(self.m_button6.GetId())
                self.m_toolBar1.Realize()
            self.mode = self.m_choice4.GetSelection()
        return None

    def getupdate(self, event):
        #updatedialog = MyDialog7(None)
        updatedialog.Show()
        self.Enable(False)


class MyDialog1(wx.Dialog):

    def __init__(self, parent):
        global command, export, isexport, languagelist
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=language.s24(), pos=wx.DefaultPosition,
                           size=wx.Size(600, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.SetSize(wx.Size(int('%.0f' % (600 * self.GetDPI()[0] / 96)),
                                        int('%.0f' % (400 * self.GetDPI()[0] / 96))))
        main.Disable(frame)

        self.SetSizeHints(wx.Size(int('%.0f' % (600 * self.GetDPI()[0] / 96)),
                                  int('%.0f' % (400 * self.GetDPI()[0] / 96))),
                          wx.Size(int('%.0f' % (600 * self.GetDPI()[0] / 96)),
                                  int('%.0f' % (400 * self.GetDPI()[0] / 96))))

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_listbook1 = wx.Listbook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT)
        list_ctrl = self.m_listbook1.GetListView()
        list_ctrl.SetColumnWidth(0, int('%.0f' % (80 * self.GetDPI()[0] / 96)))
        self.m_panel1 = wx.Panel(self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel1, wx.ID_ANY, language.s148()), wx.VERTICAL)

        gSizer8 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText20 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, language.s149(), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)

        gSizer8.Add(self.m_staticText20, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice5Choices = language.s130()
        self.m_choice5 = wx.Choice(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   m_choice5Choices, 0)
        self.m_choice5.SetSelection(setting['DefaultCheckMode'])
        gSizer8.Add(self.m_choice5, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        sbSizer6.Add(gSizer8, 1, wx.EXPAND, 5)

        bSizer7.Add(sbSizer6, 0, wx.EXPAND, 5)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel1, wx.ID_ANY, language.s25()), wx.VERTICAL)

        self.m_staticText10 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, language.s90(), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        sbSizer1.Add(self.m_staticText10, 0, wx.ALL, 5)

        gSizer4 = wx.GridSizer(2, 4, 0, 0)

        self.m_radioBtn1 = wx.RadioButton(sbSizer1.GetStaticBox(), wx.ID_ANY, language.s26(), wx.DefaultPosition,
                                          wx.DefaultSize, wx.RB_GROUP)
        self.m_radioBtn1.SetValue(True)
        gSizer4.Add(self.m_radioBtn1, 0, wx.ALL, 5)

        self.m_radioBtn2 = wx.RadioButton(sbSizer1.GetStaticBox(), wx.ID_ANY, language.s27(), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        gSizer4.Add(self.m_radioBtn2, 0, wx.ALL, 5)

        self.m_radioBtn3 = wx.RadioButton(sbSizer1.GetStaticBox(), wx.ID_ANY, language.s28(), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        gSizer4.Add(self.m_radioBtn3, 0, wx.ALL, 5)

        self.m_radioBtn4 = wx.RadioButton(sbSizer1.GetStaticBox(), wx.ID_ANY, language.s29(), wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        gSizer4.Add(self.m_radioBtn4, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(int('%.0f' % (450 * self.GetDPI()[0] / 96)), -1), 0)
        self.m_textCtrl4.SetValue(command)
        if command == '':
            self.m_radioBtn1.SetValue(True)
        elif command == 'shutdown -s -t 0':
            self.m_radioBtn2.SetValue(True)
        elif command == 'shutdown -r -t 0':
            self.m_radioBtn3.SetValue(True)
        else:
            self.m_radioBtn4.SetValue(True)
        gSizer4.Add(self.m_textCtrl4, 0, wx.ALL, 5)

        sbSizer1.Add(gSizer4, 1, wx.EXPAND, 5)

        bSizer7.Add(sbSizer1, 0, wx.EXPAND, 5)

        sbSizer7 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel1, wx.ID_ANY, language.s30()), wx.VERTICAL)

        self.m_checkBox2 = wx.CheckBox(sbSizer7.GetStaticBox(), wx.ID_ANY, language.s31(), wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.m_checkBox2.SetValue(isexport)
        sbSizer7.Add(self.m_checkBox2, 0, wx.ALL, 5)

        self.m_filePicker2 = wx.FilePickerCtrl(sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, language.s32(),
                                               language.s33(),
                                               wx.DefaultPosition,
                                               wx.Size(int('%.0f' % (450 * self.GetDPI()[0] / 96)), -1),
                                               wx.FLP_SAVE | wx.FLP_OVERWRITE_PROMPT | wx.FLP_SMALL | wx.FLP_USE_TEXTCTRL)
        if not isexport:
            self.m_filePicker2.Enable(False)

        self.m_filePicker2.SetPath(export)

        sbSizer7.Add(self.m_filePicker2, 0, wx.ALL, 5)
        bSizer7.Add(sbSizer7, 0, wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer7)
        self.m_panel1.Layout()
        bSizer7.Fit(self.m_panel1)
        self.m_listbook1.AddPage(self.m_panel1, language.s34(), True)

        self.m_panel3 = wx.Panel(self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel3, wx.ID_ANY, language.s106()), wx.VERTICAL)

        gSizer5 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText12 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, language.s107(),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)

        gSizer5.Add(self.m_staticText12, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice2Choices = ['ANSI', 'ASCII', 'BIG5', 'BIG5HKSCS', 'CP037', 'CP273', 'CP424', 'CP437', 'CP500', 'CP720',
                             'CP737', 'CP775', 'CP850', 'CP852', 'CP855', 'CP856', 'CP857', 'CP858', 'CP860', 'CP861',
                             'CP862', 'CP863', 'CP864', 'CP865', 'CP866', 'CP869', 'CP874', 'CP875', 'CP932', 'CP949',
                             'CP950', 'CP1006', 'CP1026', 'CP1125', 'CP1140', 'CP1250', 'CP1251', 'CP1252', 'CP1253',
                             'CP1254', 'CP1255', 'CP1256', 'CP1257', 'CP1258', 'EUC_JP', 'EUC_JIS_2004', 'EUC_JISX0213',
                             'EUC_KR', 'GB2312', 'GBK', 'GB18030', 'HZ', 'ISO2022_JP', 'ISO2022_JP_1', 'ISO2022_JP_2',
                             'ISO2022_JP_2004', 'ISO2022_JP_3', 'ISO2022_JP_EXT', 'ISO2022_KR', 'LATIN_1', 'ISO8859_2',
                             'ISO8859_3', 'ISO8859_4', 'ISO8859_5', 'ISO8859_6', 'ISO8859_7', 'ISO8859_8', 'ISO8859_9',
                             'ISO8859_10', 'ISO8859_11', 'ISO8859_13', 'ISO8859_14', 'ISO8859_15', 'ISO8859_16',
                             'JOHAB', 'KOI8_R', 'KOI8_T', 'KOI8_U', 'KZ1048', 'MAC_CYRILLIC', 'MAC_GREEK',
                             'MAC_ICELAND', 'MAC_LATIN2', 'MAC_ROMAN', 'MAC_TURKISH', 'OEM', 'PTCP154', 'SHIFT_JIS',
                             'SHIFT_JIS_2004', 'SHIFT_JISX0213', 'UTF_32', 'UTF_32_BE', 'UTF_32_LE', 'UTF_16',
                             'UTF_16_BE', 'UTF_16_LE', 'UTF_7', 'UTF_8', 'UTF_8_SIG']
        self.m_choice2 = wx.Choice(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   m_choice2Choices, 0)
        if find_encoding_key(setting['SaveTaskEncoding']) not in m_choice2Choices:
            self.m_choice2.SetSelection(m_choice2Choices.index('UTF_8'))
            setting['SaveTaskEncoding'] = 'UTF_8'
        else:
            self.m_choice2.SetSelection(m_choice2Choices.index(find_encoding_key(setting['SaveTaskEncoding'])))
        gSizer5.Add(self.m_choice2, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer4.Add(gSizer5, 1, wx.EXPAND, 5)

        bSizer12.Add(sbSizer4, 0, wx.EXPAND, 5)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel3, wx.ID_ANY, language.s108()), wx.VERTICAL)

        gSizer6 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText13 = wx.StaticText(sbSizer5.GetStaticBox(), wx.ID_ANY, language.s109(),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)

        gSizer6.Add(self.m_staticText13, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice3Choices = m_choice2Choices
        self.m_choice3 = wx.Choice(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   m_choice3Choices, 0)
        if find_encoding_key(setting['ExportResultEncoding']) not in m_choice3Choices:
            self.m_choice3.SetSelection(m_choice3Choices.index('ANSI'))
            setting['ExportResultEncoding'] = 'ANSI'
        else:
            self.m_choice3.SetSelection(m_choice3Choices.index(find_encoding_key(setting['ExportResultEncoding'])))
        with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.json'), 'w',
                  encoding='utf-8') as settingfile:
            settingfile.write(json.dumps(setting))
        gSizer6.Add(self.m_choice3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        sbSizer5.Add(gSizer6, 1, wx.EXPAND, 5)

        bSizer12.Add(sbSizer5, 0, wx.EXPAND, 5)

        self.m_button7 = wx.Button(self.m_panel3, wx.ID_ANY, language.s110(), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button7, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_panel3.SetSizer(bSizer12)
        self.m_panel3.Layout()
        bSizer12.Fit(self.m_panel3)
        self.m_listbook1.AddPage(self.m_panel3, language.s111(), False)

        self.m_panel2 = wx.Panel(self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, language.s35()), wx.VERTICAL)

        gSizer3 = wx.GridSizer(0, 6, 0, 0)

        self.m_button2 = wx.Button(sbSizer3.GetStaticBox(), wx.ID_ANY, language.s37(), wx.DefaultPosition, wx.DefaultSize,
                                   0)

        gSizer3.Add(self.m_button2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer3.Add(gSizer3, 0, wx.EXPAND, 5)
        '''
        languagelist = glob.glob('language_*.py')
        for i in range(len(languagelist)):
            languagelist[i] = languagelist[i].split(".")[0]
        code = 'def get():\n    list = []\n'
        for i in range(0, len(languagelist)):
            code = code + '    import ' + languagelist[i] + '\n    list.append(' + languagelist[i] + '.LANGUAGE[1])\n'
        code = code + '    return list'
        with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'getlanguagelist.py'), 'w',
                  encoding='utf-8') as f:
            f.write(code)
        import getlanguagelist
        reload(getlanguagelist)
        displanguagelist = getlanguagelist.get()

        print(languagelist)
        print(displanguagelist)
        '''
        languagelist = []
        for i in languagedic.values():
            if i[0] not in languagelist:
                languagelist.append(i[0])
        displanguagelist = []
        for i in languagedic.values():
            if i[1] not in displanguagelist:
                displanguagelist.append(i[1])
        m_listBox2Choices = [language.s21()]
        m_listBox2Choices.extend(displanguagelist)
        self.m_listBox2 = wx.ListBox(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(480, 290),
                                     m_listBox2Choices, wx.LB_NEEDED_SB | wx.LB_SINGLE)
        sbSizer3.Add(self.m_listBox2, 1, wx.ALL | wx.EXPAND, 5)

        if setting['Language'] == 'Auto':
            self.m_listBox2.SetSelection(0)
        else:
            self.m_listBox2.SetSelection(languagelist.index(setting['Language']) + 1)

        bSizer6.Add(sbSizer3, 1, wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer6)
        self.m_panel2.Layout()
        bSizer6.Fit(self.m_panel2)
        self.m_listbook1.AddPage(self.m_panel2, language.s40(), False)

        bSizer5.Add(self.m_listbook1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.close)
        self.m_button7.Bind(wx.EVT_BUTTON, self.recover)
        self.m_radioBtn1.Bind(wx.EVT_RADIOBUTTON, self.none)
        self.m_radioBtn2.Bind(wx.EVT_RADIOBUTTON, self.shutdown)
        self.m_radioBtn3.Bind(wx.EVT_RADIOBUTTON, self.reboot)
        self.m_radioBtn4.Bind(wx.EVT_RADIOBUTTON, self.custom)
        self.m_textCtrl4.Bind(wx.EVT_TEXT, self.getcmd)
        self.m_checkBox2.Bind(wx.EVT_CHECKBOX, self.autosave)
        self.m_button2.Bind(wx.EVT_BUTTON, self.changelanguage)
        self.m_listBox2.Bind(wx.EVT_LISTBOX_DCLICK, self.changelanguage)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def close(self, event):
        global command, export, isexport
        command = self.m_textCtrl4.GetValue()
        if self.m_filePicker2.GetPath() == '' and self.m_checkBox2.GetValue() == True:
            toastone = wx.MessageDialog(None, language.s91(), language.s81(),
                                        wx.OK_DEFAULT | wx.ICON_ERROR)
            toastone.SetOKLabel(language.s57())
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
        else:
            isexport = self.m_checkBox2.GetValue()
            export = self.m_filePicker2.GetPath()
            setting['DefaultCheckMode'] = self.m_choice5.GetSelection()
            setting['SaveTaskEncoding'] = self.m_choice2.GetStringSelection()
            setting['ExportResultEncoding'] = self.m_choice3.GetStringSelection()
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.json'), 'w',
                      encoding='utf-8') as settingfile:
                settingfile.write(json.dumps(setting))
            main.Enable(frame)
            self.Destroy()

    def recover(self, event):
        self.m_choice2.SetSelection(97)
        self.m_choice3.SetSelection(0)

    def changelanguage(self, event):
        global languagelist
        if locale not in languagedic.keys() and self.m_listBox2.GetSelection() == 0:
            toastone = wx.MessageDialog(None, language.s46(), language.s81(),
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
            toastone.SetOKLabel(language.s57())
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
        else:
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'newlanguage.py'),
                      'w', encoding='utf-8') as f:
                if self.m_listBox2.GetSelection() == 0:
                    f.write('from ' + languagedic[locale][0] + ' import *')
                else:
                    f.write('from ' + languagelist[self.m_listBox2.GetSelection() - 1] + ' import *')
            import newlanguage
            reload(newlanguage)
            toastone = wx.MessageDialog(None, newlanguage.s39(), newlanguage.s1(),
                                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)
            toastone.SetYesNoLabels(newlanguage.s63(), newlanguage.s64())
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                if self.m_listBox2.GetSelection() == 0:
                    setting['Language'] = 'Auto'
                else:
                    setting['Language'] = languagelist[self.m_listBox2.GetSelection() - 1]
                with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.json'), 'w',
                          encoding='utf-8') as settingfile:
                    settingfile.write(json.dumps(setting))
                os.popen(sys.argv[0])
                sys.exit(0)


    def disablebutton(self, event):
        self.m_button2.Enable(False)

    def none(self, event):
        self.m_textCtrl4.SetValue('')

    def shutdown(self, event):
        self.m_textCtrl4.SetValue('shutdown -s -t 0')

    def reboot(self, event):
        self.m_textCtrl4.SetValue('shutdown -r -t 0')

    def custom(self, event):
        event.Skip()

    def getcmd(self, event):
        if self.m_textCtrl4.GetValue() == '':
            self.m_radioBtn1.SetValue(True)
        elif self.m_textCtrl4.GetValue() == 'shutdown -s -t 0':
            self.m_radioBtn2.SetValue(True)
        elif self.m_textCtrl4.GetValue() == 'shutdown -r -t 0':
            self.m_radioBtn3.SetValue(True)
        else:
            self.m_radioBtn4.SetValue(True)

    def autosave(self, event):
        self.m_filePicker2.Enable(self.m_checkBox2.GetValue())


class MyDialog2(wx.Dialog):

    def __init__(self, parent, title):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                           size=wx.Size(300, 135),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.SetSize(wx.Size(int('%.0f' % (300 * self.GetDPI()[0] / 96)),
                                        int('%.0f' % (135 * self.GetDPI()[0] / 96))))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        #bSizer4.Add((0, int('%.0f' % (10 * self.GetDPI()[0] / 96))), 0, 0, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(-1, -1), 0)
        if self.GetTitle() != language.s42():
            if frame.m_choice4.GetSelection() == 0:
                self.m_textCtrl1.SetValue(frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 3))
            elif frame.m_choice4.GetSelection() == 1:
                self.m_textCtrl1.SetValue(frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 2))
        bSizer4.Add(self.m_textCtrl1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, language.s36([]), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        if len(list(self.m_textCtrl1.GetValue())) == 8:
            self.m_staticText11.SetLabelText(language.s36(['CRC-32']))
        elif len(list(self.m_textCtrl1.GetValue())) == 32:
            self.m_staticText11.SetLabelText(language.s36(['MD5']))
        elif len(list(self.m_textCtrl1.GetValue())) == 40:
            self.m_staticText11.SetLabelText(language.s36(['SHA-1']))
        elif len(list(self.m_textCtrl1.GetValue())) == 56:
            self.m_staticText11.SetLabelText(language.s36(['SHA-224', 'SHA3-224']))
        elif len(list(self.m_textCtrl1.GetValue())) == 64:
            self.m_staticText11.SetLabelText(language.s36(['SHA-256', 'SHA3-256', 'BLAKE2s']))
        elif len(list(self.m_textCtrl1.GetValue())) == 96:
            self.m_staticText11.SetLabelText(language.s36(['SHA-384', 'SHA3-384']))
        elif len(list(self.m_textCtrl1.GetValue())) == 128:
            self.m_staticText11.SetLabelText(language.s36(['SHA-512', 'SHA3-512', 'BLAKE2b']))
        else:
            self.m_staticText11.SetLabelText(language.s36([]))

        self.m_staticText11.Wrap(-1)

        bSizer4.Add(self.m_staticText11, 0, wx.ALL, 5)
        #bSizer4.Add((0, 0), 1, 0, 5)
        m_sdbSizer3 = wx.StdDialogButtonSizer()
        self.m_sdbSizer3OK = wx.Button(self, wx.ID_OK, language.s57(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_sdbSizer3OK.SetDefault()
        m_sdbSizer3.AddButton(self.m_sdbSizer3OK)
        m_sdbSizer3.Realize()

        bSizer4.Add( m_sdbSizer3, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.EXPAND, 5 )

        self.SetSizer(bSizer4)
        self.Layout()
        main.Disable(frame)
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.close)
        self.m_textCtrl1.Bind(wx.EVT_TEXT, self.gethash)
        self.m_sdbSizer3OK.Bind(wx.EVT_BUTTON, self.add)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class

    def close(self, event):
        main.Enable(frame)
        self.Destroy()

    def gethash(self, event):
        if len(list(self.m_textCtrl1.GetValue())) == 8:
            self.m_staticText11.SetLabelText(language.s36(['CRC-32']))
        elif len(list(self.m_textCtrl1.GetValue())) == 32:
            self.m_staticText11.SetLabelText(language.s36(['MD5']))
        elif len(list(self.m_textCtrl1.GetValue())) == 40:
            self.m_staticText11.SetLabelText(language.s36(['SHA-1']))
        elif len(list(self.m_textCtrl1.GetValue())) == 56:
            self.m_staticText11.SetLabelText(language.s36(['SHA-224', 'SHA3-224']))
        elif len(list(self.m_textCtrl1.GetValue())) == 64:
            self.m_staticText11.SetLabelText(language.s36(['SHA-256', 'SHA3-256', 'BLAKE2s']))
        elif len(list(self.m_textCtrl1.GetValue())) == 96:
            self.m_staticText11.SetLabelText(language.s36(['SHA-384', 'SHA3-384']))
        elif len(list(self.m_textCtrl1.GetValue())) == 128:
            self.m_staticText11.SetLabelText(language.s36(['SHA-512', 'SHA3-512', 'BLAKE2b']))
        else:
            self.m_staticText11.SetLabelText(language.s36([]))

    def add(self, event):
        global information
        if self.GetTitle() == language.s42():
            index = frame.m_listCtrl2.InsertItem(frame.m_listCtrl2.GetItemCount(),
                                                 str(frame.m_listCtrl2.GetItemCount() + 1))
            frame.m_listCtrl2.SetItem(index, 1, '')
            frame.m_listCtrl2.SetItem(index, 2, '')
            frame.m_listCtrl2.SetItem(index, 3, self.m_textCtrl1.GetValue().lower())
            information.append('/')
        else:
            if frame.m_choice4.GetSelection() == 0:
                frame.m_listCtrl2.SetItem(frame.m_listCtrl2.GetFocusedItem(), 1, '')
                frame.m_listCtrl2.SetItem(frame.m_listCtrl2.GetFocusedItem(), 3, self.m_textCtrl1.GetValue().lower())
            elif frame.m_choice4.GetSelection() == 1:
                frame.m_listCtrl2.SetItem(frame.m_listCtrl2.GetFocusedItem(), 2, self.m_textCtrl1.GetValue().lower())
                frame.m_listCtrl2.SetItem(frame.m_listCtrl2.GetFocusedItem(), 3, '')
                frame.m_listCtrl2.SetItemBackgroundColour(frame.m_listCtrl2.GetFocusedItem(), wx.Colour(-1, -1, -1))
        main.Enable(frame)
        frame.sort(None)
        self.Destroy()


class MyDialog3(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=language.s44(), pos=wx.DefaultPosition,
                           size=wx.Size(450, 270),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.SetSize(wx.Size(int('%.0f' % (450 * self.GetDPI()[0] / 96)),
                                        int('%.0f' % (270 * self.GetDPI()[0] / 96))))
        main.Disable(frame)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap1 = wx.GenericStaticBitmap(self, wx.ID_ANY,
                                                wx.Bitmap(os.path.join(os.path.dirname(sys.argv[0]), "Logo.png"),
                                                          wx.BITMAP_TYPE_ANY),
                                                wx.DefaultPosition, wx.Size(int('%.0f' % (100 * self.GetDPI()[0] / 96)),
                                                                            int('%.0f' % (
                                                                                    100 * self.GetDPI()[0] / 96))),
                                                0)
        self.m_bitmap1.SetScaleMode(2)
        bSizer6.Add(self.m_bitmap1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY,
                                           language.s45() + '\n' + language.s47(sys.version.partition(' ')[0],
                                                                                wx.version().partition(' ')[0]) +
                                           '\n' + 'Copyright ©2025 ZHJ.' + '\n',
                                           wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText1.Wrap(-1)

        bSizer6.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        self.m_hyperlink1 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Github", u"https://github.com/ZHJ00000",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        gSizer3.Add(self.m_hyperlink1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_hyperlink2 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"Gitee", u"https://gitee.com/zhj00",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        gSizer3.Add(self.m_hyperlink2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer6.Add(gSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.close)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def close(self, event):
        main.Enable(frame)
        self.Destroy()


class MyDialog4(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=language.s70(), pos=wx.DefaultPosition,
                          size=wx.Size(550, 315),
                          style=wx.DEFAULT_DIALOG_STYLE | wx.CLOSE_BOX)
        self.SetSize(wx.Size(int('%.0f' % (550 * self.GetDPI()[0] / 96)),
                                       int('%.0f' % (315 * self.GetDPI()[0] / 96))))
        self.SetSizeHints(wx.DefaultSize, wx.Size(int('%.0f' % (750 * self.GetDPI()[0] / 96)),
                                                  int('%.0f' % (450 * self.GetDPI()[0] / 96))))
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_DESKTOP))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, language.s66(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        bSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, language.s71(), wx.DefaultPosition, wx.DefaultSize,
                                           wx.ST_ELLIPSIZE_END)
        self.m_staticText2.Wrap(-1)

        bSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, language.s72(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        bSizer1.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, language.s67(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        bSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, language.s68(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer1.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_gauge1 = wx.Gauge(self, wx.ID_ANY, 10000, wx.DefaultPosition,
                                 wx.Size(int('%.0f' % (500 * self.GetDPI()[0] / 96)),
                                         int('%.0f' % (25 * self.GetDPI()[0] / 96))), wx.GA_HORIZONTAL)
        self.m_gauge1.SetValue(0)
        bSizer1.Add(self.m_gauge1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, language.s69(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        bSizer1.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_gauge2 = wx.Gauge(self, wx.ID_ANY, 10000, wx.DefaultPosition,
                                 wx.Size(int('%.0f' % (500 * self.GetDPI()[0] / 96)),
                                         int('%.0f' % (25 * self.GetDPI()[0] / 96))),
                                 wx.GA_HORIZONTAL | wx.GA_PROGRESS)
        self.m_gauge2.SetValue(0)
        bSizer1.Add(self.m_gauge2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        m_sdbSizer4 = wx.StdDialogButtonSizer()
        self.m_sdbSizer4OK = wx.Button(self, wx.ID_OK, language.s113())
        m_sdbSizer4.AddButton(self.m_sdbSizer4OK)
        self.m_sdbSizer4Cancel = wx.Button(self, wx.ID_CANCEL, language.s54())
        m_sdbSizer4.AddButton(self.m_sdbSizer4Cancel)
        m_sdbSizer4.Realize()

        bSizer1.Add( m_sdbSizer4, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.cancel)
        self.m_sdbSizer4Cancel.Bind(wx.EVT_BUTTON, self.cancel)
        self.m_sdbSizer4OK.Bind(wx.EVT_BUTTON, self.pause)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def close(self, event):
        pass

    def cancel(self, event):
        global iscancel
        toastone = wx.MessageDialog(None, language.s115(), language.s1(),
                                    wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)
        toastone.SetYesNoLabels(language.s63(), language.s64())
        if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
            toastone.Destroy()
            iscancel = True

    def pause(self, event):
        global ispause
        if ispause:
            ispause = False
            self.m_sdbSizer4OK.SetLabel(language.s113())
        else:
            ispause = True
            self.m_sdbSizer4OK.SetLabel(language.s114())


class MyDialog5(wx.Dialog):

    def __init__(self, parent, coding, mode=0):
        global encoding, file
        main.Disable(frame)
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=language.s50() + ' - ' + file,
                           pos=wx.DefaultPosition, size=wx.Size(500, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.SetSize(wx.Size(int('%.0f' % (500 * self.GetDPI()[0] / 96)),
                                                                int('%.0f' % (400 * self.GetDPI()[0] / 96))))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.mode = mode

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        bSizer101 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, language.s51(), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)

        bSizer101.Add(self.m_staticText13, 0, wx.ALL, 5)

        m_listBox1Choices = ['ANSI', 'ASCII', 'BIG5', 'BIG5HKSCS', 'CP037', 'CP273', 'CP424', 'CP437', 'CP500', 'CP720',
                             'CP737', 'CP775', 'CP850', 'CP852', 'CP855', 'CP856', 'CP857', 'CP858', 'CP860', 'CP861',
                             'CP862', 'CP863', 'CP864', 'CP865', 'CP866', 'CP869', 'CP874', 'CP875', 'CP932', 'CP949',
                             'CP950', 'CP1006', 'CP1026', 'CP1125', 'CP1140', 'CP1250', 'CP1251', 'CP1252', 'CP1253',
                             'CP1254', 'CP1255', 'CP1256', 'CP1257', 'CP1258', 'EUC_JP', 'EUC_JIS_2004', 'EUC_JISX0213',
                             'EUC_KR', 'GB2312', 'GBK', 'GB18030', 'HZ', 'ISO2022_JP', 'ISO2022_JP_1', 'ISO2022_JP_2',
                             'ISO2022_JP_2004', 'ISO2022_JP_3', 'ISO2022_JP_EXT', 'ISO2022_KR', 'LATIN_1', 'ISO8859_2',
                             'ISO8859_3', 'ISO8859_4', 'ISO8859_5', 'ISO8859_6', 'ISO8859_7', 'ISO8859_8', 'ISO8859_9',
                             'ISO8859_10', 'ISO8859_11', 'ISO8859_13', 'ISO8859_14', 'ISO8859_15', 'ISO8859_16',
                             'JOHAB', 'KOI8_R', 'KOI8_T', 'KOI8_U', 'KZ1048', 'MAC_CYRILLIC', 'MAC_GREEK',
                             'MAC_ICELAND', 'MAC_LATIN2', 'MAC_ROMAN', 'MAC_TURKISH', 'OEM', 'PTCP154', 'SHIFT_JIS',
                             'SHIFT_JIS_2004', 'SHIFT_JISX0213', 'UTF_32', 'UTF_32_BE', 'UTF_32_LE', 'UTF_16',
                             'UTF_16_BE', 'UTF_16_LE', 'UTF_7', 'UTF_8', 'UTF_8_SIG']

        self.m_listBox1 = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition,
                                     wx.Size(int('%.0f' % (230 * self.GetDPI()[0] / 96)),
                                             int('%.0f' % (290 * self.GetDPI()[0] / 96))), m_listBox1Choices,
                                     wx.LB_NEEDED_SB | wx.LB_SINGLE)
        try:
            self.m_listBox1.SetSelection(m_listBox1Choices.index(find_encoding_key(coding)))
        except ValueError:
            self.m_listBox1.SetSelection(97)
        bSizer101.Add(self.m_listBox1, 0, wx.ALL, 5)

        gSizer4.Add(bSizer101, 1, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, language.s52(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)

        bSizer11.Add(self.m_staticText14, 0, wx.ALL, 5)

        self.m_richText1 = wx.richtext.RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                    wx.DefaultSize,
                                                    wx.TE_READONLY | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        bSizer11.Add(self.m_richText1, 1, wx.EXPAND | wx.ALL, 5)

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button(self, wx.ID_OK, language.s53())
        m_sdbSizer1.AddButton(self.m_sdbSizer1OK)
        self.m_sdbSizer1Cancel = wx.Button(self, wx.ID_CANCEL, language.s54())
        m_sdbSizer1.AddButton(self.m_sdbSizer1Cancel)
        m_sdbSizer1.Realize()

        gSizer4.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer10.Add(gSizer4, 1, wx.EXPAND, 5)

        bSizer10.Add(m_sdbSizer1, 0, wx.EXPAND | wx.TOP|wx.BOTTOM|wx.LEFT, 5)

        if find_encoding_key(coding) not in m_listBox1Choices:
            encoding = 'utf-8'
        else:
            encoding = coding
        try:
            with open(file, 'r', encoding=encoding, errors='replace') as display:
                self.m_richText1.SetValue(display.read())
                self.m_sdbSizer1OK.Enable(True)
        except Exception as err:
            self.m_sdbSizer1OK.Enable(False)
            self.m_richText1.BeginTextColour(wx.Colour(255, 0, 0))
            self.m_richText1.SetValue(language.s55() + '\n' + type(err).__name__ + ': ' + str(err))
            self.m_richText1.EndTextColour()
        self.SetSizer(bSizer10)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.close)
        self.m_listBox1.Bind(wx.EVT_LISTBOX, self.getcode)
        self.m_sdbSizer1Cancel.Bind(wx.EVT_BUTTON, self.close)
        self.m_sdbSizer1OK.Bind(wx.EVT_BUTTON, self.ok)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def close(self, event):
        main.Enable(frame)
        self.Destroy()

    def getcode(self, event):
        global encoding, file
        encoding = self.m_listBox1.GetString(self.m_listBox1.GetSelection())
        try:
            with open(file, 'r', encoding=encoding, errors='replace') as display:
                self.m_richText1.SetValue(display.read())
                self.m_sdbSizer1OK.Enable(True)
        except Exception as err:
            self.m_sdbSizer1OK.Enable(False)
            self.m_richText1.BeginTextColour(wx.Colour(255, 0, 0))
            self.m_richText1.SetValue(language.s55() + '\n' + type(err).__name__ + ': ' + str(err))
            self.m_richText1.EndTextColour()

    def ok(self, event):
        main.Enable(frame)
        self.Destroy()
        if not self.mode:
            intask(file, encoding)
        else:
            with open(file, 'r', encoding=encoding) as f:
                frame.inputshafile.m_richText4.SetValue(f.read())


class MyDialog6(wx.Dialog):

    def __init__(self, parent):
        global information
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=language.s92(), pos=wx.DefaultPosition,
                           size=wx.Size(500, 300),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.SetSize(wx.Size(int('%.0f' % (500 * self.GetDPI()[0] / 96)),
                                        int('%.0f' % (300 * self.GetDPI()[0] / 96))))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_richText2 = wx.richtext.RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                                    wx.TE_READONLY | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        text = ''
        if frame.m_choice4.GetSelection() == 0:
            if frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 2) == '':
                text = text + language.s93() + '/' + '\n'
                text = text + language.s94() + \
                       frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 3) + '\n'
                text = text + language.s95() + '/' + '\n' + language.s96() + '/'
            else:
                text = text + language.s93() + \
                       frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 2) + '\n'
                if frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 3) == '':
                    text = text + language.s94() + '/' + '\n'
                else:
                    text = text + language.s94() + \
                           frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 3) + '\n'
                if frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 3) != language.s81():
                    text = text + language.s95() + information[
                        int(frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(),
                                                          0)) - 1] + '\n' + language.s96() + '/'
                else:
                    text = text + language.s95() + '/' + '\n' + language.s96() + information[
                        int(frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 0)) - 1]
        elif frame.m_choice4.GetSelection() == 1:
            text = text + language.s93() + \
                   frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 1) + '\n'
            if frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 2) == '':
                text = text + language.s138() + '/' + '\n'
            else:
                text = text + language.s138() + \
                       frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 2) + '\n'
            if frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 3) != language.s81():
                text = text + language.s95() + information[
                    int(frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(),
                                                      0)) - 1] + '\n' + language.s96() + '/'
            else:
                text = text + language.s95() + '/' + '\n' + language.s96() + information[
                    int(frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 0)) - 1]
        self.m_richText2.SetValue(text)
        bSizer9.Add(self.m_richText2, 1, wx.EXPAND | wx.ALL, 5)

        m_sdbSizer3 = wx.StdDialogButtonSizer()
        self.m_sdbSizer3OK = wx.Button(self, wx.ID_OK)
        self.m_sdbSizer3OK.SetLabelText(language.s53())
        m_sdbSizer3.AddButton(self.m_sdbSizer3OK)
        m_sdbSizer3.Realize()

        bSizer9.Add(m_sdbSizer3, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer9)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.close)
        self.m_sdbSizer3OK.Bind(wx.EVT_BUTTON, self.close)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def close(self, event):
        self.Destroy()


class MyDialog7(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=language.s117(), pos=wx.DefaultPosition,
                           size=wx.Size(400, 300), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSize(wx.Size(int('%.0f' % (400 * self.GetDPI()[0] / 96)),
                             int('%.0f' % (
                                     300 * self.GetDPI()[0] / 96))))
        self.retry = 0
        self.current_version = {'link': {}}
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_bitmap2 = wx.GenericStaticBitmap(self, wx.ID_ANY,
                                                wx.Bitmap(os.path.join(os.path.dirname(sys.argv[0]), "Logo.png"),
                                                          wx.BITMAP_TYPE_ANY),
                                                wx.DefaultPosition, wx.Size(int('%.0f' % (50 * self.GetDPI()[0] / 96)),
                                                                            int('%.0f' % (
                                                                                    50 * self.GetDPI()[0] / 96))), 0)
        self.m_bitmap2.SetScaleMode(2)
        fgSizer1.Add(self.m_bitmap2, 0, wx.ALL, 5)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY,
                                            language.s1() + '\n' + language.s118() + '\n' + language.s119(None),
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)

        fgSizer1.Add(self.m_staticText14, 1, wx.ALL, 5)

        bSizer13.Add(fgSizer1, 0, wx.EXPAND, 5)

        #self.m_richText3 = wx.richtext.RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                                    #wx.TE_READONLY | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        self.m_htmlWin1 = wx.html.HtmlWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.html.HW_SCROLLBAR_AUTO)
        self.m_htmlWin1.SetPage(markdown.markdown(language.s120()))
        bSizer13.Add(self.m_htmlWin1, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, language.s121(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)

        bSizer13.Add(self.m_staticText15, 0, wx.ALL, 5)
        self.m_staticText15.Show(False)

        self.m_gauge3 = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.m_gauge3.SetValue(0)

        bSizer13.Add(self.m_gauge3, 0, wx.ALL | wx.EXPAND, 5)
        self.m_gauge3.Show(False)

        m_sdbSizer5 = wx.StdDialogButtonSizer()
        self.m_sdbSizer5OK = wx.Button(self, wx.ID_OK)
        self.m_sdbSizer5OK.SetLabel(language.s122())
        self.m_sdbSizer5OK.Enable(False)
        m_sdbSizer5.AddButton(self.m_sdbSizer5OK)
        self.m_sdbSizer5Cancel = wx.Button(self, wx.ID_CANCEL)
        self.m_sdbSizer5Cancel.SetLabel(language.s54())
        m_sdbSizer5.AddButton(self.m_sdbSizer5Cancel)
        m_sdbSizer5.Realize()

        bSizer13.Add( m_sdbSizer5, 0, wx.EXPAND|wx.ALL, 5 )

        self.SetSizer(bSizer13)
        self.Layout()

        self.Centre(wx.BOTH)
        self.update(self, usecache=True)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.close)
        self.m_htmlWin1.Bind(wx.html.EVT_HTML_LINK_CLICKED, self.link)
        self.m_sdbSizer5Cancel.Bind(wx.EVT_BUTTON, self.close)
        self.m_sdbSizer5OK.Bind(wx.EVT_BUTTON, self.update)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def close(self, event):
        if self.m_sdbSizer5Cancel.IsEnabled():
            frame.Enable(True)
            self.Show(False)

    def link(self, event):
        os.startfile(event.GetLinkInfo().GetHref())

    def update(self, event, retry=0, usecache=False):
        if self.m_sdbSizer5OK.GetLabel() == language.s122():
            self.m_htmlWin1.SetPage(markdown.markdown(language.s120()))
            self.m_staticText14.SetLabel(language.s1() + '\n' + language.s118() + '\n' + language.s119(None))
            self.m_sdbSizer5OK.Enable(False)
            if not retry:
                thread2 = threading.Thread(target=self.download, args=(
                    'check',
                    'https://github.com/ZHJ00000/OTA_Service/releases/download/CurrentVersion/CurrentVersion.json',
                    os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'CurrentVersion.json'), usecache),
                                           daemon=True)
            else:
                thread2 = threading.Thread(target=self.download, args=(
                    'check',
                    'https://gitee.com/zhj00/OTA_Service/releases/download/FilesChecker/CurrentVersion.json',
                    os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'CurrentVersion.json'), usecache),
                                           daemon=True)
            thread2.start()
        elif self.m_sdbSizer5OK.GetLabel() == language.s124():
            self.m_staticText15.Show(True)
            self.m_sdbSizer5OK.Enable(False)
            self.m_sdbSizer5Cancel.Enable(False)
            if str(version) in self.current_version['link'].keys():
                thread2 = threading.Thread(target=self.download, args=(
                    'download', self.current_version['link'][str(version)][self.retry + 1],
                    os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3',
                                 os.path.basename(self.current_version['link'][str(version)][self.retry + 1]))),
                                           daemon=True)
            else:
                thread2 = threading.Thread(target=self.download, args=(
                    'download', self.current_version['link']['other'][self.retry + 1],
                    os.path.join(os.environ["TEMP"],
                                 os.path.basename(self.current_version['link']['other'][self.retry + 1]))), daemon=True)
            thread2.start()
            self.m_gauge3.Show(True)
            self.Layout()

    def download(self, mode, url, output_path, usecache=None):
        global updatedialog
        if os.path.isfile(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3',
                                       'CurrentVersion.json')) and mode == 'check' and usecache:
            if datetime.datetime.fromtimestamp(os.path.getmtime(
                    os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3',
                                 'CurrentVersion.json'))).date() == datetime.datetime.now().date():
                usecache = bool(os.path.getsize(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3',
                                                             'CurrentVersion.json')))
            else:
                usecache = False
        else:
            usecache = False
        if not usecache:
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'wgetlog.log'), 'w',
                      encoding='utf-8') as f:
                pass
            process = subprocess.Popen(
                [os.path.join(os.path.dirname(sys.argv[0]), "wget.exe"), '-o',
                 os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'wgetlog.log'),
                 '-t 3 -T 5',
                 '-O',
                 output_path, '--progress=bar', url], creationflags=subprocess.CREATE_NO_WINDOW)
            if mode == 'download':
                while True:
                    if process.poll() is not None:
                        break
                    with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'wgetlog.log'), 'r',
                              encoding='utf-8', errors='replace') as f:
                        a = f.readlines()
                    try:
                        if a[-2].rstrip().split()[1] == '..........':
                            self.m_staticText15.SetLabel(
                                language.s121() + a[-2].rstrip().split()[-3] + ' (' + a[-2].rstrip().split()[
                                    -2] + 'B/s, ' + language.s128() +
                                a[-2].rstrip().split()[-1] + ')')
                            self.m_gauge3.SetValue(int(a[-2].rstrip().split()[-3][:-1]))
                        else:
                            self.m_staticText15.SetLabel(language.s123())
                    except IndexError:
                        self.m_staticText15.SetLabel(language.s123())
                    time.sleep(0.5)

            while True:
                if process.poll() is not None:
                    break
            rc = process.poll()
            os.utime(output_path, (time.time(), time.time()))
        else:
            rc = 0

        if rc == 0:
            if mode == 'check':
                self.retry = 0
                with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'CurrentVersion.json'), 'r',
                          encoding='utf-8') as f:
                    self.current_version = json.loads(f.read())
                if tuple(self.current_version['version']) > version or str(version) in self.current_version['rollback']:
                    frame.SetStatusText(language.s139())
                try:
                    self.m_htmlWin1.SetPage(markdown.markdown(self.current_version['note'][language.LANGUAGE[1]]))
                    self.m_staticText14.SetLabel(
                        language.s1() + '\n' + language.s118() + '\n' + language.s119(self.current_version['version']))
                    if tuple(self.current_version['version']) > version or str(version) in self.current_version[
                        'rollback']:
                        self.m_sdbSizer5OK.SetLabel(language.s124())
                        if str(version) in self.current_version['link'].keys():
                            self.m_staticText15.SetLabel(language.s125() + self.current_version['link'][str(version)][0])
                        else:
                            self.m_staticText15.SetLabel(language.s126() + self.current_version['link']['other'][0])
                        self.m_staticText15.Show(True)
                        self.Layout()

                    else:
                        self.m_sdbSizer5OK.SetLabel(language.s122())
                    self.m_sdbSizer5OK.Enable(True)
                except RuntimeError:
                    pass
            elif mode == 'download':
                self.Destroy()
                if str(version) in self.current_version['link'].keys():
                    os.popen(output_path + ' /SILENT /PASSWORD=67N8F-38W0A-RNI22-YX1AQ-11AZ5')
                else:
                    os.popen(output_path)
                frame.Destroy()

        else:
            try:
                if str(version) in self.current_version['link'].keys():
                    tf = (mode == 'check' and self.retry == 1) or (
                            mode == 'download' and len(
                        self.current_version['link'][str(version)]) - 2 - self.retry == 0)
                else:
                    tf = (mode == 'check' and self.retry == 1) or (
                            mode == 'download' and len(
                        self.current_version['link']['other']) - 2 - self.retry == 0)
                if tf:
                    self.m_htmlWin1.SetPage(markdown.markdown(language.s127()))
                    self.m_staticText14.SetLabel(
                        language.s1() + '\n' + language.s118() + '\n' + language.s119(None))
                    self.m_sdbSizer5OK.SetLabel(language.s122())
                    self.m_staticText15.Show(False)
                    self.m_gauge3.Show(False)
                    self.Layout()
                    self.m_sdbSizer5OK.Enable(True)
                    self.m_sdbSizer5Cancel.Enable(True)
                else:
                    self.retry += 1
                    self.update(self, self.retry)
            except RuntimeError:
                pass


class MyDialog8 ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=language.s140(), pos=wx.DefaultPosition,
                           size=wx.Size(400, 150), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSize(wx.Size(int('%.0f' % (400 * self.GetDPI()[0] / 96)),
                             int('%.0f' % (
                                     175 * self.GetDPI()[0] / 96))))

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        frame.Enable(False)

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, language.s141(), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        fgSizer2.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_filePicker2 = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, language.s22(), language.s23(),
                                               wx.DefaultPosition, wx.Size(-1, -1),
                                               wx.FLP_DEFAULT_STYLE | wx.FLP_FILE_MUST_EXIST | wx.FLP_OPEN | wx.FLP_SMALL)
        fgSizer2.Add( self.m_filePicker2, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

        fileDrop = FileDrop2()
        self.m_filePicker2.SetDropTarget(fileDrop)

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, language.s142(), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        fgSizer2.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(int('%.0f' % (350 * self.GetDPI()[0] / 96)), -1), 0)
        fgSizer2.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer14.Add( fgSizer2, 1, wx.EXPAND, 5 )

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, language.s36([]), wx.DefaultPosition, wx.DefaultSize, 0)
        if len(list(self.m_textCtrl3.GetValue())) == 8:
            self.m_staticText18.SetLabelText(language.s36(['CRC-32']))
        elif len(list(self.m_textCtrl3.GetValue())) == 32:
            self.m_staticText18.SetLabelText(language.s36(['MD5']))
        elif len(list(self.m_textCtrl3.GetValue())) == 40:
            self.m_staticText18.SetLabelText(language.s36(['SHA-1']))
        elif len(list(self.m_textCtrl3.GetValue())) == 56:
            self.m_staticText18.SetLabelText(language.s36(['SHA-224', 'SHA3-224']))
        elif len(list(self.m_textCtrl3.GetValue())) == 64:
            self.m_staticText18.SetLabelText(language.s36(['SHA-256', 'SHA3-256', 'BLAKE2s']))
        elif len(list(self.m_textCtrl3.GetValue())) == 96:
            self.m_staticText18.SetLabelText(language.s36(['SHA-384', 'SHA3-384']))
        elif len(list(self.m_textCtrl3.GetValue())) == 128:
            self.m_staticText18.SetLabelText(language.s36(['SHA-512', 'SHA3-512', 'BLAKE2b']))
        else:
            self.m_staticText18.SetLabelText(language.s36([]))

        self.m_staticText18.Wrap(-1)

        bSizer14.Add(self.m_staticText18, 0, wx.ALL, 5)

        m_sdbSizer6 = wx.StdDialogButtonSizer()
        self.m_sdbSizer6OK = wx.Button( self, wx.ID_OK )
        self.m_sdbSizer6OK.SetLabel(language.s53())
        m_sdbSizer6.AddButton( self.m_sdbSizer6OK )
        #self.m_sdbSizer6Cancel = wx.Button( self, wx.ID_CANCEL )
        #self.m_sdbSizer6Cancel.SetLabel(language.s54())
        #m_sdbSizer6.AddButton( self.m_sdbSizer6Cancel )
        m_sdbSizer6.Realize()

        bSizer14.Add( m_sdbSizer6, 0, wx.EXPAND|wx.ALL, 5 )


        self.SetSizer( bSizer14 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.cancel)
        self.m_textCtrl3.Bind(wx.EVT_TEXT, self.gethash)
        #self.m_sdbSizer6Cancel.Bind(wx.EVT_BUTTON, self.cancel)
        self.m_sdbSizer6OK.Bind(wx.EVT_BUTTON, self.ok)

    def __del__( self ):
        pass

    # Virtual event handlers, override them in your derived class
    def gethash(self, event):
        if len(list(self.m_textCtrl3.GetValue())) == 8:
            self.m_staticText18.SetLabelText(language.s36(['CRC-32']))
        elif len(list(self.m_textCtrl3.GetValue())) == 32:
            self.m_staticText18.SetLabelText(language.s36(['MD5']))
        elif len(list(self.m_textCtrl3.GetValue())) == 40:
            self.m_staticText18.SetLabelText(language.s36(['SHA-1']))
        elif len(list(self.m_textCtrl3.GetValue())) == 56:
            self.m_staticText18.SetLabelText(language.s36(['SHA-224', 'SHA3-224']))
        elif len(list(self.m_textCtrl3.GetValue())) == 64:
            self.m_staticText18.SetLabelText(language.s36(['SHA-256', 'SHA3-256', 'BLAKE2s']))
        elif len(list(self.m_textCtrl3.GetValue())) == 96:
            self.m_staticText18.SetLabelText(language.s36(['SHA-384', 'SHA3-384']))
        elif len(list(self.m_textCtrl3.GetValue())) == 128:
            self.m_staticText18.SetLabelText(language.s36(['SHA-512', 'SHA3-512', 'BLAKE2b']))
        else:
            self.m_staticText18.SetLabelText(language.s36([]))

    def cancel(self, event):
        frame.Enable(True)
        self.Destroy()

    def ok(self, event):
        if not os.path.isfile(self.m_filePicker2.GetPath()):
            tip = wx.adv.RichToolTip(language.s143(),
                                     language.s144())
            tip.SetIcon(wx.ICON_WARNING)
            tip.ShowFor(self.m_filePicker2)
        else:
            index = frame.m_listCtrl2.InsertItem(frame.m_listCtrl2.GetItemCount(),
                                                 str(frame.m_listCtrl2.GetItemCount() + 1))
            frame.m_listCtrl2.SetItem(index, 1, self.m_filePicker2.GetPath())
            frame.m_listCtrl2.SetItem(index, 2, self.m_textCtrl3.GetValue().lower())
            frame.m_listCtrl2.SetItem(index, 3, '')
            information.append('/')
            frame.sort(None)
            frame.Enable(True)
            self.Destroy()


class MyDialog9 ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=language.s49(), pos=wx.DefaultPosition,
                           size=wx.Size(500, 400), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSize(wx.Size(int('%.0f' % (500 * self.GetDPI()[0] / 96)),
                             int('%.0f' % (
                                     400 * self.GetDPI()[0] / 96))))

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        frame.Enable(False)

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, language.s145(), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        bSizer15.Add( self.m_staticText19, 0, wx.ALL, 5 )

        self.m_richText4 = wx.richtext.RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                                    0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        bSizer15.Add( self.m_richText4, 1, wx.EXPAND |wx.ALL, 5 )

        gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_button8 = wx.Button( self, wx.ID_ANY, language.s146(), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer7.Add( self.m_button8, 0, wx.ALL, 5 )

        m_sdbSizer7 = wx.StdDialogButtonSizer()
        self.m_sdbSizer7OK = wx.Button( self, wx.ID_OK )
        self.m_sdbSizer7OK.SetLabel(language.s53())
        m_sdbSizer7.AddButton( self.m_sdbSizer7OK )
        m_sdbSizer7.Realize()

        gSizer7.Add( m_sdbSizer7, 1, wx.EXPAND|wx.ALL, 5 )


        bSizer15.Add( gSizer7, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer15 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.exit)
        self.m_button8.Bind( wx.EVT_BUTTON, self.load )
        self.m_sdbSizer7OK.Bind( wx.EVT_BUTTON, self.ok )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def exit(self, event):
        frame.Enable(True)
        self.Destroy()

    def load( self, event ):
        global file
        dlg = wx.FileDialog(self, message=language.s49(),
                            defaultDir='',
                            defaultFile='',
                            wildcard=language.s147(),
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            file = dlg.GetPath()
            dlg.Destroy()
            encodingpick = MyDialog5(None, 'utf-8', 1)
            encodingpick.Show()

    def ok( self, event ):
        frame.Enable(True)
        self.Destroy()
        for i in self.m_richText4.GetValue().split('\n'):
            if i:
                splitedline = i.split(' ')
                while len(splitedline) >= 2 and splitedline[1] == '':
                    del splitedline[1]
                fah = ''
                for j in splitedline[1:]:
                    fah += j + ' '

                index = frame.m_listCtrl2.InsertItem(frame.m_listCtrl2.GetItemCount(),
                                                     str(frame.m_listCtrl2.GetItemCount() + 1))
                fah = fah[:-1]
                if fah:
                    if (fah[0] == '"' and fah[-1] == '"') or (fah[0] == "'" and fah[-1] == "'"):
                        fah = fah[1:-1]
                    if fah[0] == '*':
                        fah = fah[1:]
                    frame.m_listCtrl2.SetItem(index, 1, fah)
                else:
                    frame.m_listCtrl2.SetItem(index, 1, '')
                frame.m_listCtrl2.SetItem(index, 2, i.split(' ')[0].lower())
                frame.m_listCtrl2.SetItem(index, 3, '')
                information.append('/')
        frame.sort(None)



if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '/Clean':
            time.sleep(1)
            if os.path.isdir(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Update')):
                shutil.rmtree(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Update'))
            for i in glob.glob(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'FilesCheckerUpdate*')):
                os.remove(i)
    app = wx.App()
    sys.path.append(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3'))
    sys.path.append(os.path.dirname(sys.argv[0]))
    if not os.path.isdir(os.path.join(os.environ["APPDATA"], 'ZHJ')):
        os.mkdir(os.path.join(os.environ["APPDATA"], 'ZHJ'))
    if not os.path.isdir(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3')):
        os.mkdir(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3'))
    languagelist = glob.glob(os.path.join(os.path.dirname(sys.argv[0]), 'language_*.py'))
    languagedic = {}
    for i in range(len(languagelist)):
        languagelist[i] = os.path.basename(languagelist[i])
        languagelist[i] = languagelist[i].split(".")[0]
    code = 'def get():\n    list = []\n'
    for i in languagelist:
        code = code + '    import ' + i + '\n    list.append(' + i + '.LANGUAGE)\n'
        code = code + '    list[-1].append("' + i + '")\n'
    code = code + '    return list'
    with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'getlanguagelist.py'), 'w',
              encoding='utf-8') as f:
        f.write(code)
    import getlanguagelist
    for i in getlanguagelist.get():
        for j in i[0]:
            languagedic[j] = [i[2], i[1]]
    try:
        with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.json'), 'r',
                  encoding='utf-8') as settingfile:
            setting = json.loads(settingfile.read())
    except Exception as err:
        try:
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.ini'), 'r',
                      encoding='utf-8') as settingfile:
                settingini = settingfile.readlines()
            for i in range(0, len(settingini)):
                settingini[i] = settingini[i].rstrip()
            settingini.extend(['', '', '', '', ''])
            setting = {}
            if settingini[0]:
                setting['Language'] = settingini[0]
            else:
                setting['Language'] = 'Auto'
            if settingini[1]:
                setting['SaveTaskEncoding'] = settingini[1]
            else:
                setting['SaveTaskEncoding'] = 'UTF-8'
            if settingini[2]:
                setting['ExportResultEncoding'] = settingini[2]
            else:
                setting['ExportResultEncoding'] = 'ANSI'
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.json'), 'w',
                      encoding='utf-8') as settingfile:
                settingfile.write(json.dumps(setting))
        except Exception as err:
            setting = {'Language': 'Auto',
                       'SaveTaskEncoding': 'UTF-8',
                       'ExportResultEncoding': 'ANSI',
                       'DefaultCheckMode': 0}
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.json'), 'w',
                      encoding='utf-8') as settingfile:
                settingfile.write(json.dumps(setting))
    if 'Language' not in setting.keys():
        setting['Language'] = 'Auto'
    if 'SaveTaskEncoding' not in setting.keys():
        setting['SaveTaskEncoding'] = 'UTF-8'
    if 'ExportResultEncoding' not in setting.keys():
        setting['ExportResultEncoding'] = 'ANSI'
    if 'DefaultCheckMode' not in setting.keys():
        setting['DefaultCheckMode'] = 0
    with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.json'), 'w',
              encoding='utf-8') as settingfile:
        settingfile.write(json.dumps(setting))
    try:
        if setting['Language'] == 'Auto':
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'language.py'),
                      'w', encoding='utf-8') as languagefile:
                languagefile.write('from ' + languagedic[locale][0] + ' import *')
        else:
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'language.py'),
                      'w', encoding='utf-8') as languagefile:
                languagefile.write('from ' + setting['Language'] + ' import *')
        import language
    except Exception as err:
        try:
            setting['Language'] = 'language_English'
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.json'), 'a',
                      encoding='utf-8') as settingfile:
                settingfile.write(json.dumps(setting))
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'language.py'),
                      'w', encoding='utf-8') as languagefile:
                languagefile.write('from ' + setting['Language'] + ' import *')
            import language
        except Exception as err:
            toastone = wx.MessageDialog(None, 'Unable to start program due to missing language pack.', 'FilesChecker',
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
            toastone.SetOKLabel('&OK')
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
    else:
        if os.path.isfile(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'LOCK')):
            try:
                os.remove(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'LOCK'))
            except PermissionError:
                toastone = wx.MessageDialog(None, language.s150(),
                                            language.s1(),
                                            wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                toastone.SetOKLabel(language.s57())
                if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                    toastone.Destroy()
            else:
                lockfile = open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'LOCK'), 'xb')
                frame = main(None)
                frame.Show(True)
                updatedialog = MyDialog7(None)
                app.MainLoop()
        else:
            lockfile = open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'LOCK'), 'xb')
            frame = main(None)
            frame.Show(True)
            updatedialog = MyDialog7(None)
            app.MainLoop()

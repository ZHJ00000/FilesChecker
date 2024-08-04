# Copyright ©2024 ZHJ. All Rights Reserved.

import wx, wx.xrc, wx.adv, wx.richtext  # pip install wxPython
import sys
import os
import glob
import hashlib
import threading
import time
import pyperclip  # pip install pyperclip
from importlib import reload
import locale
import ctypes
ctypes.windll.user32.SetProcessDPIAware()
locale = locale.getlocale()[0].replace(' ', '_').replace('(', '_').replace(')', '_')

fah = ''
ischeck = False
command = ''
export = ''
isexport = False
os.chdir(os.path.dirname(sys.argv[0]))

def intask(file, encoding):
    try:
        with open(file, 'r', encoding=encoding) as file:
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
            elif l[0] == 'sha1':
                frame.m_choice1.SetSelection(1)
                tf = True
            elif l[0] == 'sha224':
                frame.m_choice1.SetSelection(2)
                tf = True
            elif l[0] == 'sha256':
                frame.m_choice1.SetSelection(3)
                tf = True
            elif l[0] == 'sha384':
                frame.m_choice1.SetSelection(4)
                tf = True
            elif l[0] == 'sha512':
                frame.m_choice1.SetSelection(5)
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


class main(wx.Frame):

    def __init__(self, parent):
        global fah, file, information
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=language.s1(), pos=wx.DefaultPosition,
                          size=wx.Size(int('%.0f' % (1000 * wx.GetDisplayPPI()[0] / 96)),
                                       int('%.0f' % (600 * wx.GetDisplayPPI()[0] / 96))),
                          style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE_BOX | wx.TAB_TRAVERSAL)
        self.SetClientSize(wx.Size(int('%.0f' % (1000 * wx.GetDisplayPPI()[0] / 96)),
                                       int('%.0f' % (600 * wx.GetDisplayPPI()[0] / 96))))

        self.SetSizeHints(wx.Size(int('%.0f' % (1000 * wx.GetDisplayPPI()[0] / 96)),
                                       int('%.0f' % (600 * wx.GetDisplayPPI()[0] / 96))),
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

        self.m_menuItem3 = wx.MenuItem(self.m_menu3, wx.ID_ANY, language.s8() + "\tAlt+C", wx.EmptyString,
                                       wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_menuItem3)

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
        self.m_menuItem7 = wx.MenuItem(self.m_menu5, wx.ID_ANY, language.s12(), language.s105(), wx.ITEM_NORMAL)
        self.m_menu5.Append(self.m_menuItem7)

        self.m_menubar2.Append(self.m_menu5, language.s13())

        self.SetMenuBar(self.m_menubar2)

        self.m_toolBar1 = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        m_choice1Choices = [u"MD5", u"SHA1", u"SHA224", u"SHA256", u"SHA384", u"SHA512"]
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

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_listCtrl2 = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition,
                                       wx.Size(int('%.0f' % (1000 * wx.GetDisplayPPI()[0] / 96)),
                                               int('%.0f' % (485 * wx.GetDisplayPPI()[0] / 96))),
                                       wx.LC_HRULES | wx.LC_REPORT)
        self.m_listCtrl2.SetMinSize(
            wx.Size(int('%.0f' % (1000 * wx.GetDisplayPPI()[0] / 96)),
                                               int('%.0f' % (485 * wx.GetDisplayPPI()[0] / 96))))

        bSizer2.Add(self.m_listCtrl2, 1, wx.ALL | wx.EXPAND, 5)
        self.m_listCtrl2.InsertColumn(0, language.s17())
        self.m_listCtrl2.InsertColumn(1, language.s18())
        self.m_listCtrl2.InsertColumn(2, language.s19())
        self.m_listCtrl2.InsertColumn(3, language.s20())
        self.m_listCtrl2.SetColumnWidth(0, int('%.0f' % (50 * wx.GetDisplayPPI()[0] / 96)))  # 设置每一列的宽度
        self.m_listCtrl2.SetColumnWidth(1, int('%.0f' % (50 * wx.GetDisplayPPI()[0] / 96)))
        self.m_listCtrl2.SetColumnWidth(2, int('%.0f' % (425 * wx.GetDisplayPPI()[0] / 96)))
        self.m_listCtrl2.SetColumnWidth(3, int('%.0f' % (445 * wx.GetDisplayPPI()[0] / 96)))

        fileDrop = FileDrop()
        self.m_listCtrl2.SetDropTarget(fileDrop)

        information = []

        self.SetSizer(bSizer2)
        self.Layout()
        self.m_statusBar3 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.SetStatusText('')

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
        self.Bind(wx.EVT_MENU, self.exit, id=self.m_menuItem6.GetId())
        self.Bind(wx.EVT_MENU, self.about, id=self.m_menuItem7.GetId())
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
        if ischeck:
            toastone = wx.MessageDialog(None, language.s65(), language.s1(),
                                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)
            toastone.SetYesNoLabels(language.s63(), language.s64())
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
                sys.exit(-1)
        else:
            sys.exit(0)

    def export(self, path):
        try:
            with open(path, 'w', encoding='ansi') as file:
                file.write(language.s17() + ',' + language.s18() + ',' + language.s19() + ',' + language.s20() + '\n')
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
            global Time, Time2, allsize, allsize1, information, size
            size = os.path.getsize(path)  # 获取文件大小，单位是字节（byte）
            size1 = size
            with open(path, 'rb') as f:  # 以二进制模式读取文件
                Time1 = time.time()
                while size >= 1048576:  # 当文件大于1MB时将文件分块读取
                    algorithm.update(f.read(1024 * 1024))
                    size -= 1048576
                    allsize1 += 1048576
                    progress = ((size1 - size) / size1)
                    allprogress = (allsize1 / allsize)
                    Time1 = time.time()
                    check.m_staticText1.SetLabelText(language.s66() + timeformat(int((Time1 - Time) // 1)))
                    check.m_staticText4.SetLabelText(language.s67() + intformat(size1 - size) + ' ' + language.s73())
                    check.m_staticText5.SetLabelText(language.s68() + str('%.2f' % (progress * 100)) + '%')
                    check.m_gauge1.SetValue(int('%.0f' % (progress * 10000)))
                    check.m_staticText6.SetLabelText(language.s69() + str('%.2f' % (allprogress * 100)) + '%')
                    check.m_gauge2.SetValue(int('%.0f' % (allprogress * 10000)))
                algorithm.update(f.read())
            information.append(timeformat(int(Time1 - Time2) // 1))
            Time2 = time.time()
            return algorithm.hexdigest()  # 输出计算结果

        def gethash():
            global Time, Time2, allsize, allsize1, ischeck, information, size, count
            ischeck = True
            self.SetStatusText(language.s82())
            self.m_menuItem1.Enable(False)
            self.m_menuItem2.Enable(False)
            self.m_menuItem8.Enable(False)
            self.m_menuItem4.Enable(False)
            self.m_menuItem9.Enable(False)
            self.m_menuItem3.Enable(False)
            self.m_menuItem10.Enable(False)
            self.m_choice1.Enable(False)
            self.m_button1.Enable(False)
            self.m_button6.Enable(False)
            self.m_button3.Enable(False)
            self.m_listCtrl2.Enable(False)
            listitems = []
            for i in range(0, self.m_listCtrl2.GetItemCount()):
                if self.m_listCtrl2.GetItemText(i, 1) == '':
                    listitems.append([int(self.m_listCtrl2.GetItemText(i, 0)), self.m_listCtrl2.GetItemText(i, 1),
                                      self.m_listCtrl2.GetItemText(i, 2), self.m_listCtrl2.GetItemText(i, 3)])
                else:
                    listitems.append(
                        [int(self.m_listCtrl2.GetItemText(i, 0)), int(self.m_listCtrl2.GetItemText(i, 1)),
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
                if listitems[i][2] == '':
                    pass
                else:
                    count = count + 1
                    try:
                        allsize = allsize + os.path.getsize(listitems[i][2])
                    except Exception:
                        continue


            if count != 0:
                check.Show()
            check.SetTitle('(' + str(count1) + '/' + str(count) + ')' + language.s70())
            check.m_staticText1.SetLabelText(language.s66() + '00:00:00')
            Time = time.time()
            Time2 = Time
            for i in range(0, frame.m_listCtrl2.GetItemCount()):
                if listitems[i][2] == '':
                    information.append('')
                else:
                    count1 = count1 + 1
                    check.SetTitle('(' + str(count1) + '/' + str(count) + ') ' + language.s70())
                    check.m_staticText2.SetLabelText(language.s71() + listitems[i][2])
                    try:
                        if os.path.getsize(listitems[i][2]) >= 1099511627776:  # 1TB
                            check.m_staticText3.SetLabelText(language.s72() + str(
                                '%.2f' % (os.path.getsize(
                                    listitems[i][2]) / 1099511627776)) + ' TB (' + intformat(
                                os.path.getsize(listitems[i][2])) + ' ' + language.s73() + ')')
                        elif os.path.getsize(listitems[i][2]) >= 1073741824:  # 1GB
                            check.m_staticText3.SetLabelText(language.s72() + str(
                                '%.2f' % (os.path.getsize(
                                    listitems[i][2]) / 1073741824)) + ' GB (' + intformat(
                                os.path.getsize(listitems[i][2])) + ' ' + language.s73() + ')')
                        elif os.path.getsize(listitems[i][2]) >= 1048576:  # 1MB
                            check.m_staticText3.SetLabelText(language.s72() + str(
                                '%.2f' % (os.path.getsize(
                                    listitems[i][2]) / 1048576)) + ' MB (' + intformat(
                                os.path.getsize(listitems[i][2])) + ' ' + language.s73() + ')')
                        elif os.path.getsize(listitems[i][2]) >= 1024:  # 1KB
                            check.m_staticText3.SetLabelText(language.s72() + str(
                                '%.2f' % (os.path.getsize(
                                    listitems[i][2]) / 1024)) + ' KB (' + intformat(
                                os.path.getsize(listitems[i][2])) + ' ' + language.s73() + ')')
                        else:
                            check.m_staticText3.SetLabelText(language.s72() + str(
                                intformat(os.path.getsize(
                                    listitems[i][2]))) + ' ' + language.s73())
                        if self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'MD5':
                            listitems[i][3] = filehash(check, listitems[i][2],
                                                                     hashlib.md5())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA1':
                            listitems[i][3] = filehash(check, listitems[i][2],
                                                                     hashlib.sha1())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA224':
                            listitems[i][3] = filehash(check, listitems[i][2],
                                                                     hashlib.sha224())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA256':
                            listitems[i][3] = filehash(check, listitems[i][2],
                                                                     hashlib.sha256())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA384':
                            listitems[i][3] = filehash(check, listitems[i][2],
                                                                     hashlib.sha384())
                        elif self.m_choice1.GetString(self.m_choice1.GetSelection()) == 'SHA512':
                            listitems[i][3] = filehash(check, listitems[i][2],
                                                                     hashlib.sha512())
                    except Exception as err:
                        information.append(type(err).__name__ + ': ' + str(err))
                        allsize1 = allsize1 + size
                        Time2 = time.time()
                        listitems[i][3] = language.s81()
                        continue
            ischeck = False
            check.Destroy()
            self.SetStatusText(language.s83())
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
            if self.m_listCtrl2.GetSortIndicator() != -1:
                listitems = sorted(listitems, key=lambda x: x[self.m_listCtrl2.GetSortIndicator()],
                                   reverse=not self.m_listCtrl2.IsAscendingSortIndicator())
            for i in range(0, len(listitems)):
                self.m_listCtrl2.SetItem(i, 0, str(listitems[i][0]))
                self.m_listCtrl2.SetItem(i, 1, str(listitems[i][1]))
                self.m_listCtrl2.SetItem(i, 2, listitems[i][2])
                self.m_listCtrl2.SetItem(i, 3, listitems[i][3])
            self.m_menuItem1.Enable(True)
            self.m_menuItem2.Enable(True)
            self.m_menuItem8.Enable(True)
            self.m_menuItem4.Enable(True)
            self.m_menuItem9.Enable(True)
            self.m_menuItem3.Enable(True)
            self.m_menuItem10.Enable(True)
            self.m_choice1.Enable(True)
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
                    os.popen(command)
                except Exception as err:
                    toastone = wx.MessageDialog(None, language.s75(type(err).__name__ + ': ' + str(err)), language.s81(),
                                                wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                    toastone.SetOKLabel(language.s57())
                    if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                        toastone.Destroy()
            self.SetStatusText('')

        thread1 = threading.Thread(target=gethash, args=(), daemon=True)
        thread1.start()

    def addfile(self, event):
        global information
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

    def addhash(self, event):
        addhash = MyDialog2(None, language.s42())
        addhash.Show()

    def inputtask(self, event):
        global file
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
                encodingpick = MyDialog5(None, 'utf-8')
                encodingpick.Show()
            else:
                if coding[:9] == '# coding=':
                    try:
                        with open(file, 'r', encoding=coding[9:]) as f:
                            f.read()
                    except UnicodeDecodeError or LookupError:
                        encodingpick = MyDialog5(None, coding[9:])
                        encodingpick.Show()
                    else:
                        intask(file, coding[9:])
                elif coding[:8] == '#coding=':
                    try:
                        with open(file, 'r', encoding=coding[8:]) as f:
                            f.read()
                    except UnicodeDecodeError or LookupError:
                        encodingpick = MyDialog5(None, coding[8:])
                        encodingpick.Show()
                    else:
                        intask(file, coding[8:])
                else:
                    encodingpick = MyDialog5(None, 'utf-8')
                    encodingpick.Show()

    def outputtask(self, event):
        dlg = wx.FileDialog(self, message=language.s60(),
                            defaultDir='',
                            defaultFile='',
                            wildcard=language.s48(),
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText(language.s86() + dlg.GetPath())
            try:
                with open(dlg.GetPath(), 'w', encoding='utf-8') as file:
                    dlg.Destroy()
                    f = '# coding=utf-8\n' + frame.m_choice1.GetString(frame.m_choice1.GetSelection()) + '\n'
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
        if self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 2) == '':
            self.m_menuItem13.Enable(False)
            self.m_menuItem16.Enable(False)
        if self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(),
                                        3) == '' or self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(),
                                                                                  3) == language.s81():
            self.m_menuItem14.Enable(False)
        if self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 2) != '':
            self.m_menuItem17.Enable(False)
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
            self.m_listCtrl2.SetItem(self.m_listCtrl2.GetFocusedItem(), 1, '')
            self.m_listCtrl2.SetItem(self.m_listCtrl2.GetFocusedItem(), 2, fahs)
            self.m_listCtrl2.SetItem(self.m_listCtrl2.GetFocusedItem(), 3, '')
            information[int(self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 0))-1] = '/'
            self.sort(None)

    def edithash(self, event):
        addhash = MyDialog2(None, language.s88())
        addhash.Show()

    def copyfile(self, event):
        pyperclip.copy(self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 2))
        self.SetStatusText(language.s89())

    def copyhash(self, event):
        pyperclip.copy(self.m_listCtrl2.GetItemText(self.m_listCtrl2.GetFocusedItem(), 3))
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
            for i in range(0, self.m_listCtrl2.GetItemCount()):
                if self.m_listCtrl2.GetItemText(i, 1) == '':
                    listitems.append([int(self.m_listCtrl2.GetItemText(i, 0)), -1,
                                      self.m_listCtrl2.GetItemText(i, 2), self.m_listCtrl2.GetItemText(i, 3)])
                else:
                    listitems.append([int(self.m_listCtrl2.GetItemText(i, 0)), int(self.m_listCtrl2.GetItemText(i, 1)),
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

        self.m_listCtrl2.IsAscendingSortIndicator()
        self.m_listCtrl2.GetSortIndicator()


class MyDialog1(wx.Dialog):

    def __init__(self, parent):
        global command, export, isexport, languagelist
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=language.s24(), pos=wx.DefaultPosition,
                           size=wx.Size(int('%.0f' % (600 * wx.GetDisplayPPI()[0] / 96)),
                                        int('%.0f' % (400 * wx.GetDisplayPPI()[0] / 96))),
                           style=wx.DEFAULT_DIALOG_STYLE)

        main.Disable(frame)

        self.SetSizeHints(wx.Size(int('%.0f' % (600 * wx.GetDisplayPPI()[0] / 96)),
                                  int('%.0f' % (400 * wx.GetDisplayPPI()[0] / 96))),
                          wx.Size(int('%.0f' % (600 * wx.GetDisplayPPI()[0] / 96)),
                                  int('%.0f' % (400 * wx.GetDisplayPPI()[0] / 96))))

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_listbook1 = wx.Listbook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT)
        self.m_panel1 = wx.Panel(self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

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
                                       wx.Size(int('%.0f' % (450 * wx.GetDisplayPPI()[0] / 96)), -1), 0)
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
                                               wx.Size(int('%.0f' % (450 * wx.GetDisplayPPI()[0] / 96)), -1),
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
        self.m_panel2 = wx.Panel(self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, language.s35()), wx.VERTICAL)

        gSizer3 = wx.GridSizer(0, 6, 0, 0)

        self.m_button2 = wx.Button(sbSizer3.GetStaticBox(), wx.ID_ANY, language.s37(), wx.DefaultPosition, wx.DefaultSize,
                                   0)

        gSizer3.Add(self.m_button2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer3.Add(gSizer3, 0, wx.EXPAND, 5)

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

        m_listBox2Choices = [language.s21()]
        m_listBox2Choices.extend(displanguagelist)
        self.m_listBox2 = wx.ListBox(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(480, 290),
                                     m_listBox2Choices, wx.LB_NEEDED_SB | wx.LB_SINGLE)
        sbSizer3.Add(self.m_listBox2, 1, wx.ALL | wx.EXPAND, 5)

        def listlocate(list, Element):
            for i in range(0, len(list)):
                if list[i] == Element:
                    return (i)
            return (-1)
        if setting[0] == 'Auto':
            self.m_listBox2.SetSelection(0)
        else:
            self.m_listBox2.SetSelection(listlocate(languagelist, setting[0]) + 1)

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
            main.Enable(frame)
            self.Destroy()


    def changelanguage(self, event):
        global languagelist
        if not os.path.isfile('language_' + str(locale) + '.py') and self.m_listBox2.GetSelection() == 0:
            toastone = wx.MessageDialog(None, language.s46(), language.s81(),
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
            toastone.SetOKLabel(language.s57())
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
        else:
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'newlanguage.py'),
                      'w', encoding='utf-8') as f:
                if self.m_listBox2.GetSelection() == 0:
                    f.write('from language_' + str(locale) + ' import *')
                else:
                    f.write('from ' + languagelist[self.m_listBox2.GetSelection() - 1] + ' import *')
            import newlanguage
            reload(newlanguage)
            toastone = wx.MessageDialog(None, newlanguage.s39(), newlanguage.s1(),
                                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)
            toastone.SetYesNoLabels(newlanguage.s63(), newlanguage.s64())
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.ini'),
                          'r', encoding='utf-8') as settingfile:
                    setting = settingfile.readlines()
                for i in range(0, len(setting)):
                    setting[i] = setting[i].rstrip()
                if self.m_listBox2.GetSelection() == 0:
                    setting[0] = 'Auto'
                else:
                    setting[0] = languagelist[self.m_listBox2.GetSelection() - 1]
                with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.ini'), 'w',
                          encoding='utf-8') as settingfile:
                    f = ''
                    for i in setting:
                        f = f + i + '\n'
                    settingfile.write(f)
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
        global fah
        fah = ''
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                           size=wx.Size(int('%.0f' % (300 * wx.GetDisplayPPI()[0] / 96)),
                                        int('%.0f' % (135 * wx.GetDisplayPPI()[0] / 96))),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        #bSizer4.Add((0, int('%.0f' % (10 * wx.GetDisplayPPI()[0] / 96))), 0, 0, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(-1, -1), 0)
        if self.GetTitle() != language.s42():
            self.m_textCtrl1.SetValue(frame.m_listCtrl2.GetItemText(frame.m_listCtrl2.GetFocusedItem(), 3))
        bSizer4.Add(self.m_textCtrl1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, language.s36() + language.s43(), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        if len(list(self.m_textCtrl1.GetValue())) == 32:
            self.m_staticText11.SetLabelText(language.s36() + 'MD5')
        elif len(list(self.m_textCtrl1.GetValue())) == 40:
            self.m_staticText11.SetLabelText(language.s36() + 'SHA1')
        elif len(list(self.m_textCtrl1.GetValue())) == 56:
            self.m_staticText11.SetLabelText(language.s36() + 'SHA224')
        elif len(list(self.m_textCtrl1.GetValue())) == 64:
            self.m_staticText11.SetLabelText(language.s36() + 'SHA256')
        elif len(list(self.m_textCtrl1.GetValue())) == 96:
            self.m_staticText11.SetLabelText(language.s36() + 'SHA384')
        elif len(list(self.m_textCtrl1.GetValue())) == 128:
            self.m_staticText11.SetLabelText(language.s36() + 'SHA512')
        else:
            self.m_staticText11.SetLabelText(language.s36() + language.s43())

        self.m_staticText11.Wrap(-1)

        bSizer4.Add(self.m_staticText11, 0, wx.ALL, 5)
        bSizer4.Add((0, 0), 1, 0, 5)
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
        if len(list(self.m_textCtrl1.GetValue())) == 32:
            self.m_staticText11.SetLabelText(language.s36() + 'MD5')
        elif len(list(self.m_textCtrl1.GetValue())) == 40:
            self.m_staticText11.SetLabelText(language.s36() + 'SHA1')
        elif len(list(self.m_textCtrl1.GetValue())) == 56:
            self.m_staticText11.SetLabelText(language.s36() + 'SHA224')
        elif len(list(self.m_textCtrl1.GetValue())) == 64:
            self.m_staticText11.SetLabelText(language.s36() + 'SHA256')
        elif len(list(self.m_textCtrl1.GetValue())) == 96:
            self.m_staticText11.SetLabelText(language.s36() + 'SHA384')
        elif len(list(self.m_textCtrl1.GetValue())) == 128:
            self.m_staticText11.SetLabelText(language.s36() + 'SHA512')
        else:
            self.m_staticText11.SetLabelText(language.s36() + language.s43())

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
            frame.m_listCtrl2.SetItem(frame.m_listCtrl2.GetFocusedItem(), 1, '')
            frame.m_listCtrl2.SetItem(frame.m_listCtrl2.GetFocusedItem(), 3, self.m_textCtrl1.GetValue().lower())
        main.Enable(frame)
        frame.sort(None)
        self.Destroy()


class MyDialog3(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=language.s44(), pos=wx.DefaultPosition,
                           size=wx.Size(int('%.0f' % (450 * wx.GetDisplayPPI()[0] / 96)),
                                        int('%.0f' % (270 * wx.GetDisplayPPI()[0] / 96))),
                           style=wx.DEFAULT_DIALOG_STYLE)

        main.Disable(frame)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"Logo.bmp", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.Size(int('%.0f' % (100 * wx.GetDisplayPPI()[0] / 96)),
                                                                     int('%.0f' % (100 * wx.GetDisplayPPI()[0] / 96))),
                                         0)
        bSizer6.Add(self.m_bitmap1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY,
                                           language.s45() + '\n' + language.s47(sys.version.partition(' ')[0],
                                                                                wx.version().partition(' ')[0]) +
                                           '\n' + 'Copyright ©2024 ZHJ. All Rights Reserved.' + '\n',
                                           wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText1.Wrap(-1)

        bSizer6.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        self.m_hyperlink1 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"CSDN", u"https://blog.csdn.net/ZHJ0316",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE)
        gSizer3.Add(self.m_hyperlink1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_hyperlink2 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, u"GitHub", u"https://github.com/ZHJ00000",
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
                          size=wx.Size(int('%.0f' % (550 * wx.GetDisplayPPI()[0] / 96)),
                                       int('%.0f' % (280 * wx.GetDisplayPPI()[0] / 96))),
                          style=wx.DEFAULT_DIALOG_STYLE ^ wx.CLOSE_BOX)

        self.SetSizeHints(wx.DefaultSize, wx.Size(int('%.0f' % (750 * wx.GetDisplayPPI()[0] / 96)),
                                                  int('%.0f' % (450 * wx.GetDisplayPPI()[0] / 96))))
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
                                 wx.Size(int('%.0f' % (500 * wx.GetDisplayPPI()[0] / 96)),
                                         int('%.0f' % (25 * wx.GetDisplayPPI()[0] / 96))), wx.GA_HORIZONTAL)
        self.m_gauge1.SetValue(0)
        bSizer1.Add(self.m_gauge1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, language.s69(), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        bSizer1.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_gauge2 = wx.Gauge(self, wx.ID_ANY, 10000, wx.DefaultPosition,
                                 wx.Size(int('%.0f' % (500 * wx.GetDisplayPPI()[0] / 96)),
                                         int('%.0f' % (25 * wx.GetDisplayPPI()[0] / 96))),
                                 wx.GA_HORIZONTAL | wx.GA_PROGRESS)
        self.m_gauge2.SetValue(0)
        bSizer1.Add(self.m_gauge2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.close)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def close(self, event):
        pass


class MyDialog5(wx.Dialog):

    def __init__(self, parent, coding):
        global encoding, file
        main.Disable(frame)
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=language.s50() + ' - ' + file,
                           pos=wx.DefaultPosition, size=wx.Size(int('%.0f' % (500 * wx.GetDisplayPPI()[0] / 96)),
                                                                int('%.0f' % (400 * wx.GetDisplayPPI()[0] / 96))),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        bSizer101 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, language.s51(), wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)

        bSizer101.Add(self.m_staticText13, 0, wx.ALL, 5)

        m_listBox1Choices = ['ANSI', 'ASCII', 'BIG5', 'BIG5HKSCS', 'CHARMAP', 'CP037', 'CP1006', 'CP1026', 'CP1125',
                             'CP1140', 'CP1250', 'CP1251', 'CP1252', 'CP1253', 'CP1254', 'CP1255', 'CP1256', 'CP1257',
                             'CP1258',
                             'CP273', 'CP424', 'CP437', 'CP500', 'CP720', 'CP737', 'CP775', 'CP850', 'CP852', 'CP855',
                             'CP856', 'CP857', 'CP858', 'CP860', 'CP861', 'CP862', 'CP863', 'CP864', 'CP865', 'CP866',
                             'CP869', 'CP874', 'CP875', 'CP932', 'CP949', 'CP950', 'EUC_JISX0213', 'EUC_JIS_2004',
                             'EUC_JP', 'EUC_KR', 'GB18030', 'GB2312', 'GBK', 'HP_ROMAN8', 'HZ', 'IDNA', 'ISO2022_JP',
                             'ISO2022_JP_1', 'ISO2022_JP_2', 'ISO2022_JP_2004', 'ISO2022_JP_3', 'ISO2022_JP_EXT',
                             'ISO2022_KR', 'ISO8859_1', 'ISO8859_10', 'ISO8859_11', 'ISO8859_13', 'ISO8859_14',
                             'ISO8859_15', 'ISO8859_16', 'ISO8859_2', 'ISO8859_3', 'ISO8859_4', 'ISO8859_5',
                             'ISO8859_6', 'ISO8859_7', 'ISO8859_8', 'ISO8859_9', 'JOHAB', 'KOI8_R', 'KOI8_T', 'KOI8_U',
                             'KZ1048', 'LATIN_1', 'MAC_ARABIC', 'MAC_CROATIAN', 'MAC_CYRILLIC', 'MAC_FARSI',
                             'MAC_GREEK', 'MAC_ICELAND', 'MAC_LATIN2', 'MAC_ROMAN', 'MAC_ROMANIAN', 'MAC_TURKISH',
                             'MBCS', 'OEM', 'PALMOS', 'PTCP154', 'PUNYCODE', 'RAW_UNICODE_ESCAPE',
                             'SHIFT_JIS', 'SHIFT_JISX0213', 'SHIFT_JIS_2004', 'TIS_620', 'UNICODE_ESCAPE', 'UTF-16',
                             'UTF-16-BE', 'UTF-16-LE', 'UTF-32', 'UTF-32-BE', 'UTF-32-LE', 'UTF-7', 'UTF-8',
                             'UTF-8-SIG']
        self.m_listBox1 = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition,
                                     wx.Size(int('%.0f' % (230 * wx.GetDisplayPPI()[0] / 96)),
                                             int('%.0f' % (290 * wx.GetDisplayPPI()[0] / 96))), m_listBox1Choices,
                                     wx.LB_NEEDED_SB | wx.LB_SINGLE)
        try:
            self.m_listBox1.SetSelection(m_listBox1Choices.index(coding.upper()))
        except ValueError:
            self.m_listBox1.SetSelection(111)
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

        if coding.upper() not in m_listBox1Choices:
            encoding = 'utf-8'
        else:
            encoding = coding
        try:
            with open(file, 'r', encoding=encoding) as display:
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
            with open(file, 'r', encoding=encoding) as display:
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
        intask(file, encoding)


class MyDialog6(wx.Dialog):

    def __init__(self, parent):
        global information
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=language.s92(), pos=wx.DefaultPosition,
                           size=wx.Size(int('%.0f' % (500 * wx.GetDisplayPPI()[0] / 96)),
                                        int('%.0f' % (300 * wx.GetDisplayPPI()[0] / 96))),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_richText2 = wx.richtext.RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                                    wx.TE_READONLY | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        text = ''
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


if __name__ == '__main__':
    app = wx.App()
    sys.path.append(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3'))
    sys.path.append(os.path.dirname(sys.argv[0]))
    if not os.path.isdir(os.path.join(os.environ["APPDATA"], 'ZHJ')):
        os.mkdir(os.path.join(os.environ["APPDATA"], 'ZHJ'))
    if not os.path.isdir(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3')):
        os.mkdir(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3'))
    try:
        with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.ini'), 'r',
                  encoding='utf-8') as settingfile:
            setting = settingfile.readlines()
        for i in range(0, len(setting)):
            setting[i] = setting[i].rstrip()
    except Exception as err:
        with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.ini'), 'w',
                  encoding='utf-8') as settingfile:
            settingfile.write('Auto')
            setting = ['Auto']
    try:
        if setting[0] == 'Auto':
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'language.py'),
                      'w', encoding='utf-8') as languagefile:
                languagefile.write('from language_' + str(locale) + ' import *')
        else:
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'language.py'),
                      'w', encoding='utf-8') as languagefile:
                languagefile.write('from ' + setting[0] + ' import *')
        import language
    except Exception as err:
        try:
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'Setting.ini'), 'w',
                      encoding='utf-8') as settingfile:
                settingfile.write('language_English_United_States')
                setting = ['language_English_United_States']
            with open(os.path.join(os.environ["APPDATA"], 'ZHJ', 'FilesChecker3', 'language.py'),
                      'w', encoding='utf-8') as languagefile:
                languagefile.write('from ' + setting[0] + ' import *')
            import language
        except Exception as err:
            toastone = wx.MessageDialog(None, 'Unable to start program due to missing language pack.', 'FilesChecker Beta',
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
            toastone.SetOKLabel('&OK')
            if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
    else:
        frame = main(None)
        frame.Show(True)
        app.MainLoop()

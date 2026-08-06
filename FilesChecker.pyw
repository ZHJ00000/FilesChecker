import wx, wx.xrc, wx.richtext, wx.html  #pip install wxPython
import platform
import os
import sys
import time
import datetime
import shutil
import json
import ctypes
import locale
import importlib.util
import glob
import pyperclip  # pip install pyperclip
import markdown  # pip install markdown
import threading
import subprocess
import hashlib
import pyzipper  # pip install pyzipper
import base64
import zlib
from cryptography.hazmat.primitives import hashes, serialization  #pip install cryptography
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

import UI

locale1 = None
if platform.system() == 'Darwin':
    loc = 'C'
    try:
        loc = subprocess.check_output(
            ['defaults', 'read', '-g', 'AppleLocale'],
            text=True
        ).strip()
        os.environ['LANG'] = f"{loc.partition('@')[0]}.UTF-8"
        os.environ['LC_ALL'] = f"{loc.partition('@')[0]}.UTF-8"
    except Exception:
        os.environ['LANG'] = 'C.UTF-8'
        os.environ['LC_ALL'] = 'C.UTF-8'
    try:
        locale.setlocale(locale.LC_ALL, '')
    except locale.Error:
        locale1 = loc.partition('@')[0]
locale = locale.getlocale()[0]
if locale1:
    locale = locale1

Version = (4, 0, 1)
Build = '[__BUILD__]'  #Will be replaced in Build-Windows.py and Build-macOS.py.
if Build == '[__BU' + 'ILD__]':  #DO NOT edit this line!
    Build = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S')
arch = None
if platform.system() == 'Windows':
    arch = os.environ.get('PROCESSOR_ARCHITECTURE', '')
else:  #Darwin and Linux
    arch = platform.machine()

class LangProxy:
    def __init__(self, Langmodule, Englishmodule):
        self.Langmodule = Langmodule
        self.Englishmodule = Englishmodule

    def ChangeLang(self, NewLangmodule):
        self.Langmodule = NewLangmodule
    def __getattr__(self, name):
        if hasattr(self.Langmodule, name):
            return getattr(self.Langmodule, name)
        elif hasattr(self.Englishmodule, name):
            return getattr(self.Englishmodule, name)

Lang_PublicKey = '''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmK7pJ4z9d8Q4LSmGuyb/
d3nqZTdoQVDL+ujImA57k8Ps007nAUw+l796eq/WtVy8aUTSkjFssn6hS7tezh/9
wjMW9VTWrOXZn1Xjin2yB8fdIaqmAnTc3EIAnTI4AQlZ5BQETGAepuECO+C3/tfh
9OQsidiXSlNjvbdm+gysNj+ZBZvUxtA/f/AEu7Zz/6TjlkxbBXHqo/6exoeGFdeG
lFw/J2Y0F1lkbaRkc46esXXSeA1fMjiGUNXVSnJEIFogiC4od2sRNQSA80V6eFoQ
ArMBJP0/ehTu7nGbAuw7DRlzKv/DRj2NsMbKu/IeOqiI94uzcigytLCPZFll/9a1
9QIDAQAB
-----END PUBLIC KEY-----
'''
def Verify_Signature(doc_path: str, signature_path: str, public_key_str=Lang_PublicKey) -> bool:
    with open(doc_path, "rb") as f:
        data = f.read()
    if os.path.isfile(signature_path):
        with open(signature_path, "r", encoding="utf-8") as f:
            b64_sig = f.read().strip()
    else:
        return False
    try:
        signature = base64.b64decode(b64_sig)
    except Exception:
        return False

    public_key = serialization.load_pem_public_key(
        public_key_str.encode(),
        backend=default_backend()
    )
    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

def GetOSVersion():
    if platform.system() == 'Windows':
        ver = platform.version()
    elif platform.system() == 'Darwin':
        ver =  platform.mac_ver()[0]
    else:
        raise NotImplementedError('Unsupported OS: ' + platform.system())
    sysver = []
    for i in ver.split('.'):
        sysver.append(int(i))
    return sysver
if platform.system() == 'Windows':
    # Use DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 in Windows 10 1703 and above, Otherwise,
    # use DPI_AWARENESS_CONTEXT_SYSTEM_AWARE
    if tuple(GetOSVersion()) >= (10, 0, 15063):
        ctypes.windll.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))
    else:
        ctypes.windll.user32.SetProcessDPIAware()

def LoadSetting():
    with open(os.path.join(GetUserDataPath(), 'FilesChecker4', 'Setting.json'), 'r',
              encoding='utf-8') as settingfile:
        return json.loads(settingfile.read())
def SaveSetting(setting):
    with open(os.path.join(GetUserDataPath(), 'FilesChecker4', 'Setting.json'), 'w',
              encoding='utf-8') as settingfile:
        settingfile.write(json.dumps(setting))
        return None
def GetUserDataPath():
    if platform.system() == 'Windows':
        return os.path.join(os.environ["APPDATA"], 'ZHJ')
    elif platform.system() == 'Darwin':
        return os.path.join(os.environ["HOME"], "Library", "Application Support", "ZHJ")
    elif platform.system() == 'Linux':
        return os.path.join(os.environ["HOME"], ".local", "share", "ZHJ")
    else:
        raise NotImplementedError('Unsupported OS: ' + platform.system())
def GetProgPath():
    if os.path.basename(sys.argv[0]).split('.')[-1].lower().startswith('py'):
        return os.path.dirname(sys.argv[0])
    if platform.system() != 'Darwin':
        return os.path.dirname(sys.argv[0])
    else:
        return os.path.join(os.path.split(os.path.dirname(sys.argv[0]))[0], 'Resources')
def GetScaledSize(DPI, size: wx.Size):
    x = size.GetWidth()
    y = size.GetHeight()
    if platform.system() == 'Windows':
        if x != -1:
            x = int('%.0f' % (x * DPI[0] / 96))
        if y != -1:
            y = int('%.0f' % (y * DPI[0] / 96))
    return wx.Size(x, y)
def GetScaledWidth(DPI, x: int):
    if platform.system() == 'Windows':
        if x != -1:
            x = int('%.0f' % (x * DPI[0] / 96))
    return x
def Unzip(zip_file, password, output_path):
    with pyzipper.AESZipFile(zip_file) as zf:
        zf.extractall(output_path, pwd=password.encode())
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

with open(os.path.join(GetProgPath(), "Encodings.txt"), 'r', encoding='utf-8') as f:
    encodinglist = f.readlines()
encodingslist = [[], []]
for i in range(len(encodinglist)):
    encodinglist[i] = encodinglist[i].rstrip().split('==>')
    encodingslist[0].append(encodinglist[i][0])
    encodingslist[1].append(encodinglist[i][1])
del encodinglist
def find_encoding_key(coding: str, encodingslist=encodingslist):
    coding = coding.upper().replace('-', '_')
    if coding in encodingslist[1]:
        return coding
    else:
        if coding in encodingslist[0]:
            return encodingslist[1][encodingslist[0].index(coding)]
        else:
            return None

encodingchoices = ['ANSI', 'ASCII', 'BIG5', 'BIG5HKSCS', 'CP037', 'CP273', 'CP424', 'CP437', 'CP500',
                   'CP720', 'CP737', 'CP775', 'CP850', 'CP852', 'CP855', 'CP856', 'CP857', 'CP858',
                   'CP860', 'CP861', 'CP862', 'CP863', 'CP864', 'CP865', 'CP866', 'CP869', 'CP874',
                   'CP875', 'CP932', 'CP949', 'CP950', 'CP1006', 'CP1026', 'CP1125', 'CP1140', 'CP1250',
                   'CP1251', 'CP1252', 'CP1253', 'CP1254', 'CP1255', 'CP1256', 'CP1257', 'CP1258',
                   'EUC_JP', 'EUC_JIS_2004', 'EUC_JISX0213','EUC_KR', 'GB2312', 'GBK', 'GB18030', 'HZ',
                   'ISO2022_JP', 'ISO2022_JP_1', 'ISO2022_JP_2','ISO2022_JP_2004', 'ISO2022_JP_3',
                   'ISO2022_JP_EXT', 'ISO2022_KR', 'LATIN_1', 'ISO8859_2','ISO8859_3', 'ISO8859_4',
                   'ISO8859_5', 'ISO8859_6', 'ISO8859_7', 'ISO8859_8', 'ISO8859_9','ISO8859_10',
                   'ISO8859_11', 'ISO8859_13', 'ISO8859_14', 'ISO8859_15', 'ISO8859_16','JOHAB',
                   'KOI8_R', 'KOI8_T', 'KOI8_U', 'KZ1048', 'MAC_CYRILLIC', 'MAC_GREEK','MAC_ICELAND',
                   'MAC_LATIN2', 'MAC_ROMAN', 'MAC_TURKISH', 'OEM', 'PTCP154', 'SHIFT_JIS',
                   'SHIFT_JIS_2004', 'SHIFT_JISX0213', 'UTF_32', 'UTF_32_BE', 'UTF_32_LE', 'UTF_16',
                   'UTF_16_BE', 'UTF_16_LE', 'UTF_7', 'UTF_8', 'UTF_8_SIG']
if platform.system() != 'Windows':
    encodingchoices.remove(encodingchoices[0])

class OperationCancelledError(Exception):
    pass

class FileDrop(wx.FileDropTarget):
    def __init__(self, parent):
        wx.FileDropTarget.__init__(self)
        self.parent = parent

    def OnDropFiles(self, x, y, filePath):
        if self.parent.m_choice1.GetSelection() == 0:
            for i in filePath:
                if os.path.isdir(i) == False:
                    index = self.parent.m_listCtrl1.InsertItem(self.parent.m_listCtrl1.GetItemCount(),
                                                               str(self.parent.m_listCtrl1.GetItemCount() + 1))
                    self.parent.m_listCtrl1.SetItem(index, 1, '')
                    self.parent.m_listCtrl1.SetItem(index, 2, i)
                    self.parent.m_listCtrl1.SetItem(index, 3, '')
                    self.parent.informations.append(self.parent.information_default)
            self.parent.sort(None)
        elif self.parent.m_choice1.GetSelection() == 1:
            wx.CallAfter(self.parent.add_file, event=None, file=filePath[0])
        return False

class Main(UI.Main):
    def __init__(self, parent):
        UI.Main.__init__(self, parent)
        self.SetSize(GetScaledSize(self.GetDPI(), self.GetSize()))
        if platform.system() == 'Windows':
            self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        self.Centre()
        fileDrop = FileDrop(self)
        self.m_listCtrl1.SetDropTarget(fileDrop)
        self.informations = []
        self.information_default = {'Time': None, 'Error': None, 'ActualChecksum': None}
        self.SetStatusText(os.getcwd(), 1)
        self.m_choice1.SetSelection(setting['DefaultCheckMode'])
        self.mode = self.m_choice1.GetSelection()
        if platform.system() != 'Darwin':
            self.m_menu1.InsertSeparator(15)
        self.aftercmd = ''
        self.aftersave = ''
        self.ischeck = False
        self.change_lang_later_warn = None
        if platform.system() == 'Darwin':
            self.m_menu1.Remove(self.m_menuItem9)
            self.m_menubar1.OSXGetAppleMenu().Insert(1, self.m_menuItem9)
        self.change_lang()
        self.switch_mode(None)

    def change_lang(self):
        self.SetTitle(Lang.title())
        if platform.system() == 'Darwin':
            macoslocale = wx.Locale(Lang.macoslocale())
            if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                macoslocale.AddCatalogLookupPathPrefix(os.path.join(GetProgPath(), 'locale'))
            macoslocale.AddCatalog('wxstd')
            self.m_menubar1.OSXGetAppleMenu().SetTitle(Lang.title())
            self.m_menubar1.OSXGetAppleMenu().FindItemByPosition(0).SetItemLabel(Lang.menuitem_about())
            self.m_menubar1.OSXGetAppleMenu().FindItemByPosition(7).SetItemLabel(
                Lang.menuitem_hide_macos() + '\tCtrl+H')
            self.m_menubar1.OSXGetAppleMenu().FindItemByPosition(
                self.m_menubar1.OSXGetAppleMenu().GetMenuItemCount() - 1).SetItemLabel(
                Lang.menuitem_exit_macos() + '\tCtrl+Q')
        self.m_menuItem1.SetItemLabel(Lang.menuitem_startcheck() + '\tCtrl+Enter')
        self.m_menuItem1.SetHelp(Lang.menuitem_startcheck_help())
        if self.m_choice1.GetSelection() == 0:
            self.m_menuItem2.SetItemLabel(Lang.menuitem_addfile() + '\tCtrl+F')
            self.m_menuItem2.SetHelp(Lang.menuitem_addfile_help())
        elif self.m_choice1.GetSelection() == 1:
            self.m_menuItem2.SetItemLabel(Lang.menuitem_additem() + '\tCtrl+F')
            self.m_menuItem2.SetHelp(Lang.menuitem_additem_help())
        self.m_menuItem3.SetItemLabel(Lang.menuitem_addchecksum() + '\tCtrl+H')
        self.m_menuItem3.SetHelp(Lang.menuitem_addchecksum_help())
        self.m_menuItem4.SetItemLabel(Lang.menuitem_opentask() + '\tCtrl+O')
        self.m_menuItem4.SetHelp(Lang.menuitem_opentask_help())
        self.m_menuItem5.SetItemLabel(Lang.menuitem_savetask() + '\tCtrl+S')
        self.m_menuItem5.SetHelp(Lang.menuitem_savetask_help())
        self.m_menuItem6.SetItemLabel(Lang.menuitem_exportresult() + '\tCtrl+E')
        self.m_menuItem6.SetHelp(Lang.menuitem_exportresult_help())
        self.m_menuItem7.SetItemLabel(Lang.menuitem_clear())
        self.m_menuItem8.SetItemLabel(Lang.menuitem_workdir() + '\tAlt+D')
        if platform.system() == 'Darwin':
            self.m_menuItem9.SetItemLabel(Lang.menuitem_settings() + '\tCtrl+,')
        else:
            self.m_menuItem9.SetItemLabel(Lang.menuitem_settings() + '\tCtrl+Alt+S')
        self.m_menuItem9.SetHelp(Lang.menuitem_settings_help())
        if platform.system() != 'Darwin':
            self.m_menuItem10.SetItemLabel(Lang.menuitem_exit() + '\tAlt+F4')
            self.m_menuItem10.SetHelp(Lang.menuitem_exit_help())
        self.m_menubar1.SetMenuLabel(0, Lang.menu_task())
        self.m_menuItem11.SetItemLabel(Lang.menuitem_ota())
        self.m_menuItem12.SetItemLabel(Lang.menuitem_about())
        self.m_menuItem12.SetHelp(Lang.menuitem_about_help())
        self.m_menubar1.SetMenuLabel(1, Lang.menu_help())
        self.m_choice1.SetString(0, Lang.choice_mode1())
        self.m_choice1.SetString(1, Lang.choice_mode2())
        self.m_choice1.SetSize(self.m_choice1.GetBestSize())
        if self.m_choice1.GetSelection() == 0:
            self.m_button1.SetLabel(Lang.btn_addfile())
        elif self.m_choice1.GetSelection() == 1:
            self.m_button1.SetLabel(Lang.btn_additem())
        self.m_button1.SetSize(self.m_button1.GetBestSize())
        self.m_button2.SetLabel(Lang.btn_addchecksum())
        self.m_button2.SetSize(self.m_button2.GetBestSize())
        # ! Add button 'Add Item' for Mode 2
        self.m_button3.SetLabel(Lang.btn_startcheck())
        self.m_button3.SetSize(self.m_button3.GetBestSize())
        self.m_toolBar1.Realize()
        self.m_listCtrl1.DeleteAllItems()
        self.m_listCtrl1.DeleteAllColumns()
        if self.m_choice1.GetSelection() == 0:
            self.m_listCtrl1.InsertColumn(0, Lang.list_no())
            self.m_listCtrl1.InsertColumn(1, Lang.list_groupno())
            self.m_listCtrl1.InsertColumn(2, Lang.list_file())
            self.m_listCtrl1.InsertColumn(3, Lang.list_checksum())
            self.m_listCtrl1.SetColumnWidth(0, GetScaledWidth(self.GetDPI(), 50))  # 设置每一列的宽度
            self.m_listCtrl1.SetColumnWidth(1, GetScaledWidth(self.GetDPI(), 50))
            self.m_listCtrl1.SetColumnWidth(2, GetScaledWidth(self.GetDPI(), 425))
            self.m_listCtrl1.SetColumnWidth(3, GetScaledWidth(self.GetDPI(), 445))
        elif self.m_choice1.GetSelection() == 1:
            self.m_listCtrl1.InsertColumn(0, Lang.list_no())
            self.m_listCtrl1.InsertColumn(1, Lang.list_file())
            self.m_listCtrl1.InsertColumn(2, Lang.list_expected_checksum())
            self.m_listCtrl1.InsertColumn(3, Lang.list_result())
            self.m_listCtrl1.SetColumnWidth(0, GetScaledWidth(self.GetDPI(), 50))  # 设置每一列的宽度
            self.m_listCtrl1.SetColumnWidth(1, GetScaledWidth(self.GetDPI(), 425))
            self.m_listCtrl1.SetColumnWidth(2, GetScaledWidth(self.GetDPI(), 425))
            self.m_listCtrl1.SetColumnWidth(3, GetScaledWidth(self.GetDPI(), 75))
        self.m_menuItem13.SetItemLabel(Lang.rightmenu_show_details())
        self.m_menuItem14.SetItemLabel(Lang.rightmenu_reslect_file())
        self.m_menuItem15.SetItemLabel(Lang.rightmenu_edit_checksum())
        self.m_menuItem16.SetItemLabel(Lang.rightmenu_copy_file_address())
        self.m_menuItem17.SetItemLabel(Lang.rightmenu_copy_checksum())
        self.m_menuItem18.SetItemLabel(Lang.rightmenu_delete())

    def exit( self, event ):
        if not self.ischeck:
            if '/DEBUG:ForceEnableUpdate' in sys.argv[1:] or (
                    getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')):
                otadlg.Destroy()
            self.Destroy()
            sys.exit(0)

    def start_check( self, event ):
        self.calcdlg = Calculation(self)
        def filehash(path, algorithm):
            self.remain_size = os.path.getsize(path)
            size = self.remain_size
            Time_start = time.time()
            if self.iscancel:
                raise OperationCancelledError(Lang.error_operation_cancelled())
            with open(path, 'rb') as f:
                while self.remain_size >= 1048576:
                    Cur_Time1 = time.time()
                    if self.iscancel:
                        raise OperationCancelledError(Lang.error_operation_cancelled())
                    if self.ispause:
                        while self.ispause:
                            if self.iscancel:
                                raise OperationCancelledError(Lang.error_operation_cancelled())
                    algorithm.update(f.read(1024 * 1024))
                    self.remain_size -= 1048576
                    self.cur_all_size += 1048576
                    progress = ((size - self.remain_size) / size)
                    allprogress = (self.cur_all_size / self.total_all_size)
                    UsedTime = time.time()
                    speed = 1048576 / (UsedTime - Cur_Time1)
                    wx.CallAfter(self.calcdlg.update, (None, None), int((UsedTime - self.Time) // 1), None, None,
                                 self.calcdlg.sizeformat(speed, True), float('%.2f' % progress),
                                 float('%.2f' % allprogress))
                algorithm.update(f.read())
            self.cur_all_size += self.remain_size
            allprogress = (self.cur_all_size / self.total_all_size)
            wx.CallAfter(self.calcdlg.update, (None, None), None, None, None, None, 1, float('%.2f' % allprogress))
            self.informations.append(
                {'Time': time.time() - Time_start, 'Error': None, 'ActualChecksum': algorithm.hexdigest()})
            if setting['ChecksumUpper']:
                return algorithm.hexdigest().upper()
            else:
                return algorithm.hexdigest().lower()
        def filecrc32(path):
            self.remain_size = os.path.getsize(path)
            size = self.remain_size
            Time_start = time.time()
            crc = 0
            if self.iscancel:
                raise OperationCancelledError(Lang.error_operation_cancelled())
            with open(path, 'rb') as f:
                while self.remain_size >= 1048576:
                    Cur_Time1 = time.time()
                    if self.iscancel:
                        raise OperationCancelledError(Lang.error_operation_cancelled())
                    if self.ispause:
                        while self.ispause:
                            if self.iscancel:
                                raise OperationCancelledError(Lang.error_operation_cancelled())
                    block = f.read(1024 * 1024)
                    crc = zlib.crc32(block, crc)
                    self.remain_size -= 1048576
                    self.cur_all_size += 1048576
                    progress = ((size - self.remain_size) / size)
                    allprogress = (self.cur_all_size / self.total_all_size)
                    UsedTime = time.time()
                    speed = 1048576 / (UsedTime - Cur_Time1)
                    wx.CallAfter(self.calcdlg.update, (None, None), int((UsedTime - self.Time) // 1), None, None,
                                 self.calcdlg.sizeformat(speed, True), float('%.2f' % progress),
                                 float('%.2f' % allprogress))
                block = f.read()
                if block:
                    crc = zlib.crc32(block, crc)
            self.cur_all_size += self.remain_size
            allprogress = (self.cur_all_size / self.total_all_size)
            wx.CallAfter(self.calcdlg.update, (None, None), None, None, None, None, 1, float('%.2f' % allprogress))
            self.informations.append(
                {'Time': time.time() - Time_start, 'Error': None, 'ActualChecksum': str(hex(crc))[2:]})
            if setting['ChecksumUpper']:
                return str(hex(crc))[2:].upper()
            else:
                return str(hex(crc))[2:].lower()


        self.ischeck = True
        self.ispause = False
        self.iscancel = False
        self.SetStatusText(Lang.status_calculating())
        self.m_menuItem1.Enable(False)
        self.m_menuItem2.Enable(False)
        self.m_menuItem3.Enable(False)
        self.m_menuItem4.Enable(False)
        self.m_menuItem6.Enable(False)
        self.m_menuItem7.Enable(False)
        self.m_menuItem8.Enable(False)
        self.m_menuItem9.Enable(False)
        self.m_menuItem10.Enable(False)
        self.m_menuItem11.Enable(False)
        self.m_choice1.Enable(False)
        self.m_choice2.Enable(False)
        self.m_button1.Enable(False)
        self.m_button2.Enable(False)
        self.m_button3.Enable(False)
        self.m_listCtrl1.Enable(False)
        self.listitems = []
        if self.m_choice1.GetSelection() == 0:
            for i in range(0, self.m_listCtrl1.GetItemCount()):
                if self.m_listCtrl1.GetItemText(i, 1) == '':
                    self.listitems.append([int(self.m_listCtrl1.GetItemText(i, 0)), self.m_listCtrl1.GetItemText(i, 1),
                                      self.m_listCtrl1.GetItemText(i, 2), self.m_listCtrl1.GetItemText(i, 3)])
                else:
                    self.listitems.append(
                        [int(self.m_listCtrl1.GetItemText(i, 0)), int(self.m_listCtrl1.GetItemText(i, 1)),
                         self.m_listCtrl1.GetItemText(i, 2), self.m_listCtrl1.GetItemText(i, 3)])
        elif self.m_choice1.GetSelection() == 1:
            for i in range(0, self.m_listCtrl1.GetItemCount()):
                self.listitems.append(
                    [int(self.m_listCtrl1.GetItemText(i, 0)), self.m_listCtrl1.GetItemText(i, 1),
                     self.m_listCtrl1.GetItemText(i, 2), self.m_listCtrl1.GetItemText(i, 3)])
        self.listitems = sorted(self.listitems, key=lambda x: x[0],
                           reverse=False)
        self.total_count = 0
        self.cur_count = 0
        self.total_all_size = 0
        self.cur_all_size = 0
        self.informations = []
        for i in range(0, frame.m_listCtrl1.GetItemCount()):
            if self.m_choice1.GetSelection() == 0:
                if self.listitems[i][2] != '':
                    self.total_count += 1
                    try:
                        self.total_all_size += os.path.getsize(self.listitems[i][2])
                    except Exception:
                        continue
            elif self.m_choice1.GetSelection() == 1:
                self.total_count += 1
                try:
                    self.total_all_size += os.path.getsize(self.listitems[i][1])
                except Exception:
                    continue

        if self.total_count > 0:
            self.calcdlg.Show()
        if self.m_choice1.GetSelection() == 0:
            self.columns = (2, 3)
        else:
        #elif self.m_choice1.GetSelection() == 1:
            self.columns = (1, 3)
        self.Time = time.time()
        def operate():
            for i in range(0, frame.m_listCtrl1.GetItemCount()):
                self.remain_size = 0
                if not (self.m_choice1.GetSelection() == 0 and self.listitems[i][self.columns[0]] == ''):
                    self.cur_count += 1
                    if os.path.isfile(self.listitems[i][self.columns[0]]):
                        wx.CallAfter(self.calcdlg.update, (self.cur_count, self.total_count), None,
                                     self.listitems[i][self.columns[0]], os.path.getsize(
                                self.listitems[i][self.columns[0]]), None, None, None)
                    algorithms = {'MD5': hashlib.md5(),
                                  'SHA-1': hashlib.sha1(),
                                  'SHA-224': hashlib.sha224(),
                                  'SHA-256': hashlib.sha256(),
                                  'SHA-384': hashlib.sha384(),
                                  'SHA-512': hashlib.sha512(),
                                  'SHA3-224': hashlib.sha3_224(),
                                  'SHA3-256': hashlib.sha3_256(),
                                  'SHA3-384': hashlib.sha3_384(),
                                  'SHA3-512': hashlib.sha3_512(),
                                  'BLAKE2b': hashlib.blake2b(),
                                  'BLAKE2s': hashlib.blake2s()
                                  }
                    try:
                        if self.m_choice2.GetString(self.m_choice2.GetSelection()) != 'CRC-32':
                            self.listitems[i][self.columns[1]] = filehash(self.listitems[i][self.columns[0]],
                                                                          algorithms[self.m_choice2.GetString(
                                                                              self.m_choice2.GetSelection())])
                        else:
                            self.listitems[i][self.columns[1]] = filecrc32(self.listitems[i][self.columns[0]])
                    except Exception as err:
                        self.cur_all_size += self.remain_size
                        self.informations.append(
                            {'Time': None, 'Error': type(err).__name__ + ': ' + str(err), 'ActualChecksum': None})
                        self.listitems[i][self.columns[1]] = Lang.str_error()
                        continue
                else:
                    self.informations.append(self.information_default)
            self.ischeck = False
            wx.CallAfter(self.calcdlg.Destroy)
            wx.CallAfter(self.SetStatusText, Lang.status_checking())
            if self.m_choice1.GetSelection() == 0:
                group = []
                for i in range(0, self.m_listCtrl1.GetItemCount()):
                    tf = False
                    if self.listitems[i][3] != Lang.str_error():
                        for ii in range(0, len(group)):
                            if self.listitems[i][3] == group[ii]:
                                self.listitems[i][1] = ii
                                tf = True
                                break
                        if not tf:
                            group.append(self.listitems[i][3])
                            self.listitems[i][1] = len(group) - 1
            elif self.m_choice1.GetSelection() == 1:
                for i in range(0, self.m_listCtrl1.GetItemCount()):
                    if self.listitems[i][3] != Lang.str_error():
                        if self.listitems[i][3] == self.listitems[i][2]:
                            self.listitems[i][3] = 1
                        else:
                            self.listitems[i][3] = 0
            if self.m_listCtrl1.GetSortIndicator() != -1:
                self.listitems = sorted(self.listitems, key=lambda x: x[self.m_listCtrl1.GetSortIndicator()],
                                        reverse=not self.m_listCtrl1.IsAscendingSortIndicator())
            for i in range(0, len(self.listitems)):
                wx.CallAfter(self.m_listCtrl1.SetItem, i, 0, str(self.listitems[i][0]))
                wx.CallAfter(self.m_listCtrl1.SetItem, i, 1, str(self.listitems[i][1]))
                wx.CallAfter(self.m_listCtrl1.SetItem, i, 2, str(self.listitems[i][2]))
                wx.CallAfter(self.m_listCtrl1.SetItem, i, 3, str(self.listitems[i][3]))
                if self.m_choice1.GetSelection() == 1:
                    if str(self.listitems[i][3]) == '1':
                        wx.CallAfter(self.m_listCtrl1.SetItemBackgroundColour, i, wx.Colour(198, 239, 206))    #Green
                    elif str(self.listitems[i][3]) == Lang.str_error():
                        wx.CallAfter(self.m_listCtrl1.SetItemBackgroundColour, i, wx.Colour(255, 235, 156))    #Yellow
                    elif str(self.listitems[i][3]) == '0':
                        wx.CallAfter(self.m_listCtrl1.SetItemBackgroundColour, i, wx.Colour(255, 199, 206))    #Red
            self.m_menuItem1.Enable(True)
            self.m_menuItem2.Enable(True)
            self.m_menuItem3.Enable(True)
            self.m_menuItem4.Enable(True)
            self.m_menuItem6.Enable(True)
            self.m_menuItem7.Enable(True)
            self.m_menuItem8.Enable(True)
            self.m_menuItem9.Enable(True)
            self.m_menuItem10.Enable(True)
            if '/DEBUG:ForceEnableUpdate' in sys.argv[1:] or (
                    getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')):
                self.m_menuItem11.Enable(True)
            self.m_choice1.Enable(True)
            self.m_choice2.Enable(True)
            self.m_button1.Enable(True)
            self.m_button2.Enable(True)
            self.m_button3.Enable(True)
            self.m_listCtrl1.Enable(True)
            wx.CallAfter(self.SetStatusText, '')
            if self.aftersave:
                wx.CallAfter(self.SetStatusText, Lang.status_exporting(self.aftersave))
                wx.CallAfter(self.export_main, self.aftersave)
            if self.aftercmd:
                wx.CallAfter(self.SetStatusText, Lang.status_saving(self.aftercmd))
                try:
                    os.startfile(self.aftercmd)
                except FileNotFoundError:
                    try:
                        subprocess.Popen(self.aftercmd)
                    except Exception as err:
                        toastone = wx.MessageDialog(None, Lang.error_message(type(err).__name__ + ': ' + str(err)),
                                                    Lang.title(),
                                                    wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                        toastone.SetOKLabel(Lang.dlg_btn_ok())
                        if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                            toastone.Destroy()
                except Exception as err:
                    toastone = wx.MessageDialog(None, Lang.error_message(type(err).__name__ + ': ' + str(err)),
                                                Lang.title(),
                                                wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                    toastone.SetOKLabel(Lang.dlg_btn_ok())
                    if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                        toastone.Destroy()
            wx.CallAfter(self.SetStatusText, '')
            wx.CallAfter(self.Layout)


        thread1 = threading.Thread(target=operate, args=(), daemon=True)
        thread1.start()


    def add_file( self, event, file=None ):
        if self.m_choice1.GetSelection() == 0:
            dlg = wx.FileDialog(self, message=Lang.filedlg_title_add(),
                                defaultDir='',
                                defaultFile='',
                                wildcard=Lang.filedlg_wildcard_1(),
                                style=wx.FD_OPEN | wx.FD_MULTIPLE)
            if dlg.ShowModal() == wx.ID_OK:
                fahs = dlg.GetPaths()
                dlg.Destroy()
                for fah in fahs:
                    index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),
                                                         str(self.m_listCtrl1.GetItemCount() + 1))
                    self.m_listCtrl1.SetItem(index, 1, '')
                    self.m_listCtrl1.SetItem(index, 2, fah)
                    self.m_listCtrl1.SetItem(index, 3, '')
                    self.informations.append(self.information_default)
                self.sort(None)
        elif self.m_choice1.GetSelection() == 1:
            itemdlg = ItemDialog(self)
            if file:
                itemdlg.set_file(file)
            if itemdlg.ShowModal() == wx.ID_OK:
                fah = itemdlg.get_input()
                itemdlg.Destroy()
                index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),
                                                     str(self.m_listCtrl1.GetItemCount() + 1))
                self.m_listCtrl1.SetItem(index, 1, fah[0])
                if setting['ChecksumUpper']:
                    self.m_listCtrl1.SetItem(index, 2, fah[1].upper())
                else:
                    self.m_listCtrl1.SetItem(index, 2, fah[1].lower())
                self.m_listCtrl1.SetItem(index, 3, '')
                self.informations.append(self.information_default)
                self.sort(None)

    def add_checksum( self, event ):
        dlg = ChecksumDialog(self)
        dlg.set_mode(False)
        if dlg.ShowModal() == wx.ID_OK:
            index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),
                                                str(self.m_listCtrl1.GetItemCount() + 1))
            self.m_listCtrl1.SetItem(index, 1, '')
            self.m_listCtrl1.SetItem(index, 2, '')
            if setting['ChecksumUpper']:
                self.m_listCtrl1.SetItem(index, 3, dlg.get_checksum().upper())
            else:
                self.m_listCtrl1.SetItem(index, 3, dlg.get_checksum().lower())
            self.informations.append(self.information_default)
        dlg.Destroy()

    def intask(self, file, encoding):
        try:
            with open(file, 'r', encoding=encoding, errors='replace') as file:
                l = file.readlines()
        except Exception as err:
            tf = False
            toastone = wx.MessageDialog(None, Lang.error_loading_task(type(err).__name__ + ': ' + str(err)), Lang.title(),
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
            toastone.SetOKLabel(Lang.dlg_btn_ok())
            if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
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
                toastone = wx.MessageDialog(None, Lang.error_unsupported_algorithm(), Lang.title(),
                                            wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                toastone.SetOKLabel(Lang.dlg_btn_ok())
                if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                    toastone.Destroy()
            else:
                for i in range(0, len(l)):
                    l[i] = l[i].rstrip()
                if l[0].startswith('<code: ') and l[0].endswith('>'):
                    del l[0]
                l[0] = l[0].lower()
                if l[0] == 'md5':
                    self.m_choice2.SetSelection(0)
                    tf = True
                elif l[0] == 'sha1' or l[0] == 'sha-1':
                    self.m_choice2.SetSelection(1)
                    tf = True
                elif l[0] == 'sha224' or l[0] == 'sha-224':
                    self.m_choice2.SetSelection(2)
                    tf = True
                elif l[0] == 'sha256' or l[0] == 'sha-256':
                    self.m_choice2.SetSelection(3)
                    tf = True
                elif l[0] == 'sha384' or l[0] == 'sha-384':
                    self.m_choice2.SetSelection(4)
                    tf = True
                elif l[0] == 'sha512' or l[0] == 'sha-512':
                    self.m_choice2.SetSelection(5)
                    tf = True
                elif l[0] == 'sha3-224':
                    self.m_choice2.SetSelection(6)
                    tf = True
                elif l[0] == 'sha3-256':
                    self.m_choice2.SetSelection(7)
                    tf = True
                elif l[0] == 'sha3-384':
                    self.m_choice2.SetSelection(8)
                    tf = True
                elif l[0] == 'sha3-512':
                    self.m_choice2.SetSelection(9)
                    tf = True
                elif l[0] == 'blake2b':
                    self.m_choice2.SetSelection(10)
                    tf = True
                elif l[0] == 'blake2s':
                    self.m_choice2.SetSelection(11)
                    tf = True
                elif l[0] == 'crc32' or l[0] == 'crc-32':
                    self.m_choice2.SetSelection(12)
                    tf = True
                else:
                    toastone = wx.MessageDialog(None, Lang.error_unsupported_algorithm(), Lang.title(),
                                                wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                    toastone.SetOKLabel(Lang.dlg_btn_ok())
                    if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                        toastone.Destroy()
                    tf = False
        if tf:
            ll = []
            for i in range(len(l)):
                ll.append(l[i].lower())
            try:
                if ll[1] != '<file>' and ll[1] != '<hash>':
                    tf = False
                    toastone = wx.MessageDialog(None, Lang.error_not_defined(), Lang.title(),
                                                wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                    toastone.SetOKLabel(Lang.dlg_btn_ok())
                    if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                        toastone.Destroy()
            except IndexError:
                toastone = wx.MessageDialog(None, Lang.error_nodata(), Lang.title(),
                                            wx.OK | wx.OK_DEFAULT | wx.ICON_WARNING)
                toastone.SetOKLabel(Lang.dlg_btn_ok())
                if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                    toastone.Destroy()
                tf = False
        if tf:
            foha = ''
            count = self.m_listCtrl1.GetItemCount()
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
                            index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),
                                                                 str(self.m_listCtrl1.GetItemCount() + 1))
                            self.m_listCtrl1.SetItem(index, 1, '')
                            self.m_listCtrl1.SetItem(index, 2, l[i])
                            self.m_listCtrl1.SetItem(index, 3, '')
                            self.informations.append(self.information_default)
                        else:
                            for i in range(0, len(fs)):
                                if os.path.isfile(fs[i]) == False:
                                    fs[i] = ''
                            while '' in fs:
                                fs.remove('')
                            for fah in fs:
                                index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),
                                                                     str(self.m_listCtrl1.GetItemCount() + 1))
                                self.m_listCtrl1.SetItem(index, 1, '')
                                self.m_listCtrl1.SetItem(index, 2, fah)
                                self.m_listCtrl1.SetItem(index, 3, '')
                                self.informations.append(self.information_default)
                    elif foha == 2:
                        if setting['ChecksumUpper']:
                            l[i] = l[i].upper()
                        else:
                            l[i] = l[i].lower()
                        index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),
                                                             str(self.m_listCtrl1.GetItemCount() + 1))
                        self.m_listCtrl1.SetItem(index, 1, '')
                        self.m_listCtrl1.SetItem(index, 2, '')
                        self.m_listCtrl1.SetItem(index, 3, l[i])
                        self.informations.append(self.information_default)
            if count == self.m_listCtrl1.GetItemCount():
                toastone = wx.MessageDialog(None, Lang.error_nodata(), Lang.title(),
                                            wx.OK | wx.OK_DEFAULT | wx.ICON_WARNING)
                toastone.SetOKLabel(Lang.dlg_btn_ok())
                if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                    toastone.Destroy()
            self.sort(None)

    def open_task( self, event ):
        if self.m_choice1.GetSelection() == 0:
            dlg = wx.FileDialog(self, message=Lang.filedlg_title_opentask(),
                                defaultDir='',
                                defaultFile='',
                                wildcard=Lang.filedlg_wildcard_2(),
                                style=wx.FD_OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                file = dlg.GetPath()
                dlg.Destroy()
                encodingpick = None
                modal = None
                try:
                    with open(file, 'rb') as f:
                        coding = f.readline().decode('ascii').rstrip()
                except UnicodeDecodeError:
                    with open(file, 'rb') as f:
                        coding = f.readline()
                    BOM2Encoding = {b'\xef\xbb\xbf': 'UTF_8',
                                    b'\x00\x00\xfe\xff': 'UTF_32',
                                    b'\xff\xfe\x00\x00': 'UTF_32',
                                    b'\xfe\xff': 'UTF_16',
                                    b'\xff\xfe': 'UTF_16',
                                    b'\x2b\x2f\x76': 'UTF_7',
                                    b'\x84\x31\x95\x33': 'GB18030'}
                    tf = False
                    for i in BOM2Encoding.keys():
                        if coding.startswith(i):
                            try:
                                with open(file, 'r', encoding=BOM2Encoding[i]) as f:
                                    f.read()
                                self.intask(file, BOM2Encoding[i])
                            except UnicodeDecodeError:
                                encodingpick = EncodingPicker(self)
                                encodingpick.set_file(file)
                                encodingpick.set_encoding(BOM2Encoding[i])
                                modal = encodingpick.ShowModal()
                            tf = True
                            break
                    if not tf:
                        encodingpick = EncodingPicker(self)
                        encodingpick.set_file(file)
                        encodingpick.set_encoding('UTF_8')
                        modal = encodingpick.ShowModal()
                else:
                    if coding.startswith('<code: ') and coding.endswith('>'):
                        try:
                            with open(file, 'r', encoding=find_encoding_key(coding[7:-1])) as f:
                                f.read()
                        except (UnicodeDecodeError, LookupError):
                            encodingpick = EncodingPicker(self)
                            encodingpick.set_file(file)
                            encodingpick.set_encoding(find_encoding_key(coding[7:-1]))
                            modal = encodingpick.ShowModal()
                        else:
                            self.intask(file, str(find_encoding_key(coding[7:-1])))
                    else:
                        encodingpick = EncodingPicker(self)
                        encodingpick.set_file(file)
                        encodingpick.set_encoding('UTF_8')
                        modal = encodingpick.ShowModal()
                if encodingpick:
                    if modal == wx.ID_OK:
                        self.intask(file, encodingpick.get_encoding())
                    encodingpick.Destroy()
        elif self.m_choice1.GetSelection() == 1:
            dlg = OpenTaskDialog(self)
            if dlg.ShowModal() == wx.ID_OK:
                for i in dlg.get_input().split('\n'):
                    if i:
                        splitedline = i.split(' ')
                        while len(splitedline) >= 2 and splitedline[1] == '':
                            del splitedline[1]
                        fah = ''
                        for j in splitedline[1:]:
                            fah += j + ' '

                        index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),
                                                             str(self.m_listCtrl1.GetItemCount() + 1))
                        fah = fah[:-1]
                        if fah:
                            if (fah[0] == '"' and fah[-1] == '"') or (fah[0] == "'" and fah[-1] == "'"):
                                fah = fah[1:-1]
                            if fah[0] == '*':
                                fah = fah[1:]
                            self.m_listCtrl1.SetItem(index, 1, fah)
                        else:
                            self.m_listCtrl1.SetItem(index, 1, '')
                        if setting['ChecksumUpper']:
                            self.m_listCtrl1.SetItem(index, 2, i.split(' ')[0].upper())
                        else:
                            self.m_listCtrl1.SetItem(index, 2, i.split(' ')[0].lower())
                        self.m_listCtrl1.SetItem(index, 3, '')
                        self.informations.append(self.information_default)
                frame.sort(None)


    def save_task( self, event ):
        dlg = wx.FileDialog(self, message=Lang.filedlg_title_savetask(),
                            defaultDir='',
                            defaultFile='',
                            wildcard=Lang.filedlg_wildcard_2(),
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText(Lang.status_saving(dlg.GetPath()))
            try:
                with open(dlg.GetPath(), 'w', encoding=str(setting['SaveTaskEncoding'])) as file:
                    dlg.Destroy()
                    if self.m_choice1.GetSelection() == 0:
                        if not setting['CompatibleWithOldTask']:
                            f = '<code: ' + str(setting['SaveTaskEncoding']) + '>\n' + frame.m_choice2.GetString(
                                frame.m_choice2.GetSelection()) + '\n'
                        else:
                            f = frame.m_choice2.GetString(frame.m_choice2.GetSelection()) + '\n'
                        if frame.m_listCtrl1.GetItemCount() != 0:
                            foha = ''
                            for i in range(0, frame.m_listCtrl1.GetItemCount()):
                                if frame.m_listCtrl1.GetItemText(i, 2) == '' and foha != 2:
                                    foha = 2
                                    f = f + '<hash>\n' + frame.m_listCtrl1.GetItemText(i, 3) + '\n'
                                elif frame.m_listCtrl1.GetItemText(i, 2) == '' and foha == 2:
                                    f = f + frame.m_listCtrl1.GetItemText(i, 3) + '\n'
                                elif frame.m_listCtrl1.GetItemText(i, 2) != '' and foha != 1:
                                    foha = 1
                                    f = f + '<file>\n' + frame.m_listCtrl1.GetItemText(i, 2).replace('#', '##') + '\n'
                                elif frame.m_listCtrl1.GetItemText(i, 2) != '' and foha == 1:
                                    f = f + frame.m_listCtrl1.GetItemText(i, 2).replace('#', '##') + '\n'
                    elif self.m_choice1.GetSelection() == 1:
                        f = ''
                        for i in range(0, frame.m_listCtrl1.GetItemCount()):
                            if frame.m_listCtrl1.GetItemText(i, 2):
                                f += frame.m_listCtrl1.GetItemText(i, 2) + ' ' + frame.m_listCtrl1.GetItemText(i,
                                                                                                               1) + '\n'
                            else:
                                f += '<empty> ' + frame.m_listCtrl1.GetItemText(i, 1) + '\n'
                    file.write(f)
            except Exception as err:
                toastone = wx.MessageDialog(None, Lang.error_message(type(err).__name__ + ': ' + str(err)), Lang.title(),
                                            wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                toastone.SetOKLabel(Lang.dlg_btn_ok())
                if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                    toastone.Destroy()
            self.SetStatusText('')

    def export( self, event ):
        dlg = wx.FileDialog(self, message=Lang.filedlg_title_exportresult(),
                            defaultDir='',
                            defaultFile='',
                            wildcard=Lang.filedlg_wildcard_3(),
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            dlg.Destroy()
            self.SetStatusText(Lang.status_exporting(path))
            self.export_main(path)
            self.SetStatusText('')

    def export_main( self, path ):
        try:
            with open(path, 'w', encoding=str(setting['ExportResultEncoding'])) as file:
                if self.m_choice1.GetSelection() == 0:
                    file.write(
                        Lang.list_no() + ',' + Lang.list_groupno() + ',' + Lang.list_file() + ',' + Lang.list_checksum() + '\n')
                elif self.m_choice1.GetSelection() == 1:
                    file.write(
                        Lang.list_no() + ',' + Lang.list_file() + ',' + Lang.list_expected_checksum() + ',' + Lang.list_result() + '\n')
                for i in range(0, self.m_listCtrl1.GetItemCount()):
                    for ii in range(0, 4):
                        if ii == 3:
                            file.write('"' + self.m_listCtrl1.GetItemText(i, 3) + '"\n')
                        else:
                            file.write('"' + self.m_listCtrl1.GetItemText(i, ii) + '",')
        except Exception as err:
            toastone = wx.MessageDialog(None, Lang.error_message(type(err).__name__ + ': ' + str(err)), Lang.title(),
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
            toastone.SetOKLabel(Lang.dlg_btn_ok())
            if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                toastone.Destroy()

    def right_menu( self, event ):
        self.m_menuItem14.Enable(True)
        self.m_menuItem15.Enable(True)
        self.m_menuItem16.Enable(True)
        self.m_menuItem17.Enable(True)
        if self.m_choice1.GetSelection() == 0:
            if self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 2) == '':
                self.m_menuItem14.Enable(False)
                self.m_menuItem16.Enable(False)
            if self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(),
                                            3) == '' or self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(),
                                                                                     3) == Lang.str_error():
                self.m_menuItem17.Enable(False)
            if self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 2) != '':
                self.m_menuItem15.Enable(False)
        elif self.m_choice1.GetSelection() == 1:
            if self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(),
                                            2) == '':
                self.m_menuItem17.Enable(False)
        self.PopupMenu(self.m_menu3)

    def clear_list( self, event ):
        self.m_listCtrl1.DeleteAllItems()
        self.informations = []

    def work_directory( self, event ):
        dlg = wx.DirDialog(self, message=Lang.workdirdlg_title(),
                           defaultPath='',
                           style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            os.chdir(dlg.GetPath())
            self.SetStatusText(os.getcwd(), 1)

    def open_settings( self, event ):
        settingdlg = Settings(self)
        a = settingdlg.ShowModal()
        if a == wx.ID_OK:
            settingdlg.apply(None)
            settingdlg.Destroy()
        elif a == wx.ID_CANCEL:
            settingdlg.Destroy()


    def ota( self, event ):
        otadlg.Show(True)
        frame.Enable(False)

    def about( self, event ):
        aboutdlg = About(self)
        aboutdlg.ShowModal()

    def switch_mode( self, event ):
        if self.m_choice1.GetSelection() != self.mode:
            if self.m_listCtrl1.GetItemCount():
                toastone = wx.MessageDialog(None, Lang.switchmode_warning(), Lang.title(),
                                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)
                toastone.SetYesNoLabels(Lang.dlg_btn_yes(), Lang.dlg_btn_no())
                if toastone.ShowModal() == wx.ID_NO:  # 如果点击了提示框的否按钮
                    toastone.Destroy()
                    self.m_choice1.SetSelection(self.mode)
                    return None
            self.m_listCtrl1.DeleteAllItems()
            self.m_listCtrl1.RemoveSortIndicator()
            self.m_listCtrl1.DeleteAllColumns()
            if self.m_choice1.GetSelection() == 0:
                self.m_listCtrl1.InsertColumn(0, Lang.list_no())
                self.m_listCtrl1.InsertColumn(1, Lang.list_groupno())
                self.m_listCtrl1.InsertColumn(2, Lang.list_file())
                self.m_listCtrl1.InsertColumn(3, Lang.list_checksum())
                self.m_listCtrl1.SetColumnWidth(0, GetScaledWidth(self.GetDPI(), 50))  # 设置每一列的宽度
                self.m_listCtrl1.SetColumnWidth(1, GetScaledWidth(self.GetDPI(), 50))
                self.m_listCtrl1.SetColumnWidth(2, GetScaledWidth(self.GetDPI(), 425))
                self.m_listCtrl1.SetColumnWidth(3, GetScaledWidth(self.GetDPI(), 445))
                self.m_menuItem2.SetItemLabel(Lang.menuitem_addfile() + '\tCtrl+F')
                self.m_menuItem2.SetHelp(Lang.menuitem_addfile_help())
                self.m_menu1.Insert(3, self.m_menuItem3)
                self.m_button1.SetLabel(Lang.btn_addfile())
                self.m_button1.SetSize(self.m_button1.GetBestSize())
                self.m_button2.Show(True)
                self.m_toolBar1.InsertControl(3, self.m_button2)
                self.m_toolBar1.Realize()
            elif self.m_choice1.GetSelection() == 1:
                self.m_listCtrl1.InsertColumn(0, Lang.list_no())
                self.m_listCtrl1.InsertColumn(1, Lang.list_file())
                self.m_listCtrl1.InsertColumn(2, Lang.list_expected_checksum())
                self.m_listCtrl1.InsertColumn(3, Lang.list_result())
                self.m_listCtrl1.SetColumnWidth(0, GetScaledWidth(self.GetDPI(), 50))  # 设置每一列的宽度
                self.m_listCtrl1.SetColumnWidth(1, GetScaledWidth(self.GetDPI(), 425))
                self.m_listCtrl1.SetColumnWidth(2, GetScaledWidth(self.GetDPI(), 425))
                self.m_listCtrl1.SetColumnWidth(3, GetScaledWidth(self.GetDPI(), 75))
                self.m_listCtrl1.SetDropTarget(None)
                self.m_menuItem2.SetItemLabel(Lang.menuitem_additem() + '\tCtrl+F')
                self.m_menuItem2.SetHelp(Lang.menuitem_additem_help())
                self.m_menu1.Remove(self.m_menuItem3)
                self.m_button1.SetLabel(Lang.btn_additem())
                self.m_button1.SetSize(self.m_button1.GetBestSize())
                self.m_button2.Show(False)
                self.m_toolBar1.RemoveTool(self.m_button2.GetId())
                self.m_toolBar1.Realize()
            self.mode = self.m_choice1.GetSelection()
            fileDrop = FileDrop(self)
            self.m_listCtrl1.SetDropTarget(fileDrop)
        return None




    def show_detail( self, event ):
        text = ''
        if self.m_choice1.GetSelection() == 0:
            if self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 2) == '':
                text += Lang.detailsdlg_file() + Lang.detailsdlg_none() + '\n'
                text += Lang.detailsdlg_checksum() + self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(),
                                                                                  3) + '\n'
            else:
                text += Lang.detailsdlg_file() + self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(),
                                                                              2) + '\n'
                if self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 3) == '':
                    text += Lang.detailsdlg_checksum() + Lang.detailsdlg_none() + '\n'
                else:
                    text += Lang.detailsdlg_checksum() + self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(),
                                                                                      3) + '\n'

        elif self.m_choice1.GetSelection() == 1:
            text += Lang.detailsdlg_file() + self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 1) + '\n'
            if self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 2) == '':
                text += Lang.detailsdlg_expected_checksum() + Lang.detailsdlg_none() + '\n'
            else:
                text += Lang.detailsdlg_expected_checksum() + self.m_listCtrl1.GetItemText(
                    self.m_listCtrl1.GetFocusedItem(), 2) + '\n'
            if self.informations[int(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 0)) - 1][
                'ActualChecksum']:
                text += Lang.detailsdlg_actual_checksum() + \
                        self.informations[int(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 0)) - 1][
                            'ActualChecksum'] + '\n'
            else:
                text += Lang.detailsdlg_actual_checksum() + Lang.detailsdlg_none() + '\n'
        if self.informations[int(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 0)) - 1][
            'Time'] is None:
            text += Lang.detailsdlg_time() + Lang.detailsdlg_none() + '\n'
        else:
            text += Lang.detailsdlg_time() + timeformat(int(self.informations[
                int(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 0)) - 1]['Time'] // 1)) + '\n'
        if self.informations[int(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 0)) - 1][
            'Error'] is None:
            text += Lang.detailsdlg_error() + Lang.detailsdlg_none() + '\n'
        else:
            text += Lang.detailsdlg_error() + self.informations[
                int(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 0)) - 1]['Error'] + '\n'
        detailsdlg = Details(self)
        detailsdlg.set_value(text)
        detailsdlg.ShowModal()


    def reselect_file( self, event ):
        dlg = wx.FileDialog(self, message=Lang.filedlg_title_reselect(),
                            defaultDir=os.path.dirname(
                                self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 2)),
                            defaultFile='',
                            wildcard=Lang.filedlg_wildcard_1(),
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            fahs = dlg.GetPath()
            dlg.Destroy()
            if self.m_choice1.GetSelection() == 0:
                self.m_listCtrl1.SetItem(self.m_listCtrl1.GetFocusedItem(), 1, '')
                self.m_listCtrl1.SetItem(self.m_listCtrl1.GetFocusedItem(), 2, fahs)
            elif self.m_choice1.GetSelection() == 1:
                self.m_listCtrl1.SetItem(self.m_listCtrl1.GetFocusedItem(), 1, fahs)
                self.m_listCtrl1.SetItemBackgroundColour(self.m_listCtrl1.GetFocusedItem(), wx.Colour(-1, -1, -1))
            self.m_listCtrl1.SetItem(self.m_listCtrl1.GetFocusedItem(), 3, '')
            self.informations[
                int(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 0)) - 1] = self.information_default
            self.sort(None)

    def edit_checksum( self, event ):
        dlg = ChecksumDialog(self)
        dlg.set_mode(True)
        if self.m_choice1.GetSelection() == 0:
            dlg.set_checksum(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 3))
        else:
            dlg.set_checksum(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 2))
        if dlg.ShowModal() == wx.ID_OK:
            if self.m_choice1.GetSelection() == 0:
                self.m_listCtrl1.SetItem(self.m_listCtrl1.GetFocusedItem(), 1, '')
                if setting['ChecksumUpper']:
                    self.m_listCtrl1.SetItem(self.m_listCtrl1.GetFocusedItem(), 3,
                                             dlg.get_checksum().upper())
                else:
                    self.m_listCtrl1.SetItem(self.m_listCtrl1.GetFocusedItem(), 3,
                                             dlg.get_checksum().lower())
            elif self.m_choice1.GetSelection() == 1:
                if setting['ChecksumUpper']:
                    self.m_listCtrl1.SetItem(self.m_listCtrl1.GetFocusedItem(), 2,
                                             dlg.get_checksum().upper())
                else:
                    self.m_listCtrl1.SetItem(self.m_listCtrl1.GetFocusedItem(), 2,
                                             dlg.get_checksum().lower())
                self.m_listCtrl1.SetItem(self.m_listCtrl1.GetFocusedItem(), 3, '')
                self.m_listCtrl1.SetItemBackgroundColour(self.m_listCtrl1.GetFocusedItem(), wx.Colour(-1, -1, -1))
        dlg.Destroy()

    def copy_file_address( self, event ):
        if self.m_choice1.GetSelection() == 0:
            pyperclip.copy(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 2))
        elif self.m_choice1.GetSelection() == 1:
            pyperclip.copy(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 1))

    def copy_checksum( self, event ):
        if self.m_choice1.GetSelection() == 0:
            pyperclip.copy(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 3))
        elif self.m_choice1.GetSelection() == 1:
            pyperclip.copy(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 2))

    def delete_item( self, event ):
        del self.informations[int(self.m_listCtrl1.GetItemText(self.m_listCtrl1.GetFocusedItem(), 0)) - 1]
        self.m_listCtrl1.DeleteItem(self.m_listCtrl1.GetFocusedItem())
        listitems = []
        for i in range(0, self.m_listCtrl1.GetItemCount()):
            if self.m_listCtrl1.GetItemText(i, 1) == '' and self.m_choice1.GetSelection() == 0:
                listitems.append([int(self.m_listCtrl1.GetItemText(i, 0)), -1,
                                  self.m_listCtrl1.GetItemText(i, 2), self.m_listCtrl1.GetItemText(i, 3)])
            else:
                if self.m_choice1.GetSelection() == 0:
                    listitems.append([int(self.m_listCtrl1.GetItemText(i, 0)), int(self.m_listCtrl1.GetItemText(i, 1)),
                                      self.m_listCtrl1.GetItemText(i, 2), self.m_listCtrl1.GetItemText(i, 3)])
                elif self.m_choice1.GetSelection() == 1:
                    listitems.append([int(self.m_listCtrl1.GetItemText(i, 0)), self.m_listCtrl1.GetItemText(i, 1),
                                      self.m_listCtrl1.GetItemText(i, 2), self.m_listCtrl1.GetItemText(i, 3)])
        listitems = sorted(listitems, key=lambda x: x[0],
                           reverse=False)
        for i in range(0, self.m_listCtrl1.GetItemCount()):
            listitems[i][0] = i + 1
        if self.m_listCtrl1.GetSortIndicator() != -1:
            listitems = sorted(listitems, key=lambda x: x[self.m_listCtrl1.GetSortIndicator()],
                               reverse=not self.m_listCtrl1.IsAscendingSortIndicator())
        if self.m_choice1.GetSelection() == 0:
            for i in range(0, len(listitems)):
                self.m_listCtrl1.SetItem(i, 0, str(listitems[i][0]))
                if listitems[i][1] == -1:
                    self.m_listCtrl1.SetItem(i, 1, '')
                else:
                    self.m_listCtrl1.SetItem(i, 1, str(listitems[i][1]))
                self.m_listCtrl1.SetItem(i, 2, listitems[i][2])
                self.m_listCtrl1.SetItem(i, 3, listitems[i][3])
        elif self.m_choice1.GetSelection() == 1:
            for i in range(0, len(listitems)):
                self.m_listCtrl1.SetItem(i, 0, str(listitems[i][0]))
                if listitems[i][3] == -1:
                    self.m_listCtrl1.SetItem(i, 3, '')
                    self.m_listCtrl1.SetItemBackgroundColour(i, wx.Colour(-1, -1, -1))
                elif listitems[i][3] == -2:
                    self.m_listCtrl1.SetItem(i, 3, Lang.str_error())
                    self.m_listCtrl1.SetItemBackgroundColour(i, wx.Colour(255, 235, 156))  # Yellow
                else:
                    self.m_listCtrl1.SetItem(i, 3, str(listitems[i][3]))
                    if str(listitems[i][3]) == '1':
                        self.m_listCtrl1.SetItemBackgroundColour(i, wx.Colour(198, 239, 206))  # Green
                    elif str(listitems[i][3]) == '0':
                        self.m_listCtrl1.SetItemBackgroundColour(i, wx.Colour(255, 199, 206))  # Red
                self.m_listCtrl1.SetItem(i, 1, listitems[i][1])
                self.m_listCtrl1.SetItem(i, 2, listitems[i][2])

    def MainOnContextMenu( self, event ):
        self.PopupMenu( self.m_menu3, event.GetPosition() )

    def setsort(self, event):
        if self.m_listCtrl1.GetSortIndicator() == -1 or self.m_listCtrl1.GetSortIndicator() != event.GetColumn():
            self.m_listCtrl1.ShowSortIndicator(event.GetColumn(), True)
        else:
            self.m_listCtrl1.ShowSortIndicator(event.GetColumn(), not self.m_listCtrl1.IsAscendingSortIndicator())
        self.sort(None)

    def sort(self, event):
        listitems = []
        if self.m_listCtrl1.GetSortIndicator() != -1:
            if self.m_choice1.GetSelection() == 0:
                for i in range(0, self.m_listCtrl1.GetItemCount()):
                    if self.m_listCtrl1.GetItemText(i, 1) == '':
                        listitems.append([int(self.m_listCtrl1.GetItemText(i, 0)), -1,
                                          self.m_listCtrl1.GetItemText(i, 2), self.m_listCtrl1.GetItemText(i, 3)])
                    else:
                        listitems.append(
                            [int(self.m_listCtrl1.GetItemText(i, 0)), int(self.m_listCtrl1.GetItemText(i, 1)),
                             self.m_listCtrl1.GetItemText(i, 2), self.m_listCtrl1.GetItemText(i, 3)])
                listitems = sorted(listitems, key=lambda x: x[self.m_listCtrl1.GetSortIndicator()],
                                   reverse=not self.m_listCtrl1.IsAscendingSortIndicator())
                for i in range(0, len(listitems)):
                    self.m_listCtrl1.SetItem(i, 0, str(listitems[i][0]))
                    if listitems[i][1] == -1:
                        self.m_listCtrl1.SetItem(i, 1, '')
                    else:
                        self.m_listCtrl1.SetItem(i, 1, str(listitems[i][1]))
                    self.m_listCtrl1.SetItem(i, 2, listitems[i][2])
                    self.m_listCtrl1.SetItem(i, 3, listitems[i][3])
            elif self.m_choice1.GetSelection() == 1:
                for i in range(0, self.m_listCtrl1.GetItemCount()):
                    if self.m_listCtrl1.GetItemText(i, 3) == '':
                        listitems.append(
                            [int(self.m_listCtrl1.GetItemText(i, 0)), self.m_listCtrl1.GetItemText(i, 1),
                             self.m_listCtrl1.GetItemText(i, 2), -1])
                    elif self.m_listCtrl1.GetItemText(i, 3) == Lang.str_error():
                        listitems.append(
                            [int(self.m_listCtrl1.GetItemText(i, 0)), self.m_listCtrl1.GetItemText(i, 1),
                             self.m_listCtrl1.GetItemText(i, 2), -2])
                    else:
                        listitems.append([int(self.m_listCtrl1.GetItemText(i, 0)), self.m_listCtrl1.GetItemText(i, 1),
                                          self.m_listCtrl1.GetItemText(i, 2), int(self.m_listCtrl1.GetItemText(i, 3))])
                listitems = sorted(listitems, key=lambda x: x[self.m_listCtrl1.GetSortIndicator()],
                                   reverse=not self.m_listCtrl1.IsAscendingSortIndicator())
                for i in range(0, len(listitems)):
                    self.m_listCtrl1.SetItem(i, 0, str(listitems[i][0]))
                    if listitems[i][3] == -1:
                        self.m_listCtrl1.SetItem(i, 3, '')
                        self.m_listCtrl1.SetItemBackgroundColour(i, wx.Colour(-1, -1, -1))
                    elif listitems[i][3] == -2:
                        self.m_listCtrl1.SetItem(i, 3, Lang.str_error())
                        self.m_listCtrl1.SetItemBackgroundColour(i, wx.Colour(255, 235, 156))  # Yellow
                    else:
                        self.m_listCtrl1.SetItem(i, 3, str(listitems[i][3]))
                        if str(listitems[i][3]) == '1':
                            self.m_listCtrl1.SetItemBackgroundColour(i, wx.Colour(198, 239, 206))  # Green
                        elif str(listitems[i][3]) == '0':
                            self.m_listCtrl1.SetItemBackgroundColour(i, wx.Colour(255, 199, 206))  # Red
                    self.m_listCtrl1.SetItem(i, 1, listitems[i][1])
                    self.m_listCtrl1.SetItem(i, 2, listitems[i][2])


class Settings(UI.Settings):
    def __init__(self, parent):
        UI.Settings.__init__(self, parent)
        self.SetSize(GetScaledSize(self.GetDPI(), self.GetSize()))
        self.Centre()
        self.m_sdbSizer1Apply.Enable(False)
        if platform.system() == 'Windows':
            self.m_listbook1.GetListView().SetColumnWidth(0, GetScaledWidth(self.GetDPI(), 80))
        if platform.system() != 'Windows':
            self.m_radioBtn1.Show(False)
            self.m_radioBtn2.Show(False)
            self.m_radioBtn3.Show(False)
            self.m_radioBtn4.Show(False)
            self.m_scrolledWindow1.Layout()
        self.encoding_choices = encodingchoices
        self.m_choice4.SetItems(self.encoding_choices)
        self.m_choice5.SetItems(self.encoding_choices)
        self.m_choice3.SetSelection(setting['DefaultCheckMode'])
        self.m_checkBox2.SetValue(setting['ChecksumUpper'])
        if setting['SaveTaskEncoding'] not in self.encoding_choices:
            setting['SaveTaskEncoding'] = str(find_encoding_key(str(setting['SaveTaskEncoding'])))
            SaveSetting(setting)
        self.m_checkBox3.SetValue(setting['CompatibleWithOldTask'])
        if setting['ExportResultEncoding'] not in self.encoding_choices:
            setting['ExportResultEncoding'] = str(find_encoding_key(str(setting['ExportResultEncoding'])))
            SaveSetting(setting)
        self.m_choice4.SetSelection(self.encoding_choices.index(setting['SaveTaskEncoding']))
        self.m_choice5.SetSelection(self.encoding_choices.index(setting['ExportResultEncoding']))
        self.m_textCtrl1.SetValue(frame.aftercmd)
        self.run_command_edited(None, False)
        self.m_textCtrl4.SetValue(frame.aftersave)
        self.m_textCtrl4.SetMinSize(GetScaledSize(self.GetDPI(), wx.Size(425, -1)))
        self.Layout()
        self.m_checkBox1.SetValue(bool(self.m_textCtrl4.GetValue()))
        self.ascr_check(None, False)
        self.m_listBox1.SetItems([Lang.settingdlg_language_auto()])
        self.m_listBox1.AppendItems(list(languagelist.values()))
        if setting['Language'] == 'Auto':
            self.m_listBox1.SetSelection(0)
        else:
            self.m_listBox1.SetSelection(self.m_listBox1.FindString(
                languagelist[os.path.join(GetProgPath(), 'Languages', str(setting['Language']))]))
        if frame.change_lang_later_warn:
            self.m_infoCtrl1.ShowMessage(Lang.settingdlg_warning_changelang_later(frame.change_lang_later_warn),
                                         wx.ICON_INFORMATION)

        self.change_lang()

        self.m_textCtrl1.Bind(wx.EVT_TEXT, self.run_command_edited)
        self.m_choice3.Bind(wx.EVT_CHOICE, self.setchanged)
        self.m_checkBox2.Bind(wx.EVT_CHECKBOX, self.setchanged)
        self.m_choice4.Bind(wx.EVT_CHOICE, self.setchanged)
        self.m_checkBox3.Bind(wx.EVT_CHECKBOX, self.setchanged)
        self.m_choice5.Bind(wx.EVT_CHOICE, self.setchanged)
        self.m_listBox1.Bind(wx.EVT_LISTBOX, self.setchanged)

    def change_lang(self):
        self.SetTitle(Lang.settingdlg_title())
        self.sbSizer1.GetStaticBox().SetLabel(Lang.settingdlg_staticbox_starting())
        self.m_staticText1.SetLabel(Lang.settingdlg_default_checkmode())
        self.m_choice3.SetString(0, Lang.choice_mode1())
        self.m_choice3.SetString(1, Lang.choice_mode2())
        self.m_choice3.SetSize(self.m_choice3.GetBestSize())
        self.sbSizer1.Layout()
        self.sbSizer2.GetStaticBox().SetLabel(Lang.settingdlg_operation_after_completion())
        self.m_staticText2.SetLabel(Lang.settingdlg_oac_run_command())
        self.m_radioBtn1.SetLabel(Lang.settingdlg_oac_run_command_none())
        self.m_radioBtn1.SetSize(self.m_radioBtn1.GetBestSize())
        self.m_radioBtn2.SetLabel(Lang.settingdlg_oac_run_command_shutdown())
        self.m_radioBtn2.SetSize(self.m_radioBtn2.GetBestSize())
        self.m_radioBtn3.SetLabel(Lang.settingdlg_oac_run_command_reboot())
        self.m_radioBtn3.SetSize(self.m_radioBtn3.GetBestSize())
        self.m_radioBtn4.SetLabel(Lang.settingdlg_oac_run_command_custom())
        self.m_radioBtn4.SetSize(self.m_radioBtn4.GetBestSize())
        self.sbSizer3.GetStaticBox().SetLabel(Lang.settingdlg_staticbox_ascr())
        self.m_checkBox1.SetLabel(Lang.settingdlg_checkbox_ascr())
        self.m_checkBox1.SetSize(self.m_checkBox1.GetBestSize())
        self.sbSizer4.GetStaticBox().SetLabel(Lang.settingdlg_staticbox_other())
        self.m_checkBox2.SetLabel(Lang.settingdlg_other_uppercase())
        self.m_checkBox2.SetSize(self.m_checkBox2.GetBestSize())
        self.m_listbook1.SetPageText(0, Lang.settingdlg_page_routine())
        self.sbSizer5.GetStaticBox().SetLabel(Lang.settingdlg_staticbox_tasklist())
        self.m_staticText3.SetLabel(Lang.settingdlg_tasklist_encoding())
        self.m_checkBox3.SetLabel(Lang.settingdlg_checkbox_cwov())
        self.m_checkBox3.SetSize(self.m_checkBox3.GetBestSize())
        self.sbSizer6.GetStaticBox().SetLabel(Lang.settingdlg_staticbox_checkresult())
        self.m_staticText4.SetLabel(Lang.settingdlg_checkresult_encoding())
        self.m_button4.SetLabel(Lang.settingdlg_btn_restore())
        self.m_button4.SetSize(self.m_button4.GetBestSize())
        self.m_scrolledWindow2.Layout()
        self.m_listbook1.SetPageText(1, Lang.settingdlg_page_files())
        self.sbSizer7.GetStaticBox().SetLabel(Lang.settingdlg_staticbox_language_setting())
        self.m_listBox1.SetString(0, Lang.settingdlg_language_auto())
        self.m_listbook1.SetPageText(2, Lang.settingdlg_page_language())
        self.m_sdbSizer1OK.SetLabel(Lang.dlg_btn_ok())
        self.m_sdbSizer1OK.SetSize(self.m_sdbSizer1OK.GetBestSize())
        self.m_sdbSizer1Cancel.SetLabel(Lang.dlg_btn_cancel())
        self.m_sdbSizer1Cancel.SetSize(self.m_sdbSizer1Cancel.GetBestSize())
        self.m_sdbSizer1Apply.SetLabel(Lang.dlg_btn_apply())
        self.m_sdbSizer1Apply.SetSize(self.m_sdbSizer1Apply.GetBestSize())
        self.m_scrolledWindow1.Layout()
        self.m_scrolledWindow2.Layout()
        self.m_scrolledWindow3.Layout()
        self.Layout()

    def setchanged(self, event):
        self.m_sdbSizer1Apply.Enable(True)
    def apply( self, event ):
        ApplyOK = True
        if self.m_listBox1.GetSelection() != 0:
            tf = setting['Language'] != os.path.basename(languagelist1[list(languagelist.values()).index(self.m_listBox1.GetString(self.m_listBox1.GetSelection()))])
        else:
            tf = setting['Language'] != 'Auto'
        if tf:
            tf = True
            if frame.m_listCtrl1.GetItemCount():
                toastone = wx.MessageDialog(None, Lang.settingdlg_warning_changelang(), Lang.title(),
                                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)
                toastone.SetYesNoLabels(Lang.dlg_btn_yes(), Lang.dlg_btn_no())
                a = toastone.ShowModal()
                if a == wx.ID_YES:
                    tf = True
                    frame.change_lang_later_warn = None
                    self.m_infoCtrl1.Dismiss()
                    toastone.Destroy()
                elif a == wx.ID_NO:
                    tf = False
                    if self.m_listBox1.GetSelection() == 0:
                        frame.change_lang_later_warn = Lang.settingdlg_language_auto()
                    else:
                        frame.change_lang_later_warn = self.m_listBox1.GetString(self.m_listBox1.GetSelection())
                    self.m_infoCtrl1.ShowMessage(Lang.settingdlg_warning_changelang_later(frame.change_lang_later_warn),
                                                 wx.ICON_INFORMATION)
                    toastone.Destroy()
            if tf:
                spec = None
                lang = None
                if self.m_listBox1.GetSelection() == 0 and locale in languagedic.keys():
                    newlanguage = languagedic[locale]
                elif self.m_listBox1.GetSelection() == 0 and locale not in languagedic.keys():
                    newlanguage = ''
                else:
                    newlanguage = os.path.basename(
                        languagelist1[
                            list(languagelist.values()).index(self.m_listBox1.GetString(self.m_listBox1.GetSelection()))])
                if self.m_listBox1.GetSelection() == 0 and locale in languagedic.keys():
                    spec = importlib.util.spec_from_file_location(str(os.path.basename(languagedic[locale])),
                                                                  languagedic[locale])
                elif (self.m_listBox1.GetSelection() == 0 and locale not in languagedic.keys()) or os.path.join(
                    GetProgPath(), 'Languages', newlanguage) not in languagelist1:
                    toastone = wx.MessageDialog(None, Lang.settingdlg_language_error_notinstalled(),
                                                Lang.title(),
                                                wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                    toastone.SetOKLabel(Lang.dlg_btn_ok())
                    if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                        toastone.Destroy()
                        ApplyOK = False
                else:
                    if Verify_Signature(os.path.join(GetProgPath(), 'Languages', str(newlanguage)),
                                        os.path.join(GetProgPath(), 'Languages', str(newlanguage)) + '.sig') or (
                            '/DEBUG:DisableLangSign' in sys.argv[1:] and not (
                            getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'))):
                        spec = importlib.util.spec_from_file_location(str(newlanguage),
                                                                      os.path.join(GetProgPath(), 'Languages',
                                                                                   str(newlanguage)))
                    else:
                        toastone = wx.MessageDialog(None, Lang.settingdlg_language_error_signature_failure(),
                                                    Lang.title(),
                                                    wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                        toastone.SetOKLabel(Lang.dlg_btn_ok())
                        if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                            toastone.Destroy()
                            ApplyOK = False
                if spec is not None:
                    lang = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(lang)
                    Lang.ChangeLang(lang)
                    frame.change_lang()
                    if '/DEBUG:ForceEnableUpdate' in sys.argv[1:] or not os.path.basename(sys.argv[0]).split('.')[
                        -1].lower().startswith('py'):
                        otadlg.change_lang()
                        if otadlg.status == 0:
                            otadlg.update(otadlg, usecache=True)
                    self.change_lang()
                else:
                    toastone = wx.MessageDialog(None, Lang.settingdlg_language_error_failure(),
                                                Lang.title(),
                                                wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                    toastone.SetOKLabel(Lang.dlg_btn_ok())
                    if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                        toastone.Destroy()
                        ApplyOK = False
        if ApplyOK:
            if self.m_checkBox1.GetValue() and self.m_textCtrl4.GetValue() == '':
                toastone = wx.MessageDialog(None, Lang.settingdlg_error_ascr_invaild(),
                                            Lang.title(),
                                            wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                toastone.SetOKLabel(Lang.dlg_btn_ok())
                if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                    toastone.Destroy()
                    ApplyOK = False
        if ApplyOK:
            if self.m_listBox1.GetSelection() == 0:
                setting['Language'] = 'Auto'
            else:
                setting['Language'] = os.path.basename(languagelist1[list(languagelist.values()).index(
                    self.m_listBox1.GetString(self.m_listBox1.GetSelection()))])
            setting['SaveTaskEncoding'] = self.m_choice4.GetString(self.m_choice4.GetSelection())
            setting['ExportResultEncoding'] = self.m_choice5.GetString(self.m_choice5.GetSelection())
            setting['DefaultCheckMode'] = self.m_choice3.GetSelection()
            setting['ChecksumUpper'] = int(self.m_checkBox2.GetValue())
            for i in range(0, frame.m_listCtrl1.GetItemCount()):
                if setting['ChecksumUpper']:
                    if frame.m_choice1.GetSelection() == 0:
                        frame.m_listCtrl1.SetItem(i, 3, frame.m_listCtrl1.GetItemText(i, 3).upper())
                    elif frame.m_choice1.GetSelection() == 1:
                        frame.m_listCtrl1.SetItem(i, 2, frame.m_listCtrl1.GetItemText(i, 2).upper())
                else:
                    if frame.m_choice1.GetSelection() == 0:
                        frame.m_listCtrl1.SetItem(i, 3, frame.m_listCtrl1.GetItemText(i, 3).lower())
                    elif frame.m_choice1.GetSelection() == 1:
                        frame.m_listCtrl1.SetItem(i, 2, frame.m_listCtrl1.GetItemText(i, 2).lower())
            setting['CompatibleWithOldTask'] = int(self.m_checkBox3.GetValue())
            frame.aftercmd = self.m_textCtrl1.GetValue()
            if self.m_checkBox1.GetValue():
                frame.aftersave = self.m_textCtrl4.GetValue()
            else:
                frame.aftersave = ''
            SaveSetting(setting)
            self.m_sdbSizer1Apply.Enable(False)
    def close(self, event):
        if self.m_sdbSizer1Apply.IsEnabled():
            toastone = wx.MessageDialog(None, Lang.settingdlg_warning_save(), Lang.title(),
                                        wx.YES_NO | wx.CANCEL| wx.NO_DEFAULT | wx.ICON_WARNING)
            toastone.SetYesNoLabels(Lang.dlg_btn_yes(), Lang.dlg_btn_no())
            toastone.SetOKCancelLabels(Lang.dlg_btn_ok(), Lang.dlg_btn_cancel())
            a = toastone.ShowModal()
            if a == wx.ID_YES:
                self.apply(None)
                toastone.Destroy()
                self.EndModal(wx.ID_OK)
            elif a == wx.ID_NO:
                toastone.Destroy()
                self.EndModal(wx.ID_CANCEL)
            elif a == wx.ID_CANCEL:
                toastone.Destroy()
        else:
            self.EndModal(wx.ID_CANCEL)
    def ascr_check( self, event, mode=True ):
        if mode:
            self.setchanged(None)
        self.m_textCtrl4.Enable(self.m_checkBox1.IsChecked())
        self.m_button6.Enable(self.m_checkBox1.IsChecked())
    def getascrpath( self, event ):
        dlg = wx.FileDialog(self, message=Lang.settingdlg_ascr_pathpicker_title(),
                            defaultDir='',
                            defaultFile='',
                            wildcard=Lang.settingdlg_ascr_pathpicker_wildcards(),
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl4.SetValue(dlg.GetPath())
            dlg.Destroy()
    def run_command_choice_none( self, event ):
        self.m_textCtrl1.SetValue('')
    def run_command_choice_shutdown( self, event ):
        self.m_textCtrl1.SetValue('shutdown -s -t 0')
    def run_command_choice_reboot( self, event ):
        self.m_textCtrl1.SetValue('shutdown -r -t 0')
    def run_command_edited( self, event, mode=True ):
        if mode:
            self.setchanged(None)
        if self.m_textCtrl1.GetValue() == '':
            self.m_radioBtn1.SetValue(True)
        elif self.m_textCtrl1.GetValue() == 'shutdown -s -t 0':
            self.m_radioBtn2.SetValue(True)
        elif self.m_textCtrl1.GetValue() == 'shutdown -r -t 0':
            self.m_radioBtn3.SetValue(True)
        else:
            self.m_radioBtn4.SetValue(True)
    def files_setting_restore( self, event ):
        self.m_choice4.SetSelection(self.encoding_choices.index('UTF_8'))
        self.m_checkBox3.SetValue(False)
        if platform.system() == 'Windows':
            self.m_choice5.SetSelection(self.encoding_choices.index('ANSI'))
        else:
            self.m_choice5.SetSelection(self.encoding_choices.index('UTF_8'))
        self.setchanged(None)


class ChecksumDialog(UI.ChecksumDialog):
    def __init__(self, parent=None):
        UI.ChecksumDialog.__init__(self, parent)
        self.SetSize(GetScaledSize(self.GetDPI(), self.GetSize()))
        self.Centre()
        self.mode = False
        self.change_lang()
        self.m_textCtrl2.SetMinSize(self.m_textCtrl2.GetSize())
        self.Fit()
        self.Bind(wx.EVT_CLOSE, self.close)
        self.m_textCtrl2.Bind(wx.EVT_TEXT_ENTER, self.ok)

    def change_lang(self):
        self.set_mode(self.mode)
        self.gettype(None)
        self.m_sdbSizer2OK.SetLabel(Lang.dlg_btn_ok())

    def close(self, event):
        self.EndModal(wx.ID_CANCEL)

    def ok(self, event):
        self.EndModal(wx.ID_OK)

    def set_mode(self, mode=False):
        self.mode = mode
        if mode:
            self.SetTitle(Lang.checksumdlg_title_edit())
        else:
            self.SetTitle(Lang.checksumdlg_title_add())

    def gettype( self, event ):
        if len(list(self.m_textCtrl2.GetValue())) == 8:
            self.m_staticText5.SetLabelText(Lang.checksumdlg_checksum_type(['CRC-32']))
        elif len(list(self.m_textCtrl2.GetValue())) == 32:
            self.m_staticText5.SetLabelText(Lang.checksumdlg_checksum_type(['MD5']))
        elif len(list(self.m_textCtrl2.GetValue())) == 40:
            self.m_staticText5.SetLabelText(Lang.checksumdlg_checksum_type(['SHA-1']))
        elif len(list(self.m_textCtrl2.GetValue())) == 56:
            self.m_staticText5.SetLabelText(Lang.checksumdlg_checksum_type(['SHA-224', 'SHA3-224']))
        elif len(list(self.m_textCtrl2.GetValue())) == 64:
            self.m_staticText5.SetLabelText(Lang.checksumdlg_checksum_type(['SHA-256', 'SHA3-256', 'BLAKE2s']))
        elif len(list(self.m_textCtrl2.GetValue())) == 96:
            self.m_staticText5.SetLabelText(Lang.checksumdlg_checksum_type(['SHA-384', 'SHA3-384']))
        elif len(list(self.m_textCtrl2.GetValue())) == 128:
            self.m_staticText5.SetLabelText(Lang.checksumdlg_checksum_type(['SHA-512', 'SHA3-512', 'BLAKE2b']))
        else:
            self.m_staticText5.SetLabelText(Lang.checksumdlg_checksum_type([]))

    def set_checksum(self, checksum):
        self.m_textCtrl2.SetValue(checksum)
        self.gettype(None)
    def get_checksum(self):
        return self.m_textCtrl2.GetValue()


class About(UI.About):
    def __init__(self, parent=None):
        UI.About.__init__(self, parent)
        self.SetSize(GetScaledSize(self.GetDPI(), self.GetSize()))
        self.m_customControl1.SetMinSize(GetScaledSize(self.GetDPI(), self.m_customControl1.GetSize()))
        self.Layout()
        self.Centre()
        self.m_customControl1.SetScaleMode(2)
        self.change_lang()

    def change_lang(self):
        self.SetTitle(Lang.aboutdlg_title())
        self.m_staticText6.SetLabel(Lang.aboutdlg_software_name(arch))
        self.m_staticText7.SetLabel(Lang.aboutdlg_version(Version))
        self.m_staticText8.SetLabel(Lang.aboutdlg_build(Build))
        self.m_richText1.Clear()
        self.m_richText1.AppendText(Lang.aboutdlg_pyver(sys.version.partition(' ')[0]))
        self.m_richText1.AppendText('\n')
        self.m_richText1.AppendText(Lang.aboutdlg_wxpyver(wx.version().partition(' ')[0]))
        self.m_richText1.AppendText('\n\n')
        self.m_richText1.AppendText(Lang.aboutdlg_language())
        self.m_richText1.AppendText('\n\n')
        self.m_richText1.AppendText(Lang.aboutdlg_open_source_declaration('Apache-2.0'))


class Calculation(UI.Calculation):
    def __init__(self, parent=None):
        UI.Calculation.__init__(self, parent)
        self.SetSize(GetScaledSize(self.GetDPI(), self.GetSize()))
        if platform.system() == 'Windows':
            self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        self.Centre()
        self.change_lang()

    def change_lang(self):
        self.SetTitle(Lang.calcdlg_title())
        self.m_staticText10.SetLabel(Lang.calcdlg_elapsed_time())
        self.m_staticText12.SetLabel(Lang.calcdlg_file())
        self.m_staticText14.SetLabel(Lang.calcdlg_size())
        self.m_staticText16.SetLabel(Lang.calcdlg_speed())
        self.m_staticText18.SetLabel(Lang.calcdlg_progress())
        self.m_staticText19.SetLabel(Lang.calcdlg_overall_progress())
        self.m_sdbSizer3OK.SetLabel(Lang.calcdlg_btn_pause())
        self.m_sdbSizer3Cancel.SetLabel(Lang.dlg_btn_cancel())

    def intformat(self, int):
        l = list(str(int))
        for i in range(0, len(l) // 3):
            if len(l) + 1 - (i + 1) * 4 != 0:
                l.insert(len(l) + 1 - (i + 1) * 4, ',')
        string = ''
        for i in l:
            string = string + i
        return string
    def sizeformat(self, size, speedmode=False):
        if not speedmode:
            if size >= 1099511627776:  # 1TB
                return str('%.2f' % (size / 1099511627776)) + ' TB (' + self.intformat(
                    size) + ' ' + Lang.calcdlg_str_bytes() + ')'
            elif size >= 1073741824:  # 1GB
                return str('%.2f' % (size / 1073741824)) + ' GB (' + self.intformat(
                    size) + ' ' + Lang.calcdlg_str_bytes() + ')'
            elif size >= 1048576:  # 1MB
                return str('%.2f' % (size / 1048576)) + ' MB (' + self.intformat(size) + ' ' + Lang.calcdlg_str_bytes() + ')'
            elif size >= 1024:  # 1KB
                return str('%.2f' % (size / 1024)) + ' KB (' + self.intformat(size) + ' ' + Lang.calcdlg_str_bytes() + ')'
            else:
                return str(self.intformat(size)) + ' ' + Lang.calcdlg_str_bytes()
        else:
            if size >= 1099511627776:  # 1TB
                return str('%.2f' % (size / 1099511627776)) + ' TB/s'
            elif size >= 1073741824:  # 1GB
                return str('%.2f' % (size / 1073741824)) + ' GB/s'
            elif size >= 1048576:  # 1MB
                return str('%.2f' % (size / 1048576)) + ' MB/s'
            elif size >= 1024:  # 1KB
                return str('%.2f' % (size / 1024)) + ' KB/s'
            else:
                return str(size) + ' B/s'

    def update(self, count, time, file, size, speed, progress, overall_progress):
        if not count == (None, None) or count is None:
            self.SetTitle(Lang.calcdlg_title(count))
        if time:
            self.m_staticText11.SetLabel(timeformat(time))
        if file:
            self.m_staticText13.SetLabel(file)
        if size:
            self.m_staticText15.SetLabel(self.sizeformat(size))
        if speed:
            self.m_staticText17.SetLabel(speed)
        if progress:
            self.m_gauge1.SetValue(int('%.0f' % (progress * 100)))
        if overall_progress:
            self.m_gauge2.SetValue(int('%.0f' % (overall_progress * 100)))

    def pause(self, event):
        if frame.ispause:
            frame.ispause = False
            self.m_sdbSizer3OK.SetLabel(Lang.calcdlg_btn_pause())
        else:
            frame.ispause = True
            self.m_sdbSizer3OK.SetLabel(Lang.calcdlg_btn_continue())

    def cancel(self, event):
        toastone = wx.MessageDialog(None, Lang.calcdlg_warning_cancel(), Lang.title(),
                                    wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)
        toastone.SetYesNoLabels(Lang.dlg_btn_yes(), Lang.dlg_btn_no())
        if toastone.ShowModal() == wx.ID_YES:  # 如果点击了提示框的确定按钮
            toastone.Destroy()
            frame.iscancel = True


class EncodingPicker(UI.EncodingPicker):
    def __init__(self, parent=None):
        UI.EncodingPicker.__init__(self, parent)
        self.SetSize(GetScaledSize(self.GetDPI(), self.GetSize()))
        self.Centre()
        self.change_lang()
        self.file = ''
        self.m_listBox2.SetItems(encodingchoices)
        self.m_listBox2.SetSelection(self.m_listBox2.GetItems().index('UTF_8'))


    def change_lang(self):
        self.SetTitle(Lang.encodingpickerdlg_title())
        self.m_staticText20.SetLabel(Lang.encodingpickerdlg_hint())
        self.m_sdbSizer4OK.SetLabel(Lang.dlg_btn_ok())
        self.m_sdbSizer4Cancel.SetLabel(Lang.dlg_btn_cancel())

    def set_file(self, file):
        self.file = file
        self.SetTitle(Lang.encodingpickerdlg_title(file))
        self.update_preview(None)

    def update_preview( self, event ):
        if self.file:
            try:
                with open(self.file, 'r', encoding=self.get_encoding(), errors='replace') as f:
                    self.m_richText2.SetValue(f.read())
                self.m_sdbSizer4OK.Enable(True)
            except Exception as err:
                self.m_sdbSizer4OK.Enable(False)
                self.m_richText2.BeginTextColour(wx.Colour(255, 0, 0))
                self.m_richText2.SetValue('无法读取文件：' + '\n' + type(err).__name__ + ': ' + str(err))
                self.m_richText2.EndTextColour()
        else:
            self.m_richText2.SetValue('')
            self.m_sdbSizer4OK.Enable(False)

    def set_encoding(self, encoding):
        self.m_listBox2.SetSelection(self.m_listBox2.GetItems().index(encoding))
        self.update_preview(None)

    def get_encoding(self):
        return self.m_listBox2.GetString(self.m_listBox2.GetSelection())


class Details(UI.Details):
    def __init__(self, parent=None):
        UI.Details.__init__(self, parent)
        self.SetSize(GetScaledSize(self.GetDPI(), self.GetSize()))
        self.Centre()
        self.change_lang()

    def change_lang(self):
        self.SetTitle(Lang.detailsdlg_title())
        self.m_sdbSizer5OK.SetLabel(Lang.dlg_btn_ok())

    def set_value(self, value):
        self.m_richText3.SetValue(value)


class ItemDialog(UI.ItemDialog):
    def __init__(self, parent=None):
        UI.ItemDialog.__init__(self, parent)
        self.SetSize(GetScaledSize(self.GetDPI(), self.GetSize()))
        self.Centre()
        self.change_lang()
        self.m_textCtrl5.SetMinSize(GetScaledSize(self.GetDPI(), wx.Size(250, -1)))
        self.Fit()
        self.Layout()
        self.m_sdbSizer7OK.Bind(wx.EVT_BUTTON, self.ok)

    def change_lang(self):
        self.SetTitle(Lang.itemdlg_title())
        self.m_staticText25.SetLabel(Lang.itemdlg_file())
        self.m_staticText26.SetLabel(Lang.itemdlg_expected_checksum())
        self.m_staticText27.SetLabel(Lang.itemdlg_checksum_type_title())
        self.gettype(None)
        self.m_sdbSizer7OK.SetLabel(Lang.dlg_btn_ok())
        self.m_sdbSizer7Cancel.SetLabel(Lang.dlg_btn_cancel())
        self.Layout()

    def getpath(self, event):
        dlg = wx.FileDialog(self, message=Lang.filedlg_title_add(),
                            defaultDir='',
                            defaultFile='',
                            wildcard=Lang.filedlg_wildcard_1(),
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl5.SetValue(dlg.GetPath())
            dlg.Destroy()

    def gettype( self, event ):
        if len(list(self.m_textCtrl3.GetValue())) == 8:
            self.m_staticText28.SetLabelText(Lang.itemdlg_checksum_type(['CRC-32']))
        elif len(list(self.m_textCtrl3.GetValue())) == 32:
            self.m_staticText28.SetLabelText(Lang.itemdlg_checksum_type(['MD5']))
        elif len(list(self.m_textCtrl3.GetValue())) == 40:
            self.m_staticText28.SetLabelText(Lang.itemdlg_checksum_type(['SHA-1']))
        elif len(list(self.m_textCtrl3.GetValue())) == 56:
            self.m_staticText28.SetLabelText(Lang.itemdlg_checksum_type(['SHA-224', 'SHA3-224']))
        elif len(list(self.m_textCtrl3.GetValue())) == 64:
            self.m_staticText28.SetLabelText(Lang.itemdlg_checksum_type(['SHA-256', 'SHA3-256', 'BLAKE2s']))
        elif len(list(self.m_textCtrl3.GetValue())) == 96:
            self.m_staticText28.SetLabelText(Lang.itemdlg_checksum_type(['SHA-384', 'SHA3-384']))
        elif len(list(self.m_textCtrl3.GetValue())) == 128:
            self.m_staticText28.SetLabelText(Lang.itemdlg_checksum_type(['SHA-512', 'SHA3-512', 'BLAKE2b']))
        else:
            self.m_staticText28.SetLabelText(Lang.itemdlg_checksum_type([]))

    def ok(self, event):
        if not os.path.isfile(self.m_textCtrl5.GetValue()):
            toastone = wx.MessageDialog(None, Lang.itemdlg_invalid_file_error(self.m_textCtrl5.GetValue()),
                                        Lang.title(),
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
            toastone.SetOKLabel(Lang.dlg_btn_ok())
            if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
        else:
            self.EndModal(wx.ID_OK)

    def set_file(self, file:str):
        self.m_textCtrl5.SetValue(file)

    def get_input(self):
        return [self.m_textCtrl5.GetValue(), self.m_textCtrl3.GetValue()]


class OpenTaskDialog(UI.OpenTaskDialog):
    def __init__(self, parent=None):
        UI.OpenTaskDialog.__init__(self, parent)
        self.SetSize(GetScaledSize(self.GetDPI(), self.GetSize()))
        self.Centre()
        self.change_lang()
        self.Bind(wx.EVT_CLOSE, self.close)

    def change_lang(self):
        self.SetTitle(Lang.opentaskdlg_title())
        self.m_staticText29.SetLabel(Lang.opentaskdlg_hint())
        self.m_button5.SetLabel(Lang.opentaskdlg_loadfile())
        self.m_sdbSizer8OK.SetLabel(Lang.dlg_btn_ok())

    def close(self, event):
        self.EndModal(wx.ID_CANCEL)

    def load(self, event):
        dlg = wx.FileDialog(self, message=Lang.filedlg_title_opentask(),
                            defaultDir='',
                            defaultFile='',
                            wildcard=Lang.opentaskdlg_loadfile_wildcard(),
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            file = dlg.GetPath()
            dlg.Destroy()
            encodingpick = EncodingPicker(self)
            encodingpick.set_file(file)
            encodingpick.set_encoding('UTF_8')
            if encodingpick.ShowModal() == wx.ID_OK:
                with open(file, 'r', encoding=encodingpick.get_encoding(), errors='replace') as f:
                    self.m_richText4.SetValue(f.read())

    def get_input(self):
        return self.m_richText4.GetValue()

class OTA(UI.OTA):
    def __init__(self, parent=None):
        UI.OTA.__init__(self, parent)
        self.SetSize(GetScaledSize(self.GetDPI(), self.GetSize()))
        self.m_customControl2.SetMinSize(GetScaledSize(self.GetDPI(), self.m_customControl2.GetSize()))
        self.Layout()
        self.Centre()
        self.m_customControl2.SetScaleMode(2)
        self.change_lang()
        self.retry = 0
        self.status = 0
        self.current_version = {'link': {}}
        if platform.system() == 'Windows' and arch == 'AMD64':
            self.current_json = 'CurrentVersion_v2.json'
        elif platform.system() == 'Windows' and arch == 'ARM64':
            self.current_json = 'CurrentVersion_wina64.json'
        elif platform.system() == 'Darwin' and arch == 'arm64':
            self.current_json = 'CurrentVersion_macosa64.json'
        else:
            self.current_json = 'None'
        self.update(self, usecache=True)

        self.Bind(wx.EVT_CLOSE, self.close)
        self.m_sdbSizer6Cancel.Bind(wx.EVT_BUTTON, self.close)
        self.m_htmlWin1.Bind(wx.html.EVT_HTML_LINK_CLICKED, self.link)
        self.m_sdbSizer6OK.Bind(wx.EVT_BUTTON, self.update)

    def change_lang(self):
        self.SetTitle(Lang.otadlg_title())
        self.m_staticText22.SetLabel(Lang.otadlg_software_name(arch))
        self.m_staticText23.SetLabel(Lang.otadlg_current_ver(Version))
        self.m_staticText24.SetLabel(Lang.otadlg_lastest_ver(None))
        self.m_sdbSizer6OK.SetLabel(Lang.otadlg_btn_check())
        self.m_sdbSizer6Cancel.SetLabel(Lang.dlg_btn_cancel())

    def close(self, event):
        if self.m_sdbSizer6Cancel.IsEnabled():
            frame.Enable(True)
            self.Show(False)

    def link(self, event):
        if platform.system() == 'Windows':
            os.startfile(event.GetLinkInfo().GetHref())
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', event.GetLinkInfo().GetHref()])

    def update(self, event, retry=0, usecache=False):
        if self.m_sdbSizer6OK.GetLabel() == Lang.otadlg_btn_check():
            self.m_htmlWin1.SetPage(markdown.markdown(Lang.otadlg_md_checking()))
            self.m_staticText24.SetLabel(Lang.otadlg_lastest_ver(None))
            self.m_sdbSizer6OK.Enable(False)
            if not retry:
                thread2 = threading.Thread(target=self.download, args=(
                    'check',
                    'https://github.com/ZHJ00000/OTA_Service/releases/download/CurrentVersion/' + self.current_json,
                    os.path.join(GetUserDataPath(), 'FilesChecker4', self.current_json), usecache),
                                           daemon=True)
            else:
                thread2 = threading.Thread(target=self.download, args=(
                    'check',
                    'https://gitee.com/zhj00/OTA_Service/releases/download/FilesChecker/' + self.current_json,
                    os.path.join(GetUserDataPath(), 'FilesChecker4', self.current_json), usecache),
                                           daemon=True)
            thread2.start()
        elif self.m_sdbSizer6OK.GetLabel() == Lang.otadlg_btn_update():
            self.m_staticText30.Show(True)
            self.m_sdbSizer6OK.Enable(False)
            self.m_sdbSizer6Cancel.Enable(False)
            if not os.path.isdir(os.path.join(GetUserDataPath(), 'Updates')):
                os.mkdir(os.path.join(GetUserDataPath(), 'Updates'))
            if str(Version) in self.current_version['link'].keys():
                thread2 = threading.Thread(target=self.download,
                                           args=('download', self.current_version['link'][str(Version)][self.retry + 1],
                                                 os.path.join(GetUserDataPath(), 'Updates', str(os.path.basename(
                                                     self.current_version['link'][str(Version)][self.retry + 1])))),
                                           daemon=True)
            else:
                thread2 = threading.Thread(target=self.download,
                                           args=('download', self.current_version['link']['other'][self.retry + 1],
                                                 os.path.join(GetUserDataPath(), 'Updates', str(os.path.basename(
                                                     self.current_version['link']['other'][self.retry + 1])))),
                                           daemon=True)
            thread2.start()
            self.m_gauge3.Show(True)
            self.Layout()

    def download(self, mode, url, output_path, usecache=None):
        downloaderror = ''
        self.status = 1
        if os.path.isfile(os.path.join(GetUserDataPath(), 'FilesChecker4',
                                       self.current_json)) and mode == 'check' and usecache:
            if datetime.datetime.fromtimestamp(os.path.getmtime(
                    os.path.join(GetUserDataPath(), 'FilesChecker4',
                                 self.current_json))).date() == datetime.datetime.now().date():
                usecache = bool(os.path.getsize(os.path.join(GetUserDataPath(), 'FilesChecker4',
                                                             self.current_json)))
            else:
                usecache = False
        else:
            usecache = False
        if not usecache:
            downloaderror = ''
            if platform.system() == 'Windows':
                process = subprocess.Popen(
                    [os.path.join(GetProgPath(), "curl.exe"), '-f', '-o', output_path, '-L',
                     '--connect-timeout', '10', url],
                    creationflags=subprocess.CREATE_NO_WINDOW, stderr=subprocess.PIPE, universal_newlines=True,
                    bufsize=1)
            elif platform.system() == 'Darwin':
                process = subprocess.Popen(
                    [os.path.join(GetProgPath(), "curl-macos"), '-f', '-o', output_path, '-L',
                     '--connect-timeout', '10', url],
                    stderr=subprocess.PIPE, universal_newlines=True,
                    bufsize=1)
            else:
                process = subprocess.Popen(
                    [os.path.join(GetProgPath(), "curl"), '-f', '-o', output_path, '-L',
                     '--connect-timeout', '10', url],
                    stderr=subprocess.PIPE, universal_newlines=True,
                    bufsize=1)
            if mode == 'download':
                for i in process.stderr:
                    line = i
                    line = line.replace('\n', '')
                    line = line.split(' ')
                    while '' in line:
                        line.remove('')
                    if len(line) > 0 and line[0] == 'curl:':
                        downloaderror = i
                    elif len(line) > 0 and line[-1] == 'Current':
                        wx.CallAfter(self.m_staticText30.SetLabel, Lang.otadlg_connecting())
                    elif len(line) == 12:
                        wx.CallAfter(self.m_staticText30.SetLabel, Lang.otadlg_progress(line[2], line[-1], line[-2]))
                        wx.CallAfter(self.m_gauge3.SetValue, int(line[2]))
                    elif len(line) == 11:
                        wx.CallAfter(self.m_staticText30.SetLabel, Lang.otadlg_progress(line[2], line[-1], '--:--'))
                        wx.CallAfter(self.m_gauge3.SetValue, int(line[2]))
                    else:
                        wx.CallAfter(self.m_staticText30.SetLabel, Lang.otadlg_connecting())
                    time.sleep(0.5)
            else:
                for i in process.stderr:
                    if i.startswith('curl:'):
                        downloaderror = i
                    time.sleep(0.5)

            rc = process.poll()
            if os.path.isfile(output_path):
                os.utime(output_path, (time.time(), time.time()))
        else:
            rc = 0
        if rc == 0 or rc == None:
            if mode == 'check':
                self.retry = 0
                with open(os.path.join(GetUserDataPath(), 'FilesChecker4', self.current_json), 'r',
                          encoding='utf-8') as f:
                    self.current_version = json.loads(f.read())

                def releaseselect(osver):
                    osver = tuple(osver)
                    for i in self.current_version['releases'].keys():
                        if i != 'default':
                            scope = i[1:-1].split(',')
                            scope[0] = list(scope[0].split('.'))
                            if scope[0] != ['-']:
                                for j in range(len(scope[0])):
                                    scope[0][j] = int(scope[0][j])
                            scope[1] = list(scope[1].split('.'))
                            if scope[1] != ['+']:
                                for j in range(len(scope[1])):
                                    scope[1][j] = int(scope[1][j])
                            scope[0] = tuple(scope[0])
                            scope[1] = tuple(scope[1])
                            if i[0] == '(' and i[-1] == ']':
                                if scope[0] == ('-',):
                                    if osver <= scope[1]:
                                        return i
                                else:
                                    if osver <= scope[1] and osver > scope[0]:
                                        return i
                            elif i[0] == '[' and i[-1] == ')':
                                if scope[1] == ('+',):
                                    if osver >= scope[0]:
                                        return i
                                else:
                                    if osver >= scope[0] and osver < scope[1]:
                                        return i
                            elif i[0] == '(' and i[-1] == ')':
                                if scope[0] == ('-',):
                                    if osver < scope[1]:
                                        return i
                                elif scope[1] == ('+',):
                                    if osver > scope[0]:
                                        return i
                                else:
                                    if osver > scope[0] and osver < scope[1]:
                                        return i
                            elif i[0] == '[' and i[-1] == ']':
                                if osver >= scope[0] and osver <= scope[1]:
                                    return i
                    return 'default'

                self.current_version = self.current_version['releases'][releaseselect(GetOSVersion())]

                if tuple(self.current_version['version']) > Version or str(Version) in self.current_version['rollback']:
                    frame.SetStatusText(Lang.ota_hint())
                try:
                    if Lang.LANGUAGE[0] in self.current_version['note'].keys():
                        wx.CallAfter(self.m_htmlWin1.SetPage, markdown.markdown(self.current_version['note'][Lang.LANGUAGE[0]]))
                    else:
                        wx.CallAfter(self.m_htmlWin1.SetPage, markdown.markdown(self.current_version['note']['en_gb']))
                    wx.CallAfter(self.m_staticText24.SetLabel, Lang.otadlg_lastest_ver(self.current_version['version']))
                    if tuple(self.current_version['version']) > Version or str(Version) in self.current_version[
                        'rollback']:
                        wx.CallAfter(self.m_sdbSizer6OK.SetLabel, Lang.otadlg_btn_update())
                        if str(Version) in self.current_version['link'].keys():
                            wx.CallAfter(self.m_staticText30.SetLabel, Lang.otadlg_patch_size(self.current_version['link'][str(Version)][0]))
                        else:
                            wx.CallAfter(self.m_staticText30.SetLabel, Lang.otadlg_full_size(self.current_version['link']['other'][0]))
                        wx.CallAfter(self.m_staticText30.Show, True)
                        self.Layout()

                    else:
                        wx.CallAfter(self.m_sdbSizer6OK.SetLabel, Lang.otadlg_btn_check())
                    wx.CallAfter(self.m_sdbSizer6OK.Enable, True)
                except RuntimeError:
                    pass
            elif mode == 'download':
                def filehash(path, algorithm):
                    size = os.path.getsize(path)  # 获取文件大小，单位是字节（byte）
                    size1 = size
                    with open(path, 'rb') as f:  # 以二进制模式读取文件
                        while size >= 1024 * 1024:  # 当文件大于1MB时将文件分块读取
                            algorithm.update(f.read(1024 * 1024))
                            size -= 1024 * 1024
                            progress = int('%.0f' % ((size1 - size) / size1 * 100))
                            wx.CallAfter(self.m_staticText30.SetLabel, Lang.otadlg_verifying(str(progress)))
                            wx.CallAfter(self.m_gauge3.SetValue, progress)
                        algorithm.update(f.read())
                    return (algorithm.hexdigest())  # 输出计算结果

                tf = False
                checksum = filehash(output_path, hashlib.sha3_256())
                if os.path.basename(output_path) not in self.current_version['checksum'].keys():
                    tf = True
                elif checksum != self.current_version['checksum'][os.path.basename(output_path)]:
                    tf = True
                if tf:
                    toastone = wx.MessageDialog(None, Lang.otadlg_verification_error(),
                                                Lang.title(),
                                                wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
                    toastone.SetOKLabel(Lang.dlg_btn_ok())
                    if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                        toastone.Destroy()
                        wx.CallAfter(self.m_htmlWin1.SetPage, markdown.markdown(Lang.otadlg_md_failure()))
                        wx.CallAfter(self.m_staticText24.SetLabel, Lang.otadlg_lastest_ver(None))
                        wx.CallAfter(self.m_sdbSizer6OK.SetLabel, Lang.otadlg_btn_check())
                        wx.CallAfter(self.m_staticText30.Show, False)
                        wx.CallAfter(self.m_gauge3.Show, False)
                        wx.CallAfter(self.Layout)
                        wx.CallAfter(self.m_sdbSizer6OK.Enable, True)
                        wx.CallAfter(self.m_sdbSizer6Cancel.Enable, True)
                else:
                    wx.CallAfter(self.Destroy)
                    if str(Version) in self.current_version['link'].keys():
                        if platform.system() == 'Windows':
                            subprocess.Popen(output_path + ' /SILENT /PASSWORD=ZR4KZ-7TA56-582Y9-30SAF-0988L')
                        elif platform.system() == 'Darwin':
                            Unzip(output_path, 'ZR4KZ-7TA56-582Y9-30SAF-0988L',
                                  os.path.join(GetUserDataPath(), 'Updates',
                                               datetime.datetime.now().strftime('%Y%m%d')))
                            subprocess.run(['chmod', '+x', os.path.join(GetUserDataPath(), 'Updates',
                                                                        datetime.datetime.now().strftime('%Y%m%d'),
                                                                        'Update')],
                                           check=True)
                            subprocess.Popen(
                                os.path.join(GetUserDataPath(), 'Updates', datetime.datetime.now().strftime('%Y%m%d'),
                                             'Update'))

                    else:
                        if platform.system() == 'Windows':
                            subprocess.Popen(output_path)
                        elif platform.system() == 'Darwin':
                            subprocess.Popen(['open', output_path])
                    wx.CallAfter(frame.Destroy)

        else:
            try:
                if str(Version) in self.current_version['link'].keys():
                    tf = (mode == 'check' and self.retry == 1) or (
                            mode == 'download' and not len(
                        self.current_version['link'][str(Version)]) - 2 - self.retry)
                else:
                    tf = (mode == 'check' and self.retry == 1) or (
                            mode == 'download' and not len(
                        self.current_version['link']['other']) - 2 - self.retry)
                if tf:
                    wx.CallAfter(self.m_htmlWin1.SetPage, markdown.markdown(Lang.otadlg_md_failure() + '\n\n' + downloaderror))
                    wx.CallAfter(self.m_staticText24.SetLabel, Lang.otadlg_lastest_ver(None))
                    wx.CallAfter(self.m_sdbSizer6OK.SetLabel, Lang.otadlg_btn_check())
                    wx.CallAfter(self.m_staticText30.Show, False)
                    wx.CallAfter(self.m_gauge3.Show, False)
                    wx.CallAfter(self.Layout)
                    wx.CallAfter(self.m_sdbSizer6OK.Enable, True)
                    wx.CallAfter(self.m_sdbSizer6Cancel.Enable, True)
                else:
                    self.retry += 1
                    self.update(self, self.retry)
            except RuntimeError:
                pass
        self.status = 0



if __name__ == '__main__':
    LoadOK = True
    if '/Clean' in sys.argv:
        time.sleep(1)
        if os.path.isdir(os.path.join(GetUserDataPath(), 'Updates')):
            shutil.rmtree(os.path.join(GetUserDataPath(), 'Updates'))
    app = wx.App()
    if not os.path.isdir(os.path.join(GetUserDataPath())):
        os.mkdir(os.path.join(GetUserDataPath()))
    if not os.path.isdir(os.path.join(GetUserDataPath(), 'FilesChecker4')):
        os.mkdir(os.path.join(GetUserDataPath(), 'FilesChecker4'))
    languagelist1 = glob.glob(os.path.join(GetProgPath(), 'Languages', 'Lang-*.py'))
    languagedic = {}
    languagelist = {}
    for i in languagelist1:
        if Verify_Signature(i, i + '.sig') or ('/DEBUG:DisableLangSign' in sys.argv[1:] and not (
                getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'))):
            spec = importlib.util.spec_from_file_location(os.path.basename(i), i)
            if spec is not None:
                Lang = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(Lang)
                for j in Lang.LANGUAGE[1]:
                    languagedic[j] = i
                languagelist[i] = Lang.LANGUAGE[2]
        else:
            languagelist1.remove(i)
    defaultsetting = {'Language': 'Auto',
                      'SaveTaskEncoding': 'UTF-8',
                      'ExportResultEncoding': 'ANSI',
                      'DefaultCheckMode': 0,
                      'ChecksumUpper': 0,
                      'CompatibleWithOldTask': 0}
    if platform.system() != 'Windows':
        defaultsetting['ExportResultEncoding'] = 'UTF-8'
    try:
        setting = LoadSetting()
    except Exception as err:
        setting = defaultsetting
        SaveSetting(setting)
    for i in defaultsetting.keys():
        if i not in setting.keys():
            setting[i] = defaultsetting[i]
    SaveSetting(setting)
    enspec = None
    enlang = None
    if os.path.isfile(os.path.join(GetProgPath(), 'Languages', 'Lang-en_GB.py')):
        if Verify_Signature(os.path.join(GetProgPath(), 'Languages', 'Lang-en_GB.py'),
                            os.path.join(GetProgPath(), 'Languages', 'Lang-en_GB.py.sig')) or (
                '/DEBUG:DisableLangSign' in sys.argv[1:] and not (
                getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'))):
            enspec = importlib.util.spec_from_file_location('Lang-en_GB.py',
                                                            os.path.join(GetProgPath(), 'Languages',
                                                                         'Lang-en_GB.py'))
            if enspec is not None:
                enlang = importlib.util.module_from_spec(enspec)
                enspec.loader.exec_module(enlang)
        else:
            toastone = wx.MessageDialog(None,
                                        'The software cannot be started because the verification of the language pack signature failed: .\\Lang-en_GB.py.',
                                        'FilesChecker',
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
            toastone.SetOKLabel('&OK')
            LoadOK = False
            if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
    else:
        toastone = wx.MessageDialog(None, 'Unable to start program due to missing Language .\\Lang-en_GB.py.',
                                    'FilesChecker',
                                    wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
        toastone.SetOKLabel('&OK')
        LoadOK = False
        if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
            toastone.Destroy()
    if LoadOK:
        if setting['Language'] == 'Auto' and locale in languagedic.keys():
            spec = importlib.util.spec_from_file_location(os.path.basename(languagedic[locale]),
                                                          languagedic[locale])
        elif (setting['Language'] == 'Auto' and locale not in languagedic.keys()) or os.path.join(
            GetProgPath(), 'Languages',
            str(setting['Language'])) not in languagelist1:
            spec = enspec
            setting['Language'] = 'Lang-en_GB.py'
            SaveSetting(setting)
        else:
            spec = importlib.util.spec_from_file_location(str(setting['Language']),
                                                          os.path.join(GetProgPath(), 'Languages',
                                                                       str(setting['Language'])))
        if spec is not None:

            lang = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(lang)
            Lang = LangProxy(lang, enlang)
        else:
            toastone = wx.MessageDialog(None, 'Unable to start program due to unable to load language pack.',
                                        'FilesChecker',
                                        wx.OK | wx.OK_DEFAULT | wx.ICON_ERROR)
            toastone.SetOKLabel('&OK')
            if toastone.ShowModal() == wx.ID_OK:  # 如果点击了提示框的确定按钮
                toastone.Destroy()
                LoadOK = False
    if LoadOK:
        if platform.system() == 'Darwin':
            macoslocale = wx.Locale(Lang.macoslocale())
            if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                macoslocale.AddCatalogLookupPathPrefix(os.path.join(GetProgPath(), 'locale'))
            macoslocale.AddCatalog('wxstd')
        frame = Main(None)
        frame.Show()
        if '/DEBUG:ForceEnableUpdate' in sys.argv[1:] or (getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')):
            otadlg = OTA(None)
        else:
            frame.m_menuItem11.Enable(False)
        app.MainLoop()

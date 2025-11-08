# coding=utf-8
# Copyright ©2025 ZHJ.

FOR = ['FilesChecker', (3, 1, 3), 'Windows']
LANGUAGE = [['English_United States'], 'English (Generic)', 'en_gb']
def s1():
    return 'FilesChecker'
def s2():
    return 'Start Chec&k'
def s3():
    return 'Add &File...'
def s4():
    return 'Add C&hecksum...'
def s5():
    return '&Open Task List...'
def s6():
    return '&Save Task List...'
def s7():
    return '&Export Check Result...'
def s8():
    return '&Clear List'
def s9():
    return '&Setting...'
def s10():
    return 'E&xit'
def s11():
    return '&Task'
def s12():
    return '&About'
def s13():
    return '&Help'
def s14():
    return 'Add &File...'
def s15():
    return 'Add C&hecksum...'
def s16():
    return 'Start Chec&k'
def s17():
    return 'No'
def s18():
    return 'Group No'
def s19():
    return 'File'
def s20():
    return 'Checksum'
def s21():
    return 'Auto'
def s22():
    return 'Add File'
def s23():
    return 'All files (*.*)|*.*'
def s24():
    return 'Setting'
def s25():
    return 'Operation After Completion'
def s26():
    return 'None'
def s27():
    return 'Shutdown'
def s28():
    return 'Reboot'
def s29():
    return 'Custom...'
def s30():
    return 'Automatically Save Check Result'
def s31():
    return 'Automatically Save Check Result'
def s32():
    return 'Export Check Result'
def s33():
    return 'Microsoft Excel Comma Separated Values File (*.csv)|*.csv|Text Document (*.txt)|*.txt|All files (*.*)|*.*'
def s34():
    return 'Routine'
def s35():
    return 'Language Setting'
def s36(list):
    if list:
        return 'Checksum type: ' + ' or '.join(map(str, list))
    else:
        return 'Checksum type: Unknown'
def s37():
    return '&Apply'
def s38():
    return '&Delete'
def s39():
    return 'The software needs to be restarted to change the language.Are you sure to continue?'
def s40():
    return 'Language'
def s41():
    pass
def s42():
    return 'Add Checksum'
def s43():
    pass
def s44():
    return 'About'
def s45(ver):
    return 'FilesChecker v' + '.'.join(map(str, ver))
def s46():
    return 'The language pack is not installed.'
def s47(pyver, wxver):
    return 'Python version: ' + pyver + '    wxPython version: ' + wxver
def s48():
    return 'Text Document (*.txt)|*.txt|All files (*.*)|*.*'
def s49():
    return 'Open Task List'
def s50():
    return 'Open Text Document'
def s51():
    return 'Please select the encoding used for the text document.'
def s52():
    return 'Preview: '
def s53():
    return 'OK'
def s54():
    return 'Cancel'
def s55():
    return 'Unable to read file: '
def s56():
    return 'Error reading task list: '
def s57():
    return '&OK'
def s58():
    return 'Task list error: Unsupported algorithm.'
def s59():
    return 'Task list error: The data type is not defined.'
def s60():
    return 'Save Task List'
def s61():
    return 'No data can be added in the task list.'
def s62():
    return 'Warning'
def s63():
    return '&Yes'
def s64():
    return '&No'
def s65():
    return 'Verifying. Are you sure to exit?'
def s66():
    return 'Elapsed time: '
def s67():
    return 'Processed: '
def s68():
    return 'Progress: '
def s69():
    return 'Overall progress: '
def s70():
    return 'Checksum Calculation'
def s71():
    return 'Processing: '
def s72():
    return 'Size: '
def s73():
    return 'bytes'
def s74():
    return 'Time: '
def s75(err):
    return 'The error(s) occurred, the following is the error message: \n' + err
def s76():
    return '&Show Details'
def s77():
    return 'Re-Sele&ct File'
def s78():
    return '&Edit Checksum'
def s79():
    return 'Copy &File Address'
def s80():
    return 'Copy C&hecksum'
def s81():
    return 'Error'
def s82():
    return 'Calculating Checksum...'
def s83():
    return 'Checking...'
def s84():
    return 'Exporting Check Result: '
def s85():
    return 'Running Command: '
def s86():
    return 'Saving Task List: '
def s87():
    return 'Re-Select File'
def s88():
    return 'Edit Checksum'
def s89():
    return 'Has been copied to the clipboard.'
def s90():
    return 'Run Command: '
def s91():
    return 'The setting item "Automatically Save Check Results" is invalid.'
def s92():
    return 'Details'
def s93():
    return 'File: '
def s94():
    return 'Checksum: '
def s95():
    return 'Calculation Time: '
def s96():
    return 'Error Message: '
def s97():
    return 'Calculate the checksum and verify it.'
def s98():
    return 'Add one or more files.'
def s99():
    return 'Add Checksum.'
def s100():
    return 'Load the task from a file.'
def s101():
    return 'Save the task to a file.'
def s102():
    return 'Export the Check result to a file.'
def s103():
    return 'Change the settings of the software.'
def s104():
    return 'Exit this software.'
def s105():
    return 'Display software information, version number, and copyright.'
def s106():
    return 'Task List'
def s107():
    return 'Use encoding when saving task list: '
def s108():
    return 'Check Result'
def s109():
    return 'Use encoding when exporting check result: '
def s110():
    return '&Restore Default Settings'
def s111():
    return 'File Encoding'
def s112():
    return 'The user cancelled the operation.'
def s113():
    return '&Pause'
def s114():
    return '&Continue'
def s115():
    return 'Are you sure you want to cancel?'
def s116():
    return 'Software &Update...'
def s117():
    return 'Software Update'
def s118(ver):
    return 'Current Version: ' + '.'.join(map(str, ver))
def s119(version):
    if version:
        return 'Lastest Version: ' + '.'.join(map(str, version))
    else:
        return 'Lastest Version: '
def s120():
    return 'Checking for updates...'
def s121():
    return 'Download progress: '
def s122():
    return '&Check'
def s123():
    return 'Connecting...'
def s124():
    return '&Update'
def s125():
    return 'Patch package size: '
def s126():
    return 'Full package size: '
def s127():
    return 'Unable to obtain updates, please try again later.'
def s128():
    return 'remaining'
def s129():
    return 'Work &Directory...'
def s130():
    return ['Mode 1', 'Mode 2']
def s131():
    return '&Add Item...'
def s132():
    return 'Add a item.'
def s133():
    return '&Add Item...'
def s134():
    return 'Expected Checksum'
def s135():
    return 'Results'
def s136():
    return 'Set Work Directory'
def s137():
    return 'Switching modes will clear the list. Do you want to continue?'
def s138():
    return 'Expected Checksum: '
def s139():
    return 'Software updates are available.'
def s140():
    return 'Add Item'
def s141():
    return 'File: '
def s142():
    return 'Expected Checksum: '
def s143():
    return 'Invalid File'
def s144():
    return 'Select the file again and try again.'
def s145():
    return 'Paste or load task list from file.'
def s146():
    return 'Load &File...'
def s147():
    return 'All Supported Files (*.md5; *.sha; *.sha1; *.sha256; *.txt)|*.md5; *.sha; *.sha1; *.sha256; *.txt|Text Document (*.txt)|*.txt|All files (*.*)|*.*'
def s148():
    return 'When Starting the Software'
def s149():
    return 'Default check mode: '
def s150():
    return 'Another instance is running. '
def s151():
    return 'Verifying: '
def s152():
    return 'Update file verification error, please check network connection.'

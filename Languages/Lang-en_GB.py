import platform

FOR = ['FilesChecker', (4, 0, 1)]
LANGUAGE = ['en_gb', ['English_United States'], 'English (Universal)']
AUTHOR = 'ZHJ'

def title():
    return 'FilesChecker'
def macoslocale():
    return 276  # wx.LANGUAGE_ENGLISH_US
def menuitem_startcheck():
    return 'Start Chec&k...'
def menuitem_startcheck_help():
    return 'Calculate the checksum and verify it. '
def menuitem_addfile():
    return 'Add &Files...'
def menuitem_addfile_help():
    return 'Add one or more files. '
def menuitem_addchecksum():
    return 'Add C&hecksum...'
def menuitem_addchecksum_help():
    return 'Add Checksum. '
def menuitem_additem():
    return '&Add Item...'
def menuitem_additem_help():
    return 'Add a item. '
def menuitem_opentask():
    return 'Open &Task List...'
def menuitem_opentask_help():
    return 'Load the task from a file. '
def menuitem_savetask():
    return 'Save &Task List...'
def menuitem_savetask_help():
    return 'Save the task to a file. '
def menuitem_exportresult():
    return '&Export Check Result...'
def menuitem_exportresult_help():
    return 'Export the Check result to a file. '
def menuitem_clear():
    return '&Clear List'
def menuitem_workdir():
    return 'Work &Directory...'
def menuitem_settings():
    return '&Settings...'
def menuitem_settings_help():
    return 'Change the settings of the software. '
def menuitem_exit():
    return 'E&xit'
def menuitem_exit_help():
    return 'Exit this software. '
def menuitem_hide_macos():
    return 'Hide ' + title()
def menuitem_exit_macos():
    return 'Quit ' + title()
def menu_task():
    return '&Task'
def menuitem_ota():
    return 'Software &Update...'
def menuitem_about():
    return '&About'
def menuitem_about_help():
    return 'Display software information, version number, and copyright. '
def menu_help():
    return '&Help'
def choice_mode1():
    return 'Mode 1'
def choice_mode2():
    return 'Mode 2'
def btn_addfile():
    return 'Add &Files...'
def btn_addchecksum():
    return 'Add C&hecksum...'
def btn_additem():
    return '&Add Item...'
def btn_startcheck():
    return 'Start Chec&k'
def list_no():
    return 'No'
def list_groupno():
    return 'Group No'
def list_file():
    return 'File'
def list_checksum():
    return 'Checksum'
def list_expected_checksum():
    return 'Expected Checksum'
def list_result():
    return 'Result'
def switchmode_warning():
    return 'Switching modes will clear the list. Do you want to continue? '
def dlg_btn_yes():
    return '&Yes'
def dlg_btn_no():
    return '&No'
def dlg_btn_ok():
    return '&OK'
def dlg_btn_cancel():
    return 'Cancel'
def dlg_btn_apply():
    return '&Apply'
def str_error():
    return 'Error'
def filedlg_title_add():
    return 'Add Files'
def filedlg_title_reselect():
    return 'Re-Select File'
def filedlg_title_opentask():
    return 'Open Task List'
def filedlg_title_savetask():
    return 'Save Task List'
def filedlg_title_exportresult():
    return 'Export Check Result'
def filedlg_wildcard_1():
    return 'All files (*.*)|*.*'
def filedlg_wildcard_2():
    return 'Text Document (*.txt)|*.txt|All files (*.*)|*.*'
def filedlg_wildcard_3():
    return 'Microsoft Excel Comma Separated Values File (*.csv)|*.csv|Text Document (*.txt)|*.txt|All files (*.*)|*.*'
def workdirdlg_title():
    return 'Set Work Directory'
def error_message(err):
    return 'The error(s) occurred, the following is the error message: \n' + err
def rightmenu_show_details():
    return 'Show &Details'
def rightmenu_reslect_file():
    return 'Re-Select &File...'
def rightmenu_edit_checksum():
    return 'Edit C&hecksum...'
def rightmenu_copy_file_address():
    return 'Copy &File Address'
def rightmenu_copy_checksum():
    return 'Copy C&hecksum'
def rightmenu_delete():
    return '&Delete'
def error_nodata():
    return 'No data can be added in the task list.'
def error_loading_task(err):
    return 'Error reading task list: ' + err
def error_unsupported_algorithm():
    return 'Task list error: Unsupported algorithm.'
def error_not_defined():
    return 'Task list error: The data type is not defined.'
def error_operation_cancelled():
    return 'The user cancelled the operation. '
def status_saving(path):
    return 'Saving Task List: ' + path
def status_exporting(path):
    return 'Exporting Check Result: ' + path
def status_calculating():
    return 'Calculating Checksum...'
def status_checking():
    return 'Checking...'
def ota_hint():
    return 'Software updates are available. '
def settingdlg_title():
    return 'Settings'
def settingdlg_staticbox_starting():
    return 'When Starting the Software'
def settingdlg_default_checkmode():
    return 'Default Check Mode: '
def settingdlg_operation_after_completion():
    return 'Operation After Completion'
def settingdlg_oac_run_command():
    return 'Run Command: '
def settingdlg_oac_run_command_none():
    return 'None'
def settingdlg_oac_run_command_shutdown():
    return 'Shutdown'
def settingdlg_oac_run_command_reboot():
    return 'Reboot'
def settingdlg_oac_run_command_custom():
    return 'Custom...'
def settingdlg_staticbox_ascr():
    return 'Automatically Save Check Result'
def settingdlg_checkbox_ascr():
    return 'Automatically Save Check Result'
def settingdlg_ascr_pathpicker_title():
    return 'Export Check Result'
def settingdlg_ascr_pathpicker_wildcards():
    return 'Microsoft Excel Comma Separated Values File (*.csv)|*.csv|Text Document (*.txt)|*.txt|All files (*.*)|*.*'
def settingdlg_staticbox_other():
    return 'Other'
def settingdlg_other_uppercase():
    return 'Display The Checksum in Uppercase'
def settingdlg_page_routine():
    return 'Routine'
def settingdlg_staticbox_tasklist():
    return 'Task List'
def settingdlg_tasklist_encoding():
    return 'Use encoding when saving task list: '
def settingdlg_checkbox_cwov():
    return 'Compatible with Old Versions'
def settingdlg_staticbox_checkresult():
    return 'Check Result'
def settingdlg_checkresult_encoding():
    return 'Use encoding when exporting check result: '
def settingdlg_btn_restore():
    return '&Restore Default Settings'
def settingdlg_page_files():
    return 'Files'
def settingdlg_staticbox_language_setting():
    return 'Language Setting'
def settingdlg_page_language():
    return 'Language'
def settingdlg_language_auto():
    return 'Auto'
def settingdlg_language_error_notinstalled():
    return 'The language pack is not installed. '
def settingdlg_language_error_signature_failure():
    return 'Unable to verify language pack signature. '
def settingdlg_language_error_failure():
    return 'Unable to change the language. '
def settingdlg_error_ascr_invaild():
    return 'The setting item "Automatically Save Check Results" is invalid. '
def settingdlg_warning_save():
    return 'Do you want to save the changed settings? '
def settingdlg_warning_changelang():
    return 'Switching languages requires clearing the list. \nTo change the language immediately, click "Yes"; To use the new language on the next startup, click "No".'
def settingdlg_warning_changelang_later(lang:str):
    return 'The language will be used next time the software is launched: \n' + lang
def checksumdlg_title_add():
    return 'Add Checksum'
def checksumdlg_title_edit():
    return 'Edit Checksum'
def checksumdlg_checksum_type(l:list):
    if l:
        return 'Checksum Type: ' + ' or '.join(map(str, l))
    else:
        return 'Checksum Type: Unknown'
def aboutdlg_title():
    return 'About'
def aboutdlg_software_name(arch: str):
    return title() + ' ' + arch
def aboutdlg_version(ver: tuple):
    return 'Version: ' + '.'.join(map(str, ver))
def aboutdlg_build(build: str):
    return 'Build: ' + build
def aboutdlg_pyver(ver: str):
    return 'Python Version: ' + ver
def aboutdlg_wxpyver(ver: str):
    return 'wxPython Version: ' + ver
def aboutdlg_language():
    return 'Localization: ' + AUTHOR
def aboutdlg_open_source_declaration(license):
    return 'This software is licensed under ' + license + '.'
def calcdlg_title(count=None):
    if count is None:
        return 'Checksum Calculation'
    else:
        return '(' + str(count[0]) + '/' + str(count[1]) + ') Checksum Calculation'
def calcdlg_elapsed_time():
    return 'Elapsed Time: '
def calcdlg_file():
    return 'File: '
def calcdlg_size():
    return 'Size: '
def calcdlg_speed():
    return 'Speed: '
def calcdlg_progress():
    return 'Progress: '
def calcdlg_overall_progress():
    return 'Overall Progress: '
def calcdlg_str_bytes():
    return 'bytes'
def calcdlg_warning_cancel():
    return 'Are you sure you want to cancel? '
def calcdlg_btn_pause():
    return '&Pause'
def calcdlg_btn_continue():
    return '&Continue'
def encodingpickerdlg_title(file:str=''):
    if file:
        return 'Open Text Document - ' + file
    else:
        return 'Open Text Document'
def encodingpickerdlg_hint():
    return 'Please select the encoding. '
def encodingpickerdlg_preview():
    return 'Preview: '
def detailsdlg_title():
    return 'Details'
def detailsdlg_file():
    return 'File: '
def detailsdlg_checksum():
    return 'Checksum: '
def detailsdlg_expected_checksum():
    return 'Expected Checksum: '
def detailsdlg_time():
    return 'Calculation Time: '
def detailsdlg_error():
    return 'Error Message: '
def detailsdlg_actual_checksum():
    return 'Actual Checksum: '
def detailsdlg_none():
    return '<None>'
def itemdlg_title():
    return 'Add Item'
def itemdlg_file():
    return 'File: '
def itemdlg_expected_checksum():
    return 'Expected Checksum: '
def itemdlg_checksum_type_title():
    return 'Checksum Type: '
def itemdlg_checksum_type(l:list):
    if l:
        return ' or '.join(map(str, l))
    else:
        return 'Unknown'
def itemdlg_invalid_file_error(file:str=''):
    return 'Invalid File: ' + file
def opentaskdlg_title():
    return 'Open Task List'
def opentaskdlg_hint():
    return 'Paste or load task list from file. '
def opentaskdlg_loadfile():
    return 'Load &File...'
def opentaskdlg_loadfile_wildcard():
    return 'All Supported Files (*.md5; *.sha; *.sha1; *.sha256; *.txt)|*.md5; *.sha; *.sha1; *.sha256; *.txt|Text Document (*.txt)|*.txt|All files (*.*)|*.*'
def otadlg_title():
    return 'Software Update'
def otadlg_software_name(arch: str):
    return title() + ' ' + arch
def otadlg_current_ver(ver: tuple):
    return 'Current Version: ' + '.'.join(map(str, ver))
def otadlg_lastest_ver(ver: tuple):
    if ver:
        return 'Lastest Version: ' + '.'.join(map(str, ver))
    else:
        return 'Lastest Version: '
def otadlg_btn_check():
    return '&Check'
def otadlg_btn_update():
    return '&Update'
def otadlg_md_checking():
    return 'Checking for updates...'
def otadlg_connecting():
    return 'Connecting...'
def otadlg_progress(progress: str, speed:str, eta: str):
    return 'Download progress: ' + progress + '% (' + speed + 'B/s, remaining: ' + eta + ')'
def otadlg_patch_size(size: str):
    return 'Patch package size: ' + size
def otadlg_full_size(size: str):
    return 'Full package size: ' + size
def otadlg_verifying(progress: str):
    return 'Verifying: ' + progress + '%'
def otadlg_verification_error():
    return 'Update file verification error, please check network connection. '
def otadlg_md_failure():
    return 'Unable to obtain updates, please try again later. '

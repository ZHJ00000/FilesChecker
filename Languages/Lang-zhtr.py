import platform

FOR = ['FilesChecker', (4, 0, 1)]
LANGUAGE = ['zhtr', ['Chinese (Traditional)_Taiwan', 'Chinese (Traditional)_Hong Kong SAR', 'Chinese (Traditional)_Macao SAR', 'zh_HK', 'zh_MO', 'zh-Hant_CN'], '繁體中文 (中國香港特別行政區、中國澳門特別行政區、中國臺灣)']
AUTHOR = 'ZHJ'

def title():
    return '文件校驗器'
def macoslocale():
    return 137  #LANGUAGE_CHINESE_TRADITIONAL
def menuitem_startcheck():
    if platform.system() == 'Darwin':
        return '開始校驗'
    else:
        return '開始校驗(&K)'
def menuitem_startcheck_help():
    return '計算校驗和並校驗。'
def menuitem_addfile():
    if platform.system() == 'Darwin':
        return '添加文件…'
    else:
        return '添加文件(&F)…'
def menuitem_addfile_help():
    return '添加一個或多個檔。'
def menuitem_addchecksum():
    if platform.system() == 'Darwin':
        return '添加校驗和…'
    else:
        return '添加校驗和(&H)…'
def menuitem_addchecksum_help():
    return '添加校驗和。'
def menuitem_additem():
    if platform.system() == 'Darwin':
        return '添加項目…'
    else:
        return '添加項目(&A)…'
def menuitem_additem_help():
    return '添加一個項目。'
def menuitem_opentask():
    if platform.system() == 'Darwin':
        return '導入任務清單…'
    else:
        return '導入任務清單(&O)…'
def menuitem_opentask_help():
    return '從檔載入任務清單。'
def menuitem_savetask():
    if platform.system() == 'Darwin':
        return '保存任務清單…'
    else:
        return '保存任務清單(&S)…'
def menuitem_savetask_help():
    return '將任務清單保存到檔。'
def menuitem_exportresult():
    if platform.system() == 'Darwin':
        return '匯出校驗結果…'
    else:
        return '匯出校驗結果(&E)…'
def menuitem_exportresult_help():
    return '將校驗結果匯出到檔。'
def menuitem_clear():
    if platform.system() == 'Darwin':
        return '清空列表'
    else:
        return '清空列表(&C)'
def menuitem_workdir():
    if platform.system() == 'Darwin':
        return '工作目錄…'
    else:
        return '工作目錄(&D)…'
def menuitem_settings():
    if platform.system() == 'Darwin':
        return '設定…'
    else:
        return '設定(&S)…'
def menuitem_settings_help():
    return '更改軟體的設定。'
def menuitem_exit():
    if platform.system() == 'Darwin':
        return '退出'
    else:
        return '退出(&X)'
def menuitem_exit_help():
    return '退出本軟體。'
def menuitem_hide_macos():
    return '隱藏' + title()
def menuitem_exit_macos():
    return '退出' + title()
def menu_task():
    return '任務(&T)'
def menuitem_ota():
    if platform.system() == 'Darwin':
        return '軟體更新'
    else:
        return '軟體更新(&U)'
def menuitem_about():
    if platform.system() == 'Darwin':
        return '關於…'
    else:
        return '關於(&A)…'
def menuitem_about_help():
    return '顯示軟體資訊、版本號和版權。'
def menu_help():
    if platform.system() == 'Darwin':
        return '幫助'
    else:
        return '幫助(&H)'
def choice_mode1():
    return '模式 1'
def choice_mode2():
    return '模式 2'
def btn_addfile():
    if platform.system() == 'Darwin':
        return '添加文件…'
    else:
        return '添加文件(&F)…'
def btn_addchecksum():
    if platform.system() == 'Darwin':
        return '添加校驗和…'
    else:
        return '添加校驗和(&H)…'
def btn_additem():
    if platform.system() == 'Darwin':
        return '添加項目…'
    else:
        return '添加項目(&A)…'
def btn_startcheck():
    if platform.system() == 'Darwin':
        return '開始校驗'
    else:
        return '開始校驗(&K)'
def list_no():
    return '序號'
def list_groupno():
    return '組號'
def list_file():
    return '文件'
def list_checksum():
    return '校驗和'
def list_expected_checksum():
    return '預期校驗和'
def list_result():
    return '校驗結果'
def switchmode_warning():
    return '切換模式將清空清單，是否繼續？'
def dlg_btn_yes():
    if platform.system() == 'Darwin':
        return '是'
    else:
        return '是(&Y)'
def dlg_btn_no():
    if platform.system() == 'Darwin':
        return '否'
    else:
        return '否(&N)'
def dlg_btn_ok():
    if platform.system() == 'Darwin':
        return '好'
    else:
        return '確定(&O)'
def dlg_btn_cancel():
    return '取消'
def dlg_btn_apply():
    if platform.system() == 'Darwin':
        return '應用'
    else:
        return '應用(&A)'
def str_error():
    return '錯誤'
def filedlg_title_add():
    return '添加文件'
def filedlg_title_reselect():
    return '重新選擇檔'
def filedlg_title_opentask():
    return '導入任務清單'
def filedlg_title_savetask():
    return '保存任務清單'
def filedlg_title_exportresult():
    return '匯出校驗結果'
def filedlg_wildcard_1():
    return '所有檔案 (*.*)|*.*'
def filedlg_wildcard_2():
    return '文字文件 (*.txt)|*.txt|所有檔案 (*.*)|*.*'
def filedlg_wildcard_3():
    return 'Microsoft Excel 逗號分隔值文件 (*.csv)|*.csv|文字文件 (*.txt)|*.txt|所有檔案 (*.*)|*.*'
def workdirdlg_title():
    return '設定工作目錄'
def error_message(err):
    return '發生錯誤，以下是錯誤資訊：\n' + err
def rightmenu_show_details():
    if platform.system() == 'Darwin':
        return '顯示詳細資訊'
    else:
        return '顯示詳細資訊(&S)'
def rightmenu_reslect_file():
    if platform.system() == 'Darwin':
        return '重新選擇檔…'
    else:
        return '重新選擇檔(&C)…'
def rightmenu_edit_checksum():
    if platform.system() == 'Darwin':
        return '編輯校驗和…'
    else:
        return '編輯校驗和(&E)…'
def rightmenu_copy_file_address():
    if platform.system() == 'Darwin':
        return '複製檔地址(&F)'
    else:
        return '複製檔地址(&F)'
def rightmenu_copy_checksum():
    if platform.system() == 'Darwin':
        return '複製校驗和'
    else:
        return '複製校驗和(&H)'
def rightmenu_delete():
    if platform.system() == 'Darwin':
        return '刪除'
    else:
        return '刪除(&D)'
def error_nodata():
    return '任務清單中不含任何可添加資料。'
def error_loading_task(err):
    return '無法讀取任務清單：' + err
def error_unsupported_algorithm():
    return '任務清單錯誤：不支援的演算法。'
def error_not_defined():
    return '任務清單錯誤：未定義資料類型。'
def error_operation_cancelled():
    return '用戶取消了操作。'
def status_saving(path):
    return '正在保存任務清單：' + path
def status_exporting(path):
    return '正在保存校驗結果：' + path
def status_calculating():
    return '正在計算校驗和…'
def status_checking():
    return '正在校驗…'
def ota_hint():
    return '有軟體更新可用。'
def settingdlg_title():
    return '設定'
def settingdlg_staticbox_starting():
    return '啟動軟件時'
def settingdlg_default_checkmode():
    return '默認校驗模式：'
def settingdlg_operation_after_completion():
    return '完成後操作'
def settingdlg_oac_run_command():
    return '運行命令：'
def settingdlg_oac_run_command_none():
    return '無'
def settingdlg_oac_run_command_shutdown():
    return '關機'
def settingdlg_oac_run_command_reboot():
    return '重啟'
def settingdlg_oac_run_command_custom():
    return '自訂…'
def settingdlg_staticbox_ascr():
    return '自動保存校驗結果'
def settingdlg_checkbox_ascr():
    return '自動保存校驗結果'
def settingdlg_ascr_pathpicker_title():
    return '匯出校驗結果'
def settingdlg_ascr_pathpicker_wildcards():
    return 'Microsoft Excel 逗號分隔值文件 (*.csv)|*.csv|文字文件 (*.txt)|*.txt|所有檔案 (*.*)|*.*'
def settingdlg_staticbox_other():
    return '其他'
def settingdlg_other_uppercase():
    return '將校驗和顯示為大寫'
def settingdlg_page_routine():
    return '常規'
def settingdlg_staticbox_tasklist():
    return '任務清單'
def settingdlg_tasklist_encoding():
    return '保存任務清單時使用編碼：'
def settingdlg_checkbox_cwov():
    return '與舊版本相容'
def settingdlg_staticbox_checkresult():
    return '校驗結果'
def settingdlg_checkresult_encoding():
    return '匯出校驗結果時使用編碼：'
def settingdlg_btn_restore():
    if platform.system() == 'Darwin':
        return '恢復默認設置'
    else:
        return '恢復默認設置(&R)'
def settingdlg_page_files():
    return '文件'
def settingdlg_staticbox_language_setting():
    return '語言設定'
def settingdlg_page_language():
    return '語言'
def settingdlg_language_auto():
    return '自動'
def settingdlg_language_error_notinstalled():
    return '未安裝該語言包。'
def settingdlg_language_error_signature_failure():
    return '無法驗證語言包簽名。'
def settingdlg_language_error_failure():
    return '無法切換語言。'
def settingdlg_error_ascr_invaild():
    return '設置項"自動保存校驗結果"無效。'
def settingdlg_warning_save():
    return '要保存更改的設定嗎？'
def settingdlg_warning_changelang():
    return '切換語言需要清空清單。\n要立即更改語言，請按一下“是（Y）”； 要在下次啟動時使用新語言，請按一下“否（N）”。'
def settingdlg_warning_changelang_later(lang:str):
    return '下次啟動軟件時將使用語言：\n' + lang
def checksumdlg_title_add():
    return '添加校驗和'
def checksumdlg_title_edit():
    return '編輯校驗和'
def checksumdlg_checksum_type(l:list):
    if l:
        return '雜湊數值型別：' + ' 或 '.join(map(str, l))
    else:
        return '雜湊數值型別：未知'
def aboutdlg_title():
    return '關於'
def aboutdlg_software_name(arch: str):
    return title() + ' ' + arch
def aboutdlg_version(ver: tuple):
    return '版本：' + '.'.join(map(str, ver))
def aboutdlg_build(build: str):
    return '構建版本：' + build
def aboutdlg_pyver(ver: str):
    return 'Python 版本：' + ver
def aboutdlg_wxpyver(ver: str):
    return 'wxPython 版本：' + ver
def aboutdlg_language():
    return '當地語系化：' + AUTHOR
def aboutdlg_open_source_declaration(license):
    return '本軟體使用 ' + license + ' 開源。'
def calcdlg_title(count=None):
    if count is None:
        return '校驗和計算'
    else:
        return '(' + str(count[0]) + '/' + str(count[1]) + ') 校驗和計算'
def calcdlg_elapsed_time():
    return '已用時間：'
def calcdlg_file():
    return '文件: '
def calcdlg_size():
    return '大小：'
def calcdlg_speed():
    return '速度：'
def calcdlg_progress():
    return '進度：'
def calcdlg_overall_progress():
    return '總進度：'
def calcdlg_str_bytes():
    return '位元組'
def calcdlg_warning_cancel():
    return '你確定要取消嗎？'
def calcdlg_btn_pause():
    if platform.system() == 'Darwin':
        return '暫停'
    else:
        return '暫停(&P)'
def calcdlg_btn_continue():
    if platform.system() == 'Darwin':
        return '繼續'
    else:
        return '繼續(&C)'
def encodingpickerdlg_title(file:str=''):
    if file:
        return '打開文字文件 - ' + file
    else:
        return '打開文字文件'
def encodingpickerdlg_hint():
    return '請選擇文字文件使用的編碼。'
def encodingpickerdlg_preview():
    return '預覽：'
def detailsdlg_title():
    return '詳細資訊'
def detailsdlg_file():
    return '文件：'
def detailsdlg_checksum():
    return '校驗和：'
def detailsdlg_expected_checksum():
    return '預期校驗和：'
def detailsdlg_time():
    return '計算耗時：'
def detailsdlg_error():
    return '錯誤資訊：'
def detailsdlg_actual_checksum():
    return '實際校驗和：'
def detailsdlg_none():
    return '<無>'
def itemdlg_title():
    return '添加項目'
def itemdlg_file():
    return '文件：'
def itemdlg_expected_checksum():
    return '預期校驗和：'
def itemdlg_checksum_type_title():
    return '雜湊數值型別：'
def itemdlg_checksum_type(l:list):
    if l:
        return ' 或 '.join(map(str, l))
    else:
        return '未知'
def itemdlg_invalid_file_error(file:str=''):
    return '無效的檔案：' + file
def opentaskdlg_title():
    return '導入任務清單'
def opentaskdlg_hint():
    return '粘貼或從檔案加載任務清單。'
def opentaskdlg_loadfile():
    if platform.system() == 'Darwin':
        return '加載檔案…'
    else:
        return '加載檔案(&F)…'
def opentaskdlg_loadfile_wildcard():
    return '所有支持的檔案 (*.md5; *.sha; *.sha1; *.sha256; *.txt)|*.md5; *.sha; *.sha1; *.sha256; *.txt|文字文件 (*.txt)|*.txt|所有檔案 (*.*)|*.*'
def otadlg_title():
    return '軟體更新'
def otadlg_software_name(arch: str):
    return title() + ' ' + arch
def otadlg_current_ver(ver: tuple):
    return '當前版本：' + '.'.join(map(str, ver))
def otadlg_lastest_ver(ver: tuple):
    if ver:
        return '最新版本：' + '.'.join(map(str, ver))
    else:
        return '最新版本：'
def otadlg_btn_check():
    if platform.system() == 'Darwin':
        return '檢查'
    else:
        return '檢查(&C)'
def otadlg_btn_update():
    if platform.system() == 'Darwin':
        return '更新'
    else:
        return '更新(&U)'
def otadlg_md_checking():
    return '正在檢查更新…'
def otadlg_connecting():
    return '連接中…'
def otadlg_progress(progress: str, speed:str, eta: str):
    return '下载进度：' + progress + '% (' + speed + 'B/s, 剩餘：' + eta + ')'
def otadlg_patch_size(size: str):
    return '補丁包大小：' + size
def otadlg_full_size(size: str):
    return '完整包大小：' + size
def otadlg_verifying(progress: str):
    return '正在校驗：' + progress + '%'
def otadlg_verification_error():
    return '更新檔案校驗錯誤，請檢查網絡連接。'
def otadlg_md_failure():
    return '無法獲取更新，請稍後再試。'

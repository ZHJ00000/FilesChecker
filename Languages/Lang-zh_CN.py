import platform

FOR = ['FilesChecker', (4, 0, 1)]
LANGUAGE = ['zh_cn', ['Chinese (Simplified)_China', 'zh_CN'], '简体中文 (中国大陆)']
AUTHOR = 'ZHJ'

def title():
    return '文件校验器'
def macoslocale():
    return 130  #wx.LANGUAGE_CHINESE_SIMPLIFIED
def menuitem_startcheck():
    if platform.system() == 'Darwin':
        return '开始校验'
    else:
        return '开始校验(&K)'
def menuitem_startcheck_help():
    return '计算校验和并校验。'
def menuitem_addfile():
    if platform.system() == 'Darwin':
        return '添加文件…'
    else:
        return '添加文件(&F)…'
def menuitem_addfile_help():
    return '添加一个或多个文件。'
def menuitem_addchecksum():
    if platform.system() == 'Darwin':
        return '添加校验和…'
    else:
        return '添加校验和(&H)…'
def menuitem_addchecksum_help():
    return '添加校验和。'
def menuitem_additem():
    if platform.system() == 'Darwin':
        return '添加项目…'
    else:
        return '添加项目(&A)…'
def menuitem_additem_help():
    return '添加一个项目。'
def menuitem_opentask():
    if platform.system() == 'Darwin':
        return '导入任务列表…'
    else:
        return '导入任务列表(&O)…'
def menuitem_opentask_help():
    return '从文件加载任务列表。'
def menuitem_savetask():
    if platform.system() == 'Darwin':
        return '保存任务列表…'
    else:
        return '保存任务列表(&S)…'
def menuitem_savetask_help():
    return '将任务列表保存到文件。'
def menuitem_exportresult():
    if platform.system() == 'Darwin':
        return '导出校验结果…'
    else:
        return '导出校验结果(&E)…'
def menuitem_exportresult_help():
    return '将校验结果导出到文件。'
def menuitem_clear():
    if platform.system() == 'Darwin':
        return '清空列表'
    else:
        return '清空列表(&C)'
def menuitem_workdir():
    if platform.system() == 'Darwin':
        return '工作目录…'
    else:
        return '工作目录(&D)…'
def menuitem_settings():
    if platform.system() == 'Darwin':
        return '设置…'
    else:
        return '设置(&S)…'
def menuitem_settings_help():
    return '更改软件的设置。'
def menuitem_exit():
    if platform.system() == 'Darwin':
        return '退出'
    else:
        return '退出(&X)'
def menuitem_exit_help():
    return '退出本软件。'
def menuitem_hide_macos():
    return '隐藏' + title()
def menuitem_exit_macos():
    return '退出' + title()
def menu_task():
    return '任务(&T)'
def menuitem_ota():
    if platform.system() == 'Darwin':
        return '软件更新'
    else:
        return '软件更新(&U)'
def menuitem_about():
    if platform.system() == 'Darwin':
        return '关于…'
    else:
        return '关于(&A)…'
def menuitem_about_help():
    return '显示软件信息、版本号和版权。'
def menu_help():
    if platform.system() == 'Darwin':
        return '帮助'
    else:
        return '帮助(&H)'
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
        return '添加校验和…'
    else:
        return '添加校验和(&H)…'
def btn_additem():
    if platform.system() == 'Darwin':
        return '添加项目…'
    else:
        return '添加项目(&A)…'
def btn_startcheck():
    if platform.system() == 'Darwin':
        return '开始校验'
    else:
        return '开始校验(&K)'
def list_no():
    return '序号'
def list_groupno():
    return '组号'
def list_file():
    return '文件'
def list_checksum():
    return '校验和'
def list_expected_checksum():
    return '预期校验和'
def list_result():
    return '校验结果'
def switchmode_warning():
    return '切换模式将清空列表，是否继续？'
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
        return '确定(&O)'
def dlg_btn_cancel():
    return '取消'
def dlg_btn_apply():
    if platform.system() == 'Darwin':
        return '应用'
    else:
        return '应用(&A)'
def str_error():
    return '错误'
def filedlg_title_add():
    return '添加文件'
def filedlg_title_reselect():
    return '重新选择文件'
def filedlg_title_opentask():
    return '导入任务列表'
def filedlg_title_savetask():
    return '保存任务列表'
def filedlg_title_exportresult():
    return '导出校验结果'
def filedlg_wildcard_1():
    return '所有文件 (*.*)|*.*'
def filedlg_wildcard_2():
    return '文本文档 (*.txt)|*.txt|所有文件 (*.*)|*.*'
def filedlg_wildcard_3():
    return 'Microsoft Excel 逗号分隔值文件 (*.csv)|*.csv|文本文档 (*.txt)|*.txt|所有文件 (*.*)|*.*'
def workdirdlg_title():
    return '设置工作目录'
def error_message(err):
    return '发生错误，以下是错误信息：\n' + err
def rightmenu_show_details():
    if platform.system() == 'Darwin':
        return '显示详细信息'
    else:
        return '显示详细信息(&D)'
def rightmenu_reslect_file():
    if platform.system() == 'Darwin':
        return '重新选择文件…'
    else:
        return '重新选择文件(&F)…'
def rightmenu_edit_checksum():
    if platform.system() == 'Darwin':
        return '编辑校验和…'
    else:
        return '编辑校验和(&H)…'
def rightmenu_copy_file_address():
    if platform.system() == 'Darwin':
        return '拷贝文件地址'
    else:
        return '复制文件地址(&F)'
def rightmenu_copy_checksum():
    if platform.system() == 'Darwin':
        return '拷贝校验和'
    else:
        return '复制校验和(&H)'
def rightmenu_delete():
    if platform.system() == 'Darwin':
        return '删除'
    else:
        return '删除(&D)'
def error_nodata():
    return '任务列表中不含任何可添加数据。'
def error_loading_task(err):
    return '无法读取任务列表：' + err
def error_unsupported_algorithm():
    return '任务列表错误：不支持的算法。'
def error_not_defined():
    return '任务列表错误：未定义数据类型。'
def error_operation_cancelled():
    return '用户取消了操作。'
def status_saving(path):
    return '正在保存任务列表：' + path
def status_exporting(path):
    return '正在导出校验结果：' + path
def status_calculating():
    return '正在计算校验和…'
def status_checking():
    return '正在校验…'
def ota_hint():
    return '有软件更新可用。'
def settingdlg_title():
    return '设置'
def settingdlg_staticbox_starting():
    return '启动软件时'
def settingdlg_default_checkmode():
    return '默认校验模式：'
def settingdlg_operation_after_completion():
    return '完成后操作'
def settingdlg_oac_run_command():
    return '运行命令：'
def settingdlg_oac_run_command_none():
    return '无'
def settingdlg_oac_run_command_shutdown():
    return '关机'
def settingdlg_oac_run_command_reboot():
    return '重启'
def settingdlg_oac_run_command_custom():
    return '自定义…'
def settingdlg_staticbox_ascr():
    return '自动保存校验结果'
def settingdlg_checkbox_ascr():
    return '自动保存校验结果'
def settingdlg_ascr_pathpicker_title():
    return '导出校验结果'
def settingdlg_ascr_pathpicker_wildcards():
    return 'Microsoft Excel 逗号分隔值文件 (*.csv)|*.csv|文本文档 (*.txt)|*.txt|所有文件 (*.*)|*.*'
def settingdlg_staticbox_other():
    return '其他'
def settingdlg_other_uppercase():
    return '将校验和显示为大写'
def settingdlg_page_routine():
    return '常规'
def settingdlg_staticbox_tasklist():
    return '任务列表'
def settingdlg_tasklist_encoding():
    return '保存任务列表时使用编码：'
def settingdlg_checkbox_cwov():
    return '与旧版本兼容'
def settingdlg_staticbox_checkresult():
    return '校验结果'
def settingdlg_checkresult_encoding():
    return '导出校验结果时使用编码：'
def settingdlg_btn_restore():
    if platform.system() == 'Darwin':
        return '恢复默认设置'
    else:
        return '恢复默认设置(&R)'
def settingdlg_page_files():
    return '文件'
def settingdlg_staticbox_language_setting():
    return '语言设置'
def settingdlg_page_language():
    return '语言'
def settingdlg_language_auto():
    return '自动'
def settingdlg_language_error_notinstalled():
    return '未安装该语言包。'
def settingdlg_language_error_signature_failure():
    return '无法验证语言包签名。'
def settingdlg_language_error_failure():
    return '无法切换语言。'
def settingdlg_error_ascr_invaild():
    return '设置项"自动保存校验结果"无效。'
def settingdlg_warning_save():
    return '要保存更改的设置吗？'
def settingdlg_warning_changelang():
    return '切换语言需要清空列表。\n要立即更改语言，请单击“是(Y)”；要在下次启动时使用新语言，请单击“否(N)”。'
def settingdlg_warning_changelang_later(lang:str):
    return '下次启动软件时将使用语言：\n' + lang
def checksumdlg_title_add():
    return '添加校验和'
def checksumdlg_title_edit():
    return '编辑校验和'
def checksumdlg_checksum_type(l:list):
    if l:
        return '校验和类型：' + ' 或 '.join(map(str, l))
    else:
        return '校验和类型：未知'
def aboutdlg_title():
    return '关于'
def aboutdlg_software_name(arch: str):
    return title() + ' ' + arch
def aboutdlg_version(ver: tuple):
    return '版本：' + '.'.join(map(str, ver))
def aboutdlg_build(build: str):
    return '构建版本：' + build
def aboutdlg_pyver(ver: str):
    return 'Python 版本：' + ver
def aboutdlg_wxpyver(ver: str):
    return 'wxPython 版本：' + ver
def aboutdlg_language():
    return '本地化：' + AUTHOR
def aboutdlg_open_source_declaration(license):
    return '本软件使用 ' + license + ' 开源。'
def calcdlg_title(count=None):
    if count is None:
        return '校验和计算'
    else:
        return '(' + str(count[0]) + '/' + str(count[1]) + ') 校验和计算'
def calcdlg_elapsed_time():
    return '已用时间：'
def calcdlg_file():
    return '文件: '
def calcdlg_size():
    return '大小：'
def calcdlg_speed():
    return '速度：'
def calcdlg_progress():
    return '进度：'
def calcdlg_overall_progress():
    return '总进度：'
def calcdlg_str_bytes():
    return '字节'
def calcdlg_warning_cancel():
    return '你确定要取消吗？'
def calcdlg_btn_pause():
    if platform.system() == 'Darwin':
        return '暂停'
    else:
        return '暂停(&P)'
def calcdlg_btn_continue():
    if platform.system() == 'Darwin':
        return '继续'
    else:
        return '继续(&C)'
def encodingpickerdlg_title(file:str=''):
    if file:
        return '打开文本文档 - ' + file
    else:
        return '打开文本文档'
def encodingpickerdlg_hint():
    return '请选择文本文档使用的编码。'
def encodingpickerdlg_preview():
    return '预览：'
def detailsdlg_title():
    return '详细信息'
def detailsdlg_file():
    return '文件：'
def detailsdlg_checksum():
    return '校验和：'
def detailsdlg_expected_checksum():
    return '预期校验和：'
def detailsdlg_time():
    return '计算耗时：'
def detailsdlg_error():
    return '错误信息：'
def detailsdlg_actual_checksum():
    return '实际校验和：'
def detailsdlg_none():
    return '<无>'
def itemdlg_title():
    return '添加项目'
def itemdlg_file():
    return '文件：'
def itemdlg_expected_checksum():
    return '预期校验和：'
def itemdlg_checksum_type_title():
    return '校验和类型：'
def itemdlg_checksum_type(l:list):
    if l:
        return ' 或 '.join(map(str, l))
    else:
        return '未知'
def itemdlg_invalid_file_error(file:str=''):
    return '无效的文件：' + file
def opentaskdlg_title():
    return '导入任务列表'
def opentaskdlg_hint():
    return '粘贴或从文件加载任务列表。'
def opentaskdlg_loadfile():
    if platform.system() == 'Darwin':
        return '加载文件…'
    else:
        return '加载文件(&F)…'
def opentaskdlg_loadfile_wildcard():
    return '所有支持的文件 (*.md5; *.sha; *.sha1; *.sha256; *.txt)|*.md5; *.sha; *.sha1; *.sha256; *.txt|文本文档 (*.txt)|*.txt|所有文件 (*.*)|*.*'
def otadlg_title():
    return '软件更新'
def otadlg_software_name(arch: str):
    return title() + ' ' + arch
def otadlg_current_ver(ver: tuple):
    return '当前版本：' + '.'.join(map(str, ver))
def otadlg_lastest_ver(ver: tuple):
    if ver:
        return '最新版本：' + '.'.join(map(str, ver))
    else:
        return '最新版本：'
def otadlg_btn_check():
    if platform.system() == 'Darwin':
        return '检查'
    else:
        return '检查(&C)'
def otadlg_btn_update():
    if platform.system() == 'Darwin':
        return '更新'
    else:
        return '更新(&U)'
def otadlg_md_checking():
    return '正在检查更新…'
def otadlg_connecting():
    return '连接中…'
def otadlg_progress(progress: str, speed:str, eta: str):
    return '下载进度：' + progress + '% (' + speed + 'B/s, 剩余：' + eta + ')'
def otadlg_patch_size(size: str):
    return '补丁包大小：' + size
def otadlg_full_size(size: str):
    return '完整包大小：' + size
def otadlg_verifying(progress: str):
    return '正在校验：' + progress + '%'
def otadlg_verification_error():
    return '更新文件校验错误，请检查网络连接。'
def otadlg_md_failure():
    return '无法获取更新，请稍后再试。'

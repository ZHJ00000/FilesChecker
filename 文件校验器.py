#Copyright ©2022 ZHJ. All Rights Reserved.
'''
Variables Dictionary：
alg:选择的算法
size:文件大小
data:多种用途：校验源来源（文件地址或手动输入哈希值），文件地址，手动输入的哈希值
fah(列表):文件和哈希值
foh(列表):文件和哈希值判断
path:输入到计算部分的文件地址
hashs(列表):哈希值
group…:校验结果
tf:布尔值
timestart:计算哈希开始时间
timeend:计算哈希结束时间
errorfahlist:fah和foh中错误的文件地址列表序号
dispargv:显示参数
l(列表):列表文件数据
foha:校验源类型
'''
import os
import hashlib
import time
import sys
import getopt
import glob
os.system('')
exitcode = 0
print('\033[33m文件校验器 v2.3.1\033[0m')
print('\033[33mCopyright ©2022 ZHJ. All Rights Reserved.\033[0m')
print()
fah = []
foh = []
foha = ''
del sys.argv[0]
def progressbar(name,progress):
    progress = float('%.4f' % progress)
    print('\r' + name + '[' + '>'*int(progress*100//2) + '-'*(50-int(progress*100//2)) + ']' + str('%.2f' % (progress*100)) + '%',end='')
# Start:Code from"https://blog.zeruns.tech/archives/582.html",edited
def filehash(path, algorithm, name):
    size = os.path.getsize(path)  # 获取文件大小，单位是字节（byte）
    size1 = size
    with open(path, 'rb') as f:  # 以二进制模式读取文件
        while size >= 1024 * 1024:  # 当文件大于1MB时将文件分块读取
            algorithm.update(f.read(1024 * 1024))
            size -= 1024 * 1024
            progress = ((size1 - size)/size1)
            progressbar(name,progress)
        algorithm.update(f.read())
    return(algorithm.hexdigest())  # 输出计算结果
# End:Code from"https://blog.zeruns.tech/archives/582.html",edited
def check():
    global fah, foh, exitcode
    print('\033[0m正在计算哈希值…')
    hashs = []
    errorfahlist = []
    for i in range(0, (len(fah))):
        if foh[i] == 1:
            path = fah[i]
            try:
                timestart = time.time()
                if sys.argv[0] == 'file':
                    if len(fah) == 1:
                        name = ('文件的哈希：')
                    else:
                        name = ('文件' + str(i) + '的哈希：')
                else:
                    name = ('校验源' + str(i) + '的哈希：')
                progressbar(name,0)
                if alg == '1':
                    hashs.append(filehash(path, hashlib.md5(), name))
                elif alg == '2':
                    hashs.append(filehash(path, hashlib.sha1(), name))
                elif alg == '3':
                    hashs.append(filehash(path, hashlib.sha224(), name))
                elif alg == '4':
                    hashs.append(filehash(path, hashlib.sha256(), name))
                elif alg == '5':
                    hashs.append(filehash(path, hashlib.sha384(), name))
                elif alg == '6':
                    hashs.append(filehash(path, hashlib.sha512(), name))
                timeend = time.time()
                t = (timeend - timestart)
                if sys.argv[0] == 'file':
                    if len(fah) == 1:
                        print('\r文件的哈希（计算耗时：' + str('%.2f' % t) + 's）：' + hashs[len(hashs) - 1])
                    else:
                        print('\r' + '文件' + str(i) + '的哈希（计算耗时：' + str('%.2f' % t) + 's）：' + hashs[len(hashs) - 1] + ' '*10)
                else:
                    print('\r' + '校验源' + str(i) + '的哈希（计算耗时：' + str('%.2f' % t) + 's）：' + hashs[len(hashs) - 1] + ' '*10)
            except Exception as err:
                errorfahlist.append(i)
                hashs.append('')
                print('\n\033[31m读取文件"' + path + '"出现错误(' + str(err) + ')。\033[0m')
        elif foh[i] == 2:
            hashs.append(fah[i])
            print('校验源' + str(i) + '的哈希（手动输入）：' + hashs[i])
    if len(errorfahlist) == 0:
        fah = fah
    else:
        ii = len(errorfahlist) - 1
        for i in range(0, len(errorfahlist)):
            del fah[errorfahlist[ii]]
            del foh[errorfahlist[ii]]
            del hashs[errorfahlist[ii]]
            ii = ii - 1
    if len(fah) == 0:
        exitcode = 1
    elif len(fah) == 1:
        if sys.argv[0] == 'file':
            fah = fah
        else:
            print()
            print('由于只添加了1个校验源，不提供校验结果。')
    else:
        group = []
        group.append([hashs[0]])
        if foh[0] == 1:
            group[0].append(fah[0])
        elif foh[0] == 2:
            group[0].append('<' + fah[0] + '>')
        for i in range(1, len(hashs)):
            tf = False
            for ii in range(0, len(group)):
                if hashs[i] == group[ii][0]:
                    if foh[i] == 1:
                        group[ii].append(fah[i])
                    elif foh[i] == 2:
                        group[ii].append('<' + fah[i] + '>')
                    tf = True
                    break
            if tf == False:
                group.append([hashs[i]])
                if foh[i] == 1:
                    group[len(group) - 1].append(fah[i])
                elif foh[i] == 2:
                    group[len(group) - 1].append('<' + fah[i] + '>')
        for i in range(0, len(group)):
            del group[i][0]
        print()
        print('校验结果：')
        for i in range(0, len(group)):
            print('组' + str(i) + '：' + str(group[i]))
if len(sys.argv) != 0:
    dispargv = ''
    for i in range(0,len(sys.argv)):
        if ' ' in sys.argv[i]:
            dispargv = dispargv + ' "' + sys.argv[i] + '"'
        else:
            dispargv=dispargv + ' ' + sys.argv[i]
    print('\033[33m自定义运行参数：' + dispargv + '\033[0m')
    print()
    if sys.argv[0] == 'list':
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hc:", ["help", "encoding="])
        except getopt.GetoptError as err:
            print('\033[31m参数错误：' + str(err) + '\033[0m')
            exitcode = 1
        else:
            for i in range(0,len(opts)):
                opts[i] = list(opts[i])
            if len(opts) == 0 and len(args) == 0:
                tfhelp = True
            else:
                tfhelp = False
                encoding = 'utf-8'
                for i in range(0,len(opts)):
                    if '-h' in opts[i] or '--help' in opts[i]:
                        tfhelp = True
                    else:
                        if '-c' in opts[i] or '--encoding' in opts[i]:
                            encoding = opts[i][1]
            if tfhelp == True:
                print('用法：文件校验器 list [选项] <列表文件地址>\nlist选项：\n  没有参数,-h,--help\t显示帮助。\n  -c,--encoding ENCODING\t设置列表文件编码(默认utf-8)。')
            else:
                try:
                    with open(args[0], 'r', encoding=encoding) as file:
                        l = file.readlines()
                except Exception as err:
                    print('\033[31m读取列表文件出现错误(' + str(err) + ')。\033[0m')
                    exitcode = 1
                    tf = False
                else:
                    for i in range(0,len(l)):
                        l[i] = l[i].rstrip()
                    for i in range(0,len(l)):
                        l[i] = l[i].partition('#')[0]
                    while '' in l:
                        l.remove('')
                    tf = False
                    if len(l) == 0:
                        print('\033[31m列表文件错误：不支持的算法。\033[0m')
                        exitcode = 1
                    else:
                        for i in range(0, len(l)):
                            l[i] = l[i].rstrip()
                        l[0] = l[0].lower()
                        if l[0] == 'md5':
                            alg = '1'
                            tf = True
                        elif l[0] == 'sha1':
                            alg = '2'
                            tf = True
                        elif l[0] == 'sha224':
                            alg = '3'
                            tf = True
                        elif l[0] == 'sha256':
                            alg = '4'
                            tf = True
                        elif l[0] == 'sha384':
                            alg = '5'
                            tf = True
                        elif l[0] == 'sha512':
                            alg = '6'
                            tf = True
                        else:
                            print('\033[31m列表文件错误：不支持的算法。\033[0m')
                            exitcode = 1
                            tf = False
                if tf == True:
                    ll = []
                    for i in range(len(l)):
                        ll.append(l[i].lower())
                    try:
                        if ll[1] != '<file>' and ll[1] != '<hash>':
                            tf = False
                            print('\033[31m列表文件错误：未设置校验源类型。\033[0m')
                            exitcode = 1
                    except IndexError:
                        print('\033[31m列表文件中不含任何可添加校验源。\033[0m')
                        exitcode = 1
                if tf == True:
                    for i in range(1,len(l)):
                        if ll[i] == '<file>':
                            foha = 1
                        elif ll[i] == '<hash>':
                            foha = 2
                        else:
                            foh.append(foha)
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
                                    fah.append(l[i])
                                else:
                                    for i in range(0, len(fs)):
                                        if os.path.isfile(fs[i]) == False:
                                            fs[i] = ''
                                    while '' in fs:
                                        fs.remove('')
                                    fah.extend(fs)
                                    for i in range(1,len(fs)):
                                        foh.append(1)
                            elif foha == 2:
                                l[i] = l[i].lower()
                                fah.append(l[i])
                    if fah == []:
                        print('\033[31m列表文件中不含任何可添加校验源。\033[0m')
                        exitcode = 1
                    else:
                        check()
    elif sys.argv[0] == 'file':
        alg = ''
        try:
            opts, args = getopt.getopt(sys.argv[1:], "ha:", ["help", "algorithm="])
        except getopt.GetoptError as err:
            print('\033[31m参数错误：' + str(err) + '\033[0m')
            exitcode = 1
        else:
            for i in range(0,len(opts)):
                opts[i] = list(opts[i])
            tfhelp = False
            for i in range(0, len(opts)):
                if '-h' in opts[i] or '--help' in opts[i]:
                    tfhelp = True
                else:
                    if '-a' in opts[i] or '--algorithm' in opts[i]:
                        alg = opts[i][1]
            if tfhelp == True:
                print('用法：文件校验器 file [选项] [文件地址]\nfile选项：\n  没有参数,-h,--help\t显示帮助。\n  -a,--algorithm ALGORITHM\t设置算法(必选)。')
            else:
                if alg != '':
                    if alg == 'md5':
                        alg = '1'
                        tf = True
                    elif alg == 'sha1':
                        alg = '2'
                        tf = True
                    elif alg == 'sha224':
                        alg = '3'
                        tf = True
                    elif alg == 'sha256':
                        alg = '4'
                        tf = True
                    elif alg == 'sha384':
                        alg = '5'
                        tf = True
                    elif alg == 'sha512':
                        alg = '6'
                        tf = True
                    else:
                        print('\033[31m参数错误：不支持的哈希算法。\033[0m')
                        exitcode = 1
                        tf = False
                    if len(args) >= 1 and tf == True:
                        for i in range(0,len(args)):
                            fs = glob.glob(args[i])
                            if len(fs) == 0:
                                fah.append(args[i])
                                foh.append(1)
                            else:
                                for i in range(0,len(fs)):
                                    if os.path.isfile(fs[i]) == False:
                                        fs[i] = ''
                                while '' in fs:
                                    fs.remove('')
                                fah.extend(fs)
                                for i in range(0,len(fs)):
                                    foh.append(1)
                        check()
                    elif len(args) == 0:
                        print('用法：文件校验器 file [选项] [文件地址]\nfile选项：\n  没有参数,-h,--help\t显示帮助。\n  -a,--algorithm ALGORITHM\t设置算法(必选)。')
                else:
                    print('\033[31m参数错误：未指定参数：-a,--algorithm\033[0m')
                    exitcode = 1
                    print('用法：文件校验器 file [选项] [文件地址]\nfile选项：\n  没有参数,-h,--help\t显示帮助。\n  -a,--algorithm ALGORITHM\t设置算法(必选)。')
    elif sys.argv[0] == 'help' or sys.argv[0] == '-h' or sys.argv[0] == '--help':
        print('用法：文件校验器 <命令> [选项]\n命令：\n  没有命令\t使用交互模式。\n  help\t显示帮助。\n  list\t导入列表文件并校验。\n  file\t直接输入文件地址并校验。\n一般选项：\n  -h,--help\t显示帮助。')
    else:
        print('\033[31m不支持的命令。\033[0m')
        exitcode = 1
else:
    sys.argv.append('default')
    while 1:
        alg = str(input('\033[0m请选择算法[MD5(1)/SHA1(2)/SHA224(3)/SHA256(4)/SHA384(5)/SHA512(6)]：\033[32m'))
        if alg == '1' or alg == '2' or alg == '3' or alg == '4' or alg == '5' or alg == '6':
            break
    while 1:
        while 1:
            if len(fah) == 0:
                data = str(input('\033[0m请选择校验源0的类型[文件(1)/哈希值(2)]：\033[32m'))
                if data == '1' or data == '2':
                    break
            else:
                data = str(input('\033[0m请选择校验源' + str(len(fah)) + '的类型[停止添加并开始校验(0)/文件(1)/哈希值(2)]：\033[32m'))
                if data == '0' or data == '1' or data == '2':
                    break
        if data == '0':
            break
        elif data == '1':
            foh.append(1)
            while 1:
                data = str(input('\033[0m请输入文件地址：\033[32m'))
                if len(data) != 0:
                    if data[0] == '"' and data[len(data) - 1] == '"':
                        data1 = list(data)
                        del data1[0]
                        del data1[len(data1) - 1]
                        data = ''
                        for i in range(len(data1)):
                            data = data + data1[i]
                tf = os.path.isfile(data)
                if tf == True:
                    break
                elif tf == False:
                    tf = os.path.isdir(data)
                    if tf == True:
                        print('\033[31m不允许导入文件夹。\033[0m')
                    elif tf == False:
                        print('\033[31m找不到文件。\033[0m')
            fah.append(data)
        elif data == '2':
            foh.append(2)
            data = str(input('\033[0m请输入哈希值：\033[32m'))
            data = data.lower()
            fah.append(data)
    print()
    check()
print()
input('\033[0m按 Enter 退出程序。\033[32m')
print('\033[0m',end='')
sys.exit(exitcode)

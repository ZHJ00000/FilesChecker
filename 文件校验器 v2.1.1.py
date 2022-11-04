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
os.system('')
print('\033[33m文件校验器 v2.1.1\033[0m')
print('\033[33mCopyright ©2022 ZHJ. All Rights Reserved.\033[0m')
print()
fah = []
foh = []
foha = ''
del sys.argv[0]
def listlocate(list,Element):
    tf = False
    for i in range(0,len(list)):
        if list[i] == Element:
            tf = True
            return(i)
            break
    if tf == False:
        return(-1)
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
def cheak():
    global fah, foh
    print('\033[0m正在计算哈希值…')
    hashs = []
    errorfahlist = []
    for i in range(0, (len(fah))):
        if foh[i] == 1:
            path = fah[i]
            try:
                timestart = time.time()
                if lowerargv[0] == 'file':
                    name = ('文件的哈希：')
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
                if lowerargv[0] == 'file':
                    print('\r文件的哈希（计算耗时：' + str('%.2f' % t) + 's）：' + hashs[len(hashs) - 1])
                else:
                    print('\r校验源' + str(i) + '的哈希（计算耗时：' + str('%.2f' % t) + 's）：' + hashs[len(hashs) - 1])
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
        for i in range(0, len(errorfahlist)):
            del fah[errorfahlist[i]]
            del foh[errorfahlist[i]]
            del hashs[errorfahlist[i]]
    if len(fah) == 0:
        fah = fah
    elif len(fah) == 1:
        if lowerargv[0] == 'file':
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
lowerargv = []
if len(sys.argv) != 0:
    dispargv = ''
    for i in range(0,len(sys.argv)):
        if ' ' in sys.argv[i]:
            dispargv = dispargv + ' "' + sys.argv[i] + '"'
        else:
            dispargv=dispargv + ' ' + sys.argv[i]
    print('\033[33m自定义运行参数：' + dispargv + '\033[0m')
    print()
    for i in range(0,len(sys.argv)):
        lowerargv.append(sys.argv[i].lower())
    if lowerargv[0] == 'list':
        if len(sys.argv) != 1:
            tf = os.path.isfile(sys.argv[1])
            if tf == True:
                try:
                    with open(sys.argv[1], 'r', encoding='utf-8') as file:
                        l = file.readlines()
                except Exception as err:
                    print('\033[31m读取列表文件出现错误(' + str(err) + ')。\033[0m')
                else:
                    for i in range(0,len(l)):
                        l[i] = l[i].rstrip()
                    for i in range(0,len(l)):
                        l[i] = l[i].partition('#')[0]
                    while '' in l:
                        l.remove('')
                    if len(l) == 0:
                        print('\033[31m列表文件中指定了不支持的算法。\033[0m')
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
                            print('\033[31m列表文件中指定了不支持的算法。\033[0m')
                            tf = False
            elif tf == False:
                print('\033[31m找不到列表文件。\033[0m')
            if tf == True:
                ll = []
                for i in range(len(l)):
                    ll.append(l[i].lower())
                if ll[1] != '<file>' and ll[1] != '<hash>':
                    tf = False
                    print('\033[31m未设置校验源类型。\033[0m')
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
                        elif foha == 2:
                            l[i] = l[i].lower()
                        fah.append(l[i])
                cheak()
        else:
            print('\033[31m找不到列表文件。\033[0m')
    elif lowerargv[0] == 'file':
        if len(sys.argv) != 1:
            if lowerargv[1] == 'md5':
                alg = '1'
                tf = True
            elif lowerargv[1] == 'sha1':
                alg = '2'
                tf = True
            elif lowerargv[1] == 'sha224':
                alg = '3'
                tf = True
            elif lowerargv[1] == 'sha256':
                alg = '4'
                tf = True
            elif lowerargv[1] == 'sha384':
                alg = '5'
                tf = True
            elif lowerargv[1] == 'sha512':
                alg = '6'
                tf = True
            else:
                print('\033[31m参数中指定了不支持的算法。\033[0m')
                tf = False
            if len(sys.argv) != 2 and tf == True:
                foh.append(1)
                fah.append(sys.argv[2])
                cheak()
            elif len(sys.argv) == 2:
                print('\033[31m找不到文件。\033[0m')
        else:
            print('\033[31m参数中指定了不支持的算法。\033[0m')
    else:
        print('\033[31m不支持的参数。\033[0m')
else:
    sys.argv.append('default')
    lowerargv.append('default')
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
    cheak()
print()
input('\033[0m按 Enter 退出程序。\033[32m')
print('\033[0m')

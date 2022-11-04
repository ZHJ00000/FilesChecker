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
t:计算耗时
errorfahlist:fah和foh中错误的文件地址列表序号
'''
import os
import hashlib
import time
os.system('')
print('\033[33m文件校验器 v1.4\033[0m')
print('\033[33mCopyright ©2022 ZHJ. All Rights Reserved.\033[0m')
print()
fah=[]
foh=[]
#Start:Code from"https://blog.zeruns.tech/archives/582.html",changed
def calculation(path, algorithm):
    global start, end  # 声明全局变量
    timestart = time.time()
    size = os.path.getsize(path)  # 获取文件大小，单位是字节（byte）
    with open(path, 'rb') as f:  # 以二进制模式读取文件
        while size >= 1024 * 1024:  # 当文件大于1MB时将文件分块读取
            algorithm.update(f.read(1024 * 1024))
            size -= 1024 * 1024
        algorithm.update(f.read())
    hashs.append(algorithm.hexdigest())  # 输出计算结果
    timeend = time.time()
    t = (timeend - timestart)
    print('校验源' + str(i) + '的哈希（计算耗时：' + str('%.2f' % t) +'s）：' + hashs[len(hashs)-1])
#End:Code from"https://blog.zeruns.tech/archives/582.html",changed
while 1:
    alg = str(input('\033[0m请选择算法[MD5(1)/SHA1(2)/SHA224(3)/SHA256(4)/SHA384(5)/SHA512(6)]：\033[32m'))
    if alg == '1' or alg == '2' or alg == '3' or alg == '4' or alg == '5' or alg == '6' :
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
            data = str(input('\033[0m请输入文件地址（前后添加引号将无法读取）：\033[32m'))
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
print('\033[0m正在计算哈希值…')
hashs = []
errorfahlist = []
i = 0
for i in range(0,(len(fah))):
    if foh[i] == 1:
        path = fah[i]
        tf = os.path.isfile(path)
        if tf == True:
            try:
                if alg == '1':
                    calculation(path, hashlib.md5())
                elif alg == '2':
                    calculation(path, hashlib.sha1())
                elif alg == '3':
                    calculation(path, hashlib.sha224())
                elif alg == '4':
                    calculation(path, hashlib.sha256())
                elif alg == '5':
                    calculation(path, hashlib.sha384())
                elif alg == '6':
                    calculation(path, hashlib.sha512())
            except OSError:
                errorfahlist.append(i)
                print('\033[31m读取文件"' + path + '"出现错误(OSError)。\033[0m')
        elif tf == False:
            errorfahlist.append(i)
            print('\033[31m找不到文件"' + path + '"。\033[0m')
    elif foh[i] == 2:
        hashs.append(fah[i])
        print('校验源' + str(i) + '的哈希（手动输入）：' + hashs[i])
if len(errorfahlist) == 0:
    fah = fah
else:
    i = 0
    for i in range(0,len(errorfahlist)):
        del fah[errorfahlist[i]]
        del foh[errorfahlist[i]]
if len(fah) == 0:
    fah = fah
elif len(fah) == 1:
    print()
    print('由于只添加了1个校验源，不提供校验结果。')
else:
    group = []
    group.append([hashs[0]])
    if foh[0] == 1:
        group[0].append(fah[0])
    elif foh[0] == 2:
        group[0].append('<' + fah[0] + '>')
    i = 0
    for i in range(1, len(hashs)):
        ii = 0
        tf = False
        for ii in range(0,len(group)):
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
    i = 0
    for i in range(0, len(group)):
        del group[i][0]
    print()
    print('校验结果：')
    i = 0
    for i in range(0, len(group)):
        print('组' + str(i) + '：' + str(group[i]))
print()
input('\033[0m按 Enter 退出程序。\033[32m')
print('\033[0m')

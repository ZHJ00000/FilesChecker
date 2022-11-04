#Copyright ©2022 ZHJ. All Rights Reserved.
'''
Variables Dictionary：
alg:选择的算法
size:文件大小
data:多种用途：比较源来源（文件地址或手动输入哈希值），文件地址，手动输入的哈希值
fah(列表):文件和哈希值
foh(列表):文件和哈希值判断
path:输入到计算部分的文件地址
hashs(列表):哈希值
group…:比较结果
tf:判断文件是否为真返回的结果（布尔值）
'''
import os
import hashlib
fah=[]
foh=[]
#Start:Code from"https://zhuanlan.zhihu.com/p/168608305",changed
def calculation(path, algorithm):
    global start, end  # 声明全局变量
    size = os.path.getsize(path)  # 获取文件大小，单位是字节（byte）
    with open(path, 'rb') as f:  # 以二进制模式读取文件
        while size >= 1024 * 1024:  # 当文件大于1MB时将文件分块读取
            algorithm.update(f.read(1024 * 1024))
            size -= 1024 * 1024
        algorithm.update(f.read())
    hashs.append(algorithm.hexdigest())  # 输出计算结果
    print('比较源' + str(len(hashs)-1) + '的哈希：' + hashs[len(hashs)-1])
#End:Code from"https://zhuanlan.zhihu.com/p/168608305",changed
print('此工具可以通过多种算法比较文件是否一致。')
print('最多可添加10个比较源。')
while 1:
    alg = str(input('请选择算法[MD5(1)/SHA1(2)/SHA256(3)]：'))
    if alg == '1' or alg == '2' or alg == '3':
        break
while 1:
    data = str(input('请选择比较源0的来源[文件地址(1)/手动输入哈希值(2)]：'))
    if data == '1' or data == '2':
        break
if data == '1':
    foh.append(1)
    while 1:
        data = str(input('请输入文件地址（前后添加引号将无法读取）：'))
        tf = os.path.exists(data)
        if tf == True:
            break
        elif tf == False:
            print('输入的文件地址无效。')
    fah.append(data)
elif data == '2':
    foh.append(2)
    while 1:
        data = str(input('请输入哈希值：'))
        if data != '*':
            break
    data = data.lower()
    fah.append(data)
while 1:
    data = str(input('请选择比较源1的来源[文件地址(1)/手动输入哈希值(2)]：'))
    if data == '1' or data == '2':
        break
if data == '1':
    foh.append(1)
    while 1:
        data = str(input('请输入文件地址（前后添加引号将无法读取）：'))
        tf = os.path.exists(data)
        if tf == True:
            break
        elif tf == False:
            print('输入的文件地址无效。')
    fah.append(data)
elif data == '2':
    foh.append(2)
    while 1:
        data = str(input('请输入哈希值：'))
        if data != '*':
            break
    data = data.lower()
    fah.append(data)
while 1:
    while 1:
        data = str(input('请选择比较源'+str(len(fah))+'的来源[停止添加比开始比较(0)/文件地址(1)/手动输入哈希值(2)]：'))
        if data == '0' or data == '1' or data == '2':
            break
    if data == '0':
        break
    if data == '1':
        foh.append(1)
        while 1:
            data = str(input('请输入文件地址（前后添加引号将无法读取）：'))
            tf = os.path.exists(data)
            if tf == True:
                break
            elif tf == False:
                print('输入的文件地址无效。')
        fah.append(data)
        if len(fah) == 10:
            print('已输入10个比较源。')
            break
    elif data == '2':
        foh.append(2)
        while 1:
            data = str(input('请输入哈希值：'))
            if data != '*':
                break
        data = data.lower()
        fah.append(data)
        if len(fah) == 10:
            print('已输入10个比较源。')
            break
print('正在计算哈希值…')
hashs = []
i = 0
for i in range(0,(len(fah))):
    if foh[i] == 1:
        path = fah[i]
        if alg == '1':
            calculation(path, hashlib.md5())
        elif alg == '2':
            calculation(path, hashlib.sha1())
        elif alg == '3':
            calculation(path, hashlib.sha256())
    elif foh[i] == 2:
        hashs.append(fah[i])
        print('比较源' + str(i) + '的哈希：' + hashs[i])
group0 = ['*']
group0[0] = (hashs[0])
group1 = ['*']
group2 = ['*']
group3 = ['*']
group4 = ['*']
group5 = ['*']
group6 = ['*']
group7 = ['*']
group8 = ['*']
group9 = ['*']
group0.append(fah[0])
i=0
for i in range(0,len(hashs)):
    if hashs[i] == group0[0]:
        group0.append(fah[i])
    elif hashs[i] == group1[0]:
        group1.append(fah[i])
    elif hashs[i] == group2[0]:
        group2.append(fah[i])
    elif hashs[i] == group3[0]:
        group3.append(fah[i])
    elif hashs[i] == group4[0]:
        group4.append(fah[i])
    elif hashs[i] == group5[0]:
        group5.append(fah[i])
    elif hashs[i] == group6[0]:
        group6.append(fah[i])
    elif hashs[i] == group7[0]:
        group7.append(fah[i])
    elif hashs[i] == group8[0]:
        group8.append(fah[i])
    elif hashs[i] == group9[0]:
        group9.append(fah[i])
    else:
        if group1[0] == '*':
            group1[0] = (hashs[i])
            group1.append(fah[i])
        elif group2[0] == '*':
            group2[0] = (hashs[i])
            group2.append(fah[i])
        elif group3[0] == '*':
            group3[0] = (hashs[i])
            group3.append(fah[i])
        elif group4[0] == '*':
            group4[0] = (hashs[i])
            group4.append(fah[i])
        elif group5[0] == '*':
            group5[0] = (hashs[i])
            group5.append(fah[i])
        elif group6[0] == '*':
            group6[0] = (hashs[i])
            group6.append(fah[i])
        elif group7[0] == '*':
            group7[0] = (hashs[i])
            group7.append(fah[i])
        elif group8[0] == '*':
            group8[0] = (hashs[i])
            group8.append(fah[i])
        elif group9[0] == '*':
            group9[0] = (hashs[i])
            group9.append(fah[i])
print('比较结果：')
del group0[0]
del group0[0]
del group1[0]
del group2[0]
del group3[0]
del group4[0]
del group5[0]
del group6[0]
del group7[0]
del group8[0]
del group9[0]
print('组0：'+str(group0))
if len(group1)!=0:
    print('组1：' + str(group1))
if len(group2)!=0:
    print('组2：' + str(group2))
if len(group3)!=0:
    print('组3：' + str(group3))
if len(group4)!=0:
    print('组4：' + str(group4))
if len(group5)!=0:
    print('组5：' + str(group5))
if len(group6)!=0:
    print('组6：' + str(group6))
if len(group7)!=0:
    print('组7：' + str(group7))
if len(group8)!=0:
    print('组8：' + str(group8))
if len(group9)!=0:
    print('组9：' + str(group9))
input('报告生成完毕，按 Enter 退出程序。')
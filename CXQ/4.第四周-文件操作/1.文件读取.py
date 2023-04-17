"""
文件:命名:文件名字.扩展名  例如:写python.py文件, .txt普通文本, ,doc(word文档), .csv, .xlsx, .ppt   window系统会根据文件名字的后缀来确定当前文件类型
文本文件：写入的给用户看，以ASCII码存储的文件
二进制文件：给计算机看
ASCII码：使用八位二进制，对键盘的字母，数字，符号进行了编码，转换成二进制
utf-8：编码字符集，国家统一，对全国的文字进行了编码，  # -*- coding: ut-8 -*-  指定当前py文件为utf-8
GBK/gb2312:国标
file:是python语言的一个对象，可以通过open()打开文件进行操作
"""
# UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 4: illegal multibyte sequence
# open():用来打开文件，会返回一个文件对象；第一个参数file：文件的路径（绝对路径和相对路径），第二个参数encoding：设置打开文本的编码字符集，默认使用gbk
# f:操作句柄，用来操作文件的内容，可以查看表数据，可以添加数据
f = open(file=r"静夜思.txt", encoding="utf-8")
# read():方法，属于文件对象，读取文件中所有的数据，返回一个长字符串
string = f.read()
print(string)
# 将这个长字符串处理一下，将字符串里面的题目拿到然后作为字典的键，后边诗句作为字典的值
# string = string.replace("\n", "")
# print(string[:3])
# dict1 = {}
# dict1[string[:3]] = string[:3]
# print(dict1)
# 将字符串，题目做键，每一句诗放入列表中
list1 = string.split("\n")
print(list1)
dict2 = {}
dict2[list1[0]] = list1[1:]
print(dict2)
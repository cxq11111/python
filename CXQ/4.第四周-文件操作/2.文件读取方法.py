# open():默认使用     模式是r，叫做只读模式
f = open("静夜思.txt",encoding="utf-8")
# 1.read():读取文本所有数据，从光标的位置往后读取到末尾
all = f.read()
print(all)
# 2.readable():结果是布尔值，True能读取数据
res = f.readable()
print(res)
# 3.seek():移动光标，参数offset：是相对于指定位置的字节（注意：字母数字英文占一个字节，汉字占三个字节，utf-8字符集）偏移量；参数whence：表示所指定的位置，默认为0是文件开始位置，值为1是相对文件的读写位置，值为2是文件的结尾位置
s = f.seek(3)
print(s)
# 3.readline():读取一行数据，从光标所在的行读取一行数据，只读取一行数据，光标往后
line = f.readline()
print(line)
# 4.readlines():从光标开始读取数据，每一行都拿到，放在列表中，光标往后
f.seek(0)
lines = f.readlines()
print(lines)
# 5.tell():告诉你光标的位置
print(f.tell())
"""
# 练习: 在文件login.txt中添加一些账号密码 例如: zhangsan-123465
# 1. 打开文件, 将所有的账号拿到
# 2.设置闰年判断程序.py 键盘输入账号, 判断是否在文件中
"""
# zhangsan-123456
# lisi123-123456
# root123-zhangsan
# root000-www.baidu
fuser = open("login.txt", encoding="utf-8")
print(fuser.read())
i = f.readable()
print(i)
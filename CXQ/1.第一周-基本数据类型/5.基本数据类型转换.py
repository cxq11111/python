# 基本数据类型 ：int-整型，str-字符串，float-浮点型，bool-布尔型
# 1.str(),函数，将数据转换成字符串
intl = 10000
print(intl,type(intl))
sl = str(intl)
print(sl,type(sl))
# 将float转化成str
fl = 5.235
print(fl,type(fl))
s2 =str(fl)
print(s2,type(s2))
# Ture
print(str(True),type(str(True)))
# True 转化字符串，相当于"True"
print(str(True),type(str(True)))
# 2。int()，函数，将数据转化为整型
# 将float 转化成int，取整数位，在一定范围内适用
f2 = 8.99999999
il = int(f2)
print(il,type(il))
# 将str转化为int,当字符串是纯数字的时候可以转换int
strl = "98266"
i2 = int(strl)
print(i2,type(i2))
# ValueError:  invalid literal for int() with base10:' j456789'
# value: 值，error:错误
#str2 = "j456789"
# i3 = int(str2)
#print(i3,type(i3))
#将bool转化成int
fa = False
i4 = int(fa)
print(i4,type(i4))
# 3.float(),函数数据转化为float型
# int转化成float，带上小数点
print(float(890),type(float(890)))
# str转化成float
print(float("5.666"),type(float(5.666)))
print(float("5"),type(float("5")))
# 4.bool():函数，可以将其他数据转化为布尔值
# 字符串如果是" " 相当于Flase，长度大于0是True
string = ""
print(bool(string))
# len（）：可以计算字符串长度
print(len(string))
# int转化为bool值，只有0.0是False,其他都是True
f100 = -1.23
print(bool(f100))
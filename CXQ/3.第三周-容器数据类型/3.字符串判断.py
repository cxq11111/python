"""
format():拼接字符串
"""
# 1.拼接字符串
name = "曹操"
say = "挟天子以令诸侯"
print("姓名:{0} 主要事迹:{1}".format(name, say))
print("姓名:{n} 主要事迹:{m}".format(n=name, m=say))
print(f"姓名：{name} {say}")
# 拼接字符串
yi = 1.08
# .4f:保留浮点数后四位
print(f"补税:{yi:.4f}")
# 带符号 +
print(f"补税：{13.5:+.2f}")
# 不带小数点，四舍五入
print(f"{6.462864:.0f}")
# 拼接字符串，10d，占10个位置
age = 78
print(f"年龄：{age:10d}")
# 位数不够前面补0
print(f"年龄:{age:0>5}")
print(f"年龄:{age:*<5}")
# 百分数格式化
GDP = 0.1516
print(f"国内生产总值：{GDP:.2%}")
# 调位置
print(f"{name:>10}")
print(f"{name:<10}")
print(f"{name:^10}")
# 三角形
n = 10
for i in range(1, n, 2):
    s = "*" * i
    print(f"{s:^{n}}")
# 判断字符串
string = "abcdefg"
# 1.isalpha():判断是否为纯字母，是纯字母结果为True，否则为False
if string.isalpha():
    print("纯字母")
# 2.isdigit():判断是否为纯数字，是纯数字结果为True，否则为False
str2 = "123456"
if str2.isdigit():
    print("纯数字")
# 3.isalnum():判断字符串是否符号，没有符号为True，有符号为False
str3 = "abc123@汉字"
if str3.isalnum():
    print("是")
else:
    print("不是")
# 4.isupper():判断是否全部字母为大写
str4 = "ABCDEF"
if str4.isupper():
    print("都是大写")
# 5.islower():判断是否全部字母为小写
str5 = "acdh"
if str5.islower():
    print("都是小写")


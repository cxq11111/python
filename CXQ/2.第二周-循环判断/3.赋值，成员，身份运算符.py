name = "赋值符号"
a = 100
a += 1 # 相当于a = a + 1
print(a)
b = 8
b -= 10 # 相当于 b = b - 10
print(b)
a *= 10 # 相当于 a = a * 10
print(a)
b /= 2 # b = b / 2
print(b)
c = 9
c %= 4 # c = c % 4
print(c)
c //= 2   # c = c// 2
print(c)
y = 2
y **= 10 # y = y** 10
print(y)
"""
成员符号：in 在里面， not in 不在里面
"""
# 字符串： 是一种容器，"abc","a"是其中的一个元素
if "a" in "abc":
    print("在字符串内")
# 列表：是一种容器，["str",100,1.1,True],里面可以放任何类型数据
if 100 in ["str",100,1.1,True]:
    print("列表中有100")
# not in：不在里面
if False not in ["str",100,1.1,True]:
    print("确实没有在里面")
"""
身份运算符：is 是     is not 不是
is 主要是判断内存地址是否相等，是否是同一个数据
== 主要是判断数据的大小是否相同，类型不同不相等，但是 True == 1，False==0
"""
n = 100
m = 100
h = "100"
print("-----------------")
print(n is m)        # 正确
print(int(h) is m)
print(n == m)
i =int(input("请输入100: "))   # 这里的h有"100"成为int类型100
print("--------------------")
print(id(m),id(i))
print(i is m)
print(i == m)
print("-------------------")

x = 500
y = "500"
print(id(x),id(int(y)))
print(x is int(y))
"""
for x in range(100,999):
    y = str(x)
    if x is int(y):
        print(f"{x}地址与字符串转换的相同")
    else:
        print("-----")
"""

# 256
a = 257
b = "257"
b = int(b)
print(a is b)

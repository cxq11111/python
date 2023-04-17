"""
1.算数运算符：+加  -减  *乘  /除  **幂  //整除  %求余
"""

# 1 + 1 表达式
print(1+1)
n = 9 - 2
print(n)
print(78*87)
# /除法计算的结果是浮点数
print(998/5)
print(10/2)
# m**n : m的n次方
print(2**10)
# 5 // 3:整除只要整数部分
print(5//3)
# %:整除后取余数
print(5%2)
# 所有偶数（0）对2取余数结果是0
# 所有基数对2取余数结果是1
print(8 % 2)
"""
2.关系运算符（比较运算符）： == 比较左右两边相等，数值上的相等
> 大于    < 小于    <= 小于等于    >= 大于等于    != 不等于
比较运算符形成的表达式结果是布尔值：True，False
"""
print(2>20)
print(2 >= 2)     # 相当于 2=2 或者 2>2
print(True == 1)
print("小明" != "小明")
print("小明" != "大明")
print(1 ==1.0)
print(1 == "1")
"""
逻辑运算符：and 逻辑与， or 逻辑或， not， 逻辑非
"""
print("------------逻辑运算符---------------")
# and：将两个表达式的结果（布尔值）进行计算，当同时为True结果为True 有一个为False就为False
print(True and False)
print(True and True)
print(1 == 1 and 2 > 10)
# or: 当两个表达式其中一个成立（True）结果为True，都不成立结果为False
print(True or False)
print(True or True)
print(1 < 0 or 9 == 20 )
# not:与原来的条件相反，比如:a < 20,那么 not a < 20 相当于 a >= 20
print(not 1 == 0)
print(not True)
print(not False)
"""
内置函数:print(), type(), int(), len(), str(), bool(), float(), sum(), max(), min()...
函数:实现某些功能，把实现功能的代码封装起来
自定义函数:函数相当于爆米花的炉子，参数相当于玉米粒，糖，油，返回值(return)相当于爆米花
def:定义函数的关键字
def 函数名()                 -- 函数名，参数放入括号中
    函数体                   -- 函数体必须缩进在函数中
    return                   -- 返回值
函数名()                     -- 调用函数
函数名命名规则:字母数字下划线，不能数字开头，不能与关键字冲突，不与内置函数冲突，见名知意
"""
# 1.定义函数，实现输出
def pt():
    print("周杰伦, i love you")
# 调用函数
pt()
pt()
# 2.计算123456+98765
def jisuan():
    print(123456+98765)
jisuan()
# 3.函数内定义变量
def chengfa():
    a = 100
    b = 988
    print(a * b)
chengfa()
# 4.函数循环列表
def forlist():
    list1 = [1, 2, 3, 4, 5]
    for l in list1:
        print(list1)
forlist()
# 5.判断星期
def week():
    x = input("输入汉字星期（聪明的人不乱写）: ")
    if x == "星期一":
        print("today is Monday")
    elif x == "星期二":
        print("today is Tuesday")
    elif x == "星期三":
        print("today is Wednesday")
    elif x == "星期四":
        print("today is Thursday")
    elif x == "星期五":
        print("today isFriday")
    else:
        print("today is weekend")
week()
# 练习1: 使用函数打印乘法表, 10 x 10 乘法表
def cf():
    for i in range(1, 11):
        for a in range(1, i+1):
            print(f"{i}x{a}={i*a}", end="\t")
        print("")
cf()
# 练习2: 判断字符串, 输入一个字母判断, 输出该首字母对应的星期/月份英文
def zm():
    x = input("输入星期第一个字母（大写）:")
    if x == "M":
        print("星期一")
    elif x == "T":
        print("星期二或星期四")
        y = input("输入星期第二个字母（小写）:")
        if y == "u":
            print("星期二")
        elif y == "h":
            print("星期四")
    elif x == "W":
        print("星期三")
    elif x == "F":
        print("星期五")
    elif x == "S":
        print("星期六或星期日")
        z = input("输入星期的第二个字母（小写）:")
        if z == "a":
            print("星期六")
        elif z == "u":
            print("星期日")
# zm()
# 练习3: 键盘输入一个三位数, 判断是否为水仙花数
def hua():
    list1 = []
    k = input("输入一个三位数字:")
    k = int(k)
    for j in range(100, 1000):
        a = j // 100
        b = j // 10 % 10
        c = j % 10
        if a ** 3 + b ** 3 + c ** 3 == j:
            list1.append(j)
    if k in list1:
        print("是水仙花数")
    else:
        print("不是水仙花数")
hua()

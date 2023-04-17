"""
返回值:可以是任何数据类型，可以是多个数据，多个数据，逗号隔开
def 函数体(参数):
    函数体
    return 返回值
变量 = 函数名(实参)
"""
# 1.加法函数，返回值是变量
def func1():
    a, b = 9, 21
    c = a + b
    return c
res1 = func1()
print(res1)
# 2.乘法函数，将表达式作为结果返回，返回值是计算的结果
def func2():
    return 10 * 20
res2 = func2()
print(res2)
# 3.返回多个数据，多个类型
def func3():
    string = "小楼昨夜又东风"
    number = 123456
    list1 = [134, 324, 454, 564, 623]
    f = 3.33333333
    return string, number, list1, f
# 多个数据返回，需要多个变量接收，一一对应
a, b, c, d = func3()
print(a, b, c, d)
# 当一个变量接收多个返回值，多个返回值会放入元组中返回
# 如果返回值只有一个数据，该数据类型不变，不会放入元组
t = func3()
print(t)
# 4.元组的取值
# 给一个变量赋值多个数据，结果是放入元组
num = 1, 2, 3
print(num)
# 元组，列表，多个变量接收，结果一一对应取出数据
# a, b, c = (5, 6, 7)
a, b, c = [5, 6, 7]
print(a, b, c)
# 5.传入参数，返回字典
def stu_info(name, age, sex):
    # 放入字典中
    # dict1 = {"姓名": name,"年龄":age,"性别": sex}
    dict1 = dict(name=name, age=age, sex=sex)
    return dict1
res5 = stu_info("张三", 88, "男")
print(res5)
# 6.传入不定长参数，返回字典
def school_info(*args):
    dict1 = {}
    for index, s in enumerate(args):
        dict1[index] = s
    return dict1
res6 = school_info("河艺", "人工智能", "AI2班", "YYDS")
print(res6)
# 7.传入不定长关键字参数
def teacher_info(**kwargs):
    s = ""
    for value in kwargs.values():
        if isinstance(value, int):
            value = str(value)
        s = s + value + ":"
    return s.strip(":")
res7 = teacher_info(name="张广师", age=18, car="雅迪")
print(res7)
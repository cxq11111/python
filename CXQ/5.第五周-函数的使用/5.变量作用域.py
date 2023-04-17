"""
变量作用域: 作用域就是起作用的范围
全局变量: 定义在函数外部, 真个py文件都能够调用;还可使用关键字global改变局部变量为全局变量
局部变量: 定义在函数内部, 只在函数内部起作用,叫做局变量, 函数的参数只在函数内部起作用, 包括在类中定义的变量, 私有属性
"""
name = "乔峰"     # 全局变量
print(name)
def stu(nm):
    """
    :param name: 参数是局部变量
    :return:
    """
    print(name, "全局变量")
    age = 18    # 局部变量
    global sex  # 在函数内部声明为全局变量
    sex = "男"
    print(nm, age, sex)
stu(nm="易烊千玺")
# 在函数外部调用函数内变量
# print(nm)
# print(age, sex)
print(sex)

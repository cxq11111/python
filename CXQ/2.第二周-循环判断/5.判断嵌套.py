"""
if 条件:
    if 条件：
        代码块
    elif 条件：
        代码块
    else：
        代码块
"""
# 先判断天气有没有下雨，如果下雨考虑 打伞还是穿雨衣，没有下雨随意
rain = "暴雨"
if "雨" in rain:
    if rain == "暴雨" or rain == "大雨":
        print("穿上雨衣")
    elif rain == "中雨" or rain == "小雨":
        print("打上雨伞")
    else:
        print("都行")
"""
if 表达式1：
    if 条件：
        代码块
    else：
        代码块
else：
    if 条件：
        代码块
    else：
        代码块
"""
# 定义变量：零花钱 money，先判断钱是否大于1000，大于1000，再判断是否在1000-1500，吃烧鸡，烤鸭，如果是 大于1500，吃大龙虾，大闸蟹
# 在1000以下，1-500之间 吃泡面，馒头，500-1000，大米，面条
# pass 不起任何作用，占位，不让代码块为空报错
money = 1900
if money >= 1000:
    if money > 1500:
        print("吃大龙虾，大闸蟹")
    else:
        print("吃烧鸡，烤鸭")
else:
    if money >= 500:
        print("吃大米，面条")
    else:
        print("吃泡面，馒头")
# 练习1： 定义2个变量，先判断是否为数字类型，int，float如果是，接着判断，判断变量a与b的大小
# 如果不是，就进行转换为int类型，然后判断大小
variable1 = "123"
variable2 = "435"
if type(variable1) == int or type(variable1) == float and type(variable2) == float or type(variable2) == int:
    if variable1 > variable2:
        print("是数字类型，且a>b")
    else:
        print("是数字类型，当a<=b")
else:
    variable1 = int(variable1)
    variable2 = int (variable2)
    if variable1 > variable2:
        print("是数字类型，且a>b")
    else:
        print("是数字类型，但a<=b")

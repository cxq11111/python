

# 1.使用函数，打印乘法表，乘法表格式用传入的参数决定，比如传入9，9就是99乘法表，结果将所有式子放入集合给返回值
def cheng(a, b):
    for i in range(a, b):
        for j in range(1, i+1):
            print(f"{i}x{j} = {i*j} \t", end="")
        print("")
cheng(1, 15)


# 2.使用函数，计算器实现，传入不定长关键字参数实现加减乘除计算器功能，比如传入12，22，"*"为12乘上22将结果返回
def jsj(**ab):
    a = ab["m"]
    b = ab["n"]
    w = a + b
    x = a - b
    q = a * b
    z = a / b
    return w, x, q, z
res1 = jsj(m = 11, n = 22)
print(res1)

# 3.函数实现纯数字列表，元组的求最大最小值的功能，结果返回
def csz(x):
    list1 = []
    list2 = []
    for i in x:
        if i.isdigit():
            list1.append(i)
    a = max(list1)
    b = min(list1)
    c = [a, b]
    list2.extend(c)
    tuple1 = tuple(list2)
    return list1, tuple1
res2 = csz("123456mn")
print(res2)

# 4.函数实现数据分类，传入不定长关键字参数，通过字典取值判断，实现数据分类，将不同的数据类型写入csv文件，将写入文件的功能写成另一个函数，使用函数写入注意，四道题都能实现的并可以课堂讲解每道题加2分


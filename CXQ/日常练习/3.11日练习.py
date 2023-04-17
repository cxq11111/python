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

# 练习1： 定义一个列表：放入奇数，每次循环算这个奇数的立方
num = [1, 3, 5, 7, 9]
for x in num:
    print(x**3)
# 练习2 ：写一个诗：“会当凌绝顶，一览众山小”，循环打印每个字
for s in "会当凌绝顶，一览众山小":
    # 空格也是一个字符，占一个位置
    print(s)
# 练习：回文数字，比如十位数字5665，具有对称结构，找出1000-9999中所有的回文数1111,2222,3333，4444


# 练习：通过循环判断年龄处于什么阶段，比如：幼儿1-6，儿童7-14，少年13-19，青年20-39，中年40-59，老年60以上

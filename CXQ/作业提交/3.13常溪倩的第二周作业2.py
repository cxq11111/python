
"""
 总结列表的使用方法
1.index():获取元素的索引，当元素有多个取头一个元素的索引
2.count():计算元素在列表的个数
3.sort():对列表进行排序，根据元素的编码进行排序，默认列表升序排列（reverse=False）,reverse=True降序排列
4.append():可以向列表中添加元素，添加到末尾的位置
5.insert():根据索引插入元素
6.extend():将两个列表按照顺序进行合并元素
7.pop():删除元素，默认删除最后一个，可以根据索引删除对应的元素
8.remove():移除元素，直接将对应的元素移除
9.设置摆放家具的程序.reverse()：翻转列表
10.copy():克隆一个列表，新的与旧的内存地址不一样，不是同一个列表，元素一样
11.del：删除关键字
12.clear():清空列表

"""
# 程序设计
# 1.实现1 - 10数字的叠加, 叠乘
a = 0
for i in range(1, 11):
    a += i
    print(a)

b = 1
for i in range(1,11):
    b *= i
    print(b)

# 2.使用 * 号打印出一个正三角形
for i in range(1, 10):
    for j in range(1, 10-i):
        print(" ", end="")
    for m in range(1, i+1):
        print("*", end=" ")
    print()
#  3.流量计费1.每个月49套餐, 10G流量, 超出1G收费1 / G元, 超出20G后开始收费2元 / G, 超出50G后开始收费5元 / G
set_meal = 49
flow = 10
i = int(input("请输入您的流量： "))
if 10 < i < 20:
    set_meal = (i - 10)*1 + set_meal
    print(f"您这月话费共消耗 {set_meal}元")
elif 20 <= i < 50:
    set_meal = (i - 10)*1 + (i - 20)*2 + set_meal
    print(f"您这月花费共消耗 {set_meal}元")
elif flow > 50:
    set_meal = (i - 20)*1 + (i - 20)*2 + (i - 50)
    print(f"您这月话费共消耗 {set_meal}元")


"""
for 循环比较注重循环的范围，循环的次数
while 循环比较注重循环的条件
while 表达式 :        -- 当表达式成立，开始循环，循环体执行，不成立循环结束
"""
# 例1： 循环打印1-9.设置摆放家具的程序
n = 1      # 定义变量为循环的初始值
while n <= 9:      # 当条件成立开始循环
    print(n)
    # 注意：初始值要持续递增，知道条件不成立结束循环
    n += 1      # n = n + 1

# 例2：变量递减的循环
m = 10
while m > 0:
    print(m)
    m -= 1
# 例3： 循环打印周1到周7，判断那天可以休息
weekday = 7
while weekday < 8:
    day = "周" + str(weekday)
    if day == "周7":
        print("周末可以休息了！")
    else:
        print(f"{day}学学学！")
    weekday += 1
# 练习：猜数字，1-6，定义一个数字，从键盘接受一个数字，看能否猜成功，给三次机会
sz =5    # 猜数字是不是5
i = 1
while i <= 3:
        num = input("请输入要猜的数字：")
        if num == str(sz):
            print("True")
            i = 4
        else:
            print("False")
            i += 1
# 练习：逢七必过，代码实现100以内的逢七必过

# 例1: 20以内说奇数不说偶数
for i in range(1,21):
    if i % 2 == 0:
        print("过")
        continue
    print(i)
# 上边例子，当我们遇到十三就跳过
for i in range(1,21):
    if i == 13:
        continue
    if i % 2 == 0:
        print("过")
        continue
    print(i)

# 练习：回文数字，比如十位数字5665，具有对称结构，找出1000-9999中所有的回文数1111,2222,3333，4444
for num in range(1000, 10000):
    g = num % 10             # 取个位数
    q = num // 1000          # 取千位数
    b = num // 100 % 10      # 取百位
    s = num // 100 //10      # 取十位
    if g == q and b == s:
        print(num)
# 练习：斐波那契数列，第一项1 第二项 1
# 第三项 1 + 1 = 2
# 1 1 2 3 5 8 ...  算出一百项
a = 1
b = 1
for i in range(100):
    a = b
    b = a + b
    print(b)
# 练习：通过循环判断年龄处于什么阶段，比如：幼儿1-6，儿童7-14，少年13-19，青年20-39，中年40-59，老年60以上

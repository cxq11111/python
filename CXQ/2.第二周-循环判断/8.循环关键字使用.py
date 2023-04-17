# 1. break:关键字，结束循环，当循环中遇到break循环就结束了
for i in range(10):
    if i == 6:
        # 当循环到 i 赋值为6 ，判断成立执行break，这个循环结束，后面的代码不执行
        break
    print(i)
# 例：猜喜欢的人，猜三次
for n in range(3):
    # name = input("请输入周杰伦喜欢的人: ")
    name ="昆凌"
    if name == "昆凌":
        print("我不同意！")
        break
    else:
        print("接着猜")
# 2.设置闰年判断程序.py continue,关键字，跳过当前某一次循环，后边循环继续
j = 1
while j <= 20:
    if j == 13:
        print('跳过')
        j += 1
        continue
    print(j)
    j += 1
# 逢七必过：数字中有7或7的倍数跳过 1- 100
# 17,27,37....    71,72,73..
for n in range(1, 100):
    if n % 7 == 0 or n % 10 == 7 or n // 10 == 7:
        print("跳过")
        continue
    print(n)


# "17"字符串中有没有7
for n in range(1, 100):
    if n % 7 == 0 or "7" in str(n):
        print("跳过")
        continue
    print(n)

# 练习：回文数字，比如十位数字5665，具有对称结构，找出1000-9999中所有的回文数1111,2222,3333，4444

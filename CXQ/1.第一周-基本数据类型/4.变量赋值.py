# 变量赋值

# 1.给单个变量进行赋值，使用 = ： 赋值符号
# == ： 判断左右两边相等
str_name ="海王星，天王星，冥王星"
print(str_name)
number = 88888888888
print(number)
pi = 3.1415926
print(pi)
bl = True
print(bl,type(bl))
# 2.多个变量赋值相同的值
a = 10
b = 10
c = 10
# 使用连等号
x = y = z = 100
print(x,y,z)
o = p = q ="海绵宝宝"
print(o,p,q)
# 3.多个变量赋值不同的值
o = 6
p = 7
q = 8
#  左右两边一一对应赋值
n, m = 8000, 9000
print(n, m)
# 4.两个变量交换数据
chen = "BMW"
chang = "奥迪"
print(chen,chang)
# 可以利用第三个变量
zj = chen        # zj = chen = "BMW"
print(zj)
# chang = zj            # chang = zj = "BMW"
# chen = chang               # chen = chang = "BMW"
# print(chen,chang)
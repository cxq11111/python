# -- coding:utf-8 --
def sum(a):
    print(a+10)
sum(10)

def sum(a,b):
    print(a+b)
sum(666,999)     # 形参a,b 实参 666,999

# def sum():
#     a = input('请输入数值:')
#     b = input('请输入第二数值:')
#     c = int(a) + int(b)
#     print(c)
# sum()
# def sum():
#     a = int(input('请输入数值:'))
#     b = int(input('请输入第二数值:'))
#     c = a + b
#     print(c)
# sum()

def a(x,y):
    if type(x) is str and type(y) is str:
        return x+y
    if type(x) is int and type(y) is int:
        return x+y
print(a('x','y'))

def sum():
    li = ['0','1','2','3','4','5','6','7','8','9']
    a = input('请输入数值:')    # 一定是字符串
    b = input('请输入第二数值:')
    if a in li and b in li:
        return int(a) + int(b)
    else:
        return a+b
print(sum())
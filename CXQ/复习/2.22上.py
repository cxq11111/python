# -- coding:utf-8 --
# 函数文档说明
def a(b,c):
    """
    :param b:
    :param c:
    :return:
    """
    c1 = b+c
    print(c1)
help(a)
a(1,2)

def testB():
    print('--- testB start ---')
    print('这里是testB函数执行的代码....(省略)...')
    print('--- testB end ---')
# 自定义函数A
def testA():
    print('--- testA start ---')
    testB()
    print('--- testA end ---')
testA()

# 位置参数：带用函数时根据函数定义的参数位置来传递参数
def user_info(name,age,sex):
    print(f'您的名字是{name},年龄是{age},性别是{sex}')
user_info('TOM',20,'男')

# 关键字参数
def user_info(name,age,sex):
    print(f'您的名字是{name},年龄是{age},性别是{sex}')
user_info(name='lisa',age=25,sex='女')

# 缺省参数
def user_info(name,age,sex='男'):
    print(f'您的名字是{name},年龄是{age},性别是{sex}')
user_info('rose',19,'女')
user_info('tom',18)

# 不定长参数：不定长参数也叫可变参数，用于不确定调用的时候会传递多少个参数(不传参也可以)的场景
# 1.动态位置传参
def user_info(*args):
    print(args)
user_info('TOM')
user_info('TOM',18)

# 2.动态关键字传参
def user_info(**kwargs):
    print(kwargs)
user_info(name='lisa',age=19,id=110)

# 按位置传参
def fun(a,b,c):
    print('...')
fun(10,20,30)	#函数调用，参数的顺序及个数要和定义时的参数保持一致

# 按关键字传参
def fun(a,b,c):
    print('...')
 #函数调用时，要用"="将关键字与值进行连接，此时，这三个参数表达式的位置可以换，因为编译器会根据关键字查找，然后再将值传递给形参
fun(a=10,b=20,c=30)
fun(b=23,c=12,a=11)

# 混合传参
def fun(a,b,c,d):
    print('...')
 # 函数调用，混合传参时，必须要位置传参在前，关键字传参在后
fun(10,20,d=40,c=30)
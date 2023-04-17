class Square(object):
    """计算正方的周长和面积"""

    def __init__(self,length):
        self.length = length

    def perimeter(self):
        """计算周长的方法"""
        p = self.length * 4
        return p

    def area(self):
        """计算面积的方法"""
        a = self.length ** 2
        return a
# 实例化对象，一个正方形
s = Square(length=10)
print(s.perimeter())    # 调用计算周长的方法
print(s.area())         # 调用计算面积的方法

# 练习：升级上边的案例，定义一个类可以计算出 长方形的周长和面积
class Squarel(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zhouchang(self):
        m = self.a * 2 + self.b * 2
        return m

    def mianji(self):
        n = self.a * self.b
        return n
s = Squarel(a=2, b=3)
print(s.zhouchang())
print(s.mianji())
class Zheng(object):
    def __init__(self, chang):
        self.chang = chang
    def m(self):
        p = self.chang * 4
        return p
    def z(self):
        a = self.chang ** 2
        return a
class Chang(Zheng):
    def __init__(self, chang, kuan, gao):
        Zheng.__init__(self, chang)
        self.gao = gao
        self.chang = chang
        self.kuan = kuan
    def n(self):
        a = (self.chang * self.kuan + self.chang * self.gao + self.kuan * self.gao) * 2
        return a
    def l(self):
        tiji = self.chang * self.kuan * self.gao
        return tiji
x = Zheng(chang=2)
print(x.m())
print(x.z())
y = Chang(chang=2, kuan=2, gao=2)
print(y.n())
print(y.l())
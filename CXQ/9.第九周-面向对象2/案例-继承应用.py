"""
父类:计算正方形面积与周长，定义属性为边长
子类:计算长方形表面积和体积，重写父类的构造方法
"""
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
        Zheng.__init__(self,chang)
        self.gao = gao
        self.chang = chang
        self.kuan = kuan
    def n(self):
        mianji = (self.chang * self.kuan + self.chang * self.gao + self.kuan * self.gao) * 2
        return mianji
    def l(self):
        tiji = self.chang * self.kuan * self.gao
        return tiji
x = Zheng(chang=2)
print(x.m())
print(x.z())
y = Chang(chang=1, kuan=2, gao=2)
print(y.n())
print(y.l())
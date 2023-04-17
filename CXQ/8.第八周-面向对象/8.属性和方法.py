"""
class 类名:
    类属性1
    类属性2
    类属性3
    ...
    def 方法名1(self):
        ...
    def 方法名2(self):
        ...
"""
# 定义个女朋友
# 类名后边括号中表示继承，默认是继承object，不写就是默认值
# object 是所有类的类，是基类，所有定义的类都会去继承object
class GirlFriend(object):
    height = 160
    weight = 102
    fule = "自然色"
    job = "模特"
    def dress(self):
        # self:每个类中定义的方法都有self参数，必须有，指的是对象本身
        print("洗衣服")
    def cooking(self):
        print("做饭")
    def abc(self):
        print("养孩子")
if __name__ == '__main__':
    # 实例化对象
    g1 = GirlFriend()
    print(g1.job)        # 访问属性
    # 调用方法
    g1.cooking()
    g1.abc()
    # 给对象更改属性
    g1.weight = 140
    print(g1.weight)
    # 再实例化一个对象
    g2 = GirlFriend()
    print(g2.weight)
    g2.weight = 120
    print(g2.weight)
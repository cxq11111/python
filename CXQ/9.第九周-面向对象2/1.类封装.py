# 封装:将属性,方法进行封装，隐藏不对外界暴露，使用私有属性和私有方法
class Class(object):
    # object:基类，所有类继承基类，里面定义很多魔法方法，例如:__init__()实例方法，__del__()析构函数
    cla_name = "类属性"
    def __init__(self, cls_room):
        # 实例属性，对象属性
        self.cla_name = cls_room
        self._job = "造火箭"
        self.__hobby = "课下不复习"

    def get_hidden(self):
        return self.__hobby

    def __set_hidden(self, h):
        # 方法前边添加双下划线，称为私有方法
        self.__hobby = h

    def hidden(self, h):
        self.__set_hidden(h)

# 实例对象，构造一个对象
AI2 = Class(cls_room=206)
print(AI2.cla_name, Class.cla_name)     # 类属性，类和对象都可以访问
# print(AI2.cla_room, Class.cla_room)   # 实例属性，类不能访问，只有这个实例对象可以访问
# 访问保护属性，私有属性
# print(AI2._job,Class._job)    # 保护属性如果和共有属性对象可以访问，类不能访问实例属性
# print(AI2.__hobby,Class.__hobby)    # 私有属性，只能类内访问
# 可以通过类内定义的实例方法访问
print(AI2.get_hidden())
# AI2.__set_hidden(h="学而时习之")
# print(AI2.get_hidden())
# 强制访问，不建议这样做
print(AI2._Class__hobby)
# 强制调用私有方法
AI2._Class__set_hidden(h="时常复习")
print(AI2._Class__hobby)
# 内部的方法可以调用私有方法
AI2.hidden(h="死活不学")
print(AI2.get_hidden())
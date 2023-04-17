# 定义类
class Hero(object):
    # 类属性定义是固定的值，只能通过实例化后再修改
    # 所有的对象实例化得到的属性都一样
    print("1.类属性被执行！")      # 定义类被执行，这里的类属性会被执行
    def __init__(self):
        """__init__(),方法叫做魔法方法，是定义类自带的，来自基类
        在实例化类的时候，会首先调用这个方法，因此我们可以在这里定义属性"""
        print("2.这个init方法被调用")
# 实例化对象
xiaoqiao = Hero()

class Dog:
    def __init__(self, name, age, breed):   # 初始化函数，实例化对象被自动调用，进行传参数
        # self:指对象本身，self.name 是对象属性
        self.name = name
        self.age = age
        self.breed = breed
# 实例化属性，构造一个对象
xiaobai = Dog(name="小白", age=6, breed="中华田园犬")
print(xiaobai.name, xiaobai.age, xiaobai.breed)
# 再实例化一个
wkeke = Dog(name="王可可", age=3, breed="阿拉斯加雪橇犬")
print(wkeke.name, wkeke.age, wkeke.breed)
# 练习: 使用init实例化一个班级类, 通过这个班级类构造出不同专业的班级, 定义方法进行上课

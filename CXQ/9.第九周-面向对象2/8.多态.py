# 172.19.65.52
# 多态:指具有不同功能的函数使用相同的函数名，这样就可以用一个函数名调用不同内容的函数
class ArmyDod(object):
    def bite_enemy(self):
        print("追击罪犯")
class DruDog(object):
    def track_drug(self):
        print("搜查毒品")
class Police(object):
    def army_work(self, dog):
        dog.bite_enemy()
    def drug_work(self, dog):
        dog.track_drug()
# 实例化一个对象
zhu = Police()
zhu.army_work(dog=ArmyDod())   # 实例化的对象调用方法，需要将实例化的对象dog对象传入
zhu.drug_work(dog=DruDog())     # 实例化追查毒品
# 利用类的多态进行简写
class ArmyDog(object):
    def work(self):
        # 不同功能的函数使用相同的函数名
        print("追击罪犯")
class DruDog(object):
    def work(self):
        # 不同的函数使用相同的函数名
        print("搜查毒品")
class Police(object):
    def work(self, dog):
        # 可以用一个函数名调用不同内容的函数
        dog.work()
# 实例化一个警察
chang = Police()
 # 多态的调用
chang.work(dog=ArmyDog())      # 这个方法起到追击罪犯的作用
chang.work(dog=DruDog())      # 这个方法起到搜查毒品的作用
"""
练习:定义工具:抹布，拖把 可以有不同的方法，相同的方法名，定义学生类:有清洁方法，需要工作做参数传入，使用多态的写法
"""
class Mabu(object):
    def job(self):
        print("擦桌子")
class Tuoba(object):
    def job(self):
        print("拖地")
class Student(object):
    def job(self, stu):
        stu.job()
chang = Student()
chang.job(stu=Mabu())
chang.job(stu=Tuoba())
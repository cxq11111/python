# 定义一个类
# 类名:需要首字母大写，遵循大驼峰命名规则，当多个单词命名时首字母都大写
class Person:
    pass

# 首字母大写是规范，不是必要的需求
class dog:
    pass

# 创建学生类
class Student:
    pass
# 创建班级类
class Class:
    pass

# 创建人对象，创建对象的过程叫做实例化对象
zhangsan = Person()
# 创建学生
changxiqian  = Student()
# 查看类，查看对象
print(Student)                 # <class '__main__.Student'>
print(changxiqian)             # <__main__.Student object at 0x000001B180A6BC18>

class Boyfriend:
    pass

chengzhengwei = Boyfriend()
print(chengzhengwei)
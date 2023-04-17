# 继承:子类继承父类属性和方法，子类实例化对象可以调用父类的属性和方法，也可以继承父类的属性
# 单继承:子类继承一个父类
class Father(object):
    # object:所有的类继承于基类，给定义的类提供魔法方法
    work = "伐木工人"
    _job = "抓熊"

    def day_work(self):
        print("砍树,伐木...")
    def _day_job(self):
        print("抓熊大,熊二")

class Son(Father):
    # 子类继承父类
    hobby = "徒步"

    def studay(self):
        print("学习开挖掘机...")

# 实例化对象
dudu = Son()
print(dudu.work, dudu._job)     # 子类继承了父类的属性，可以实例化对象进行访问
dudu.day_work()     # 子类继承了父类的方法，可以实例对象进行调用
dudu._day_job()
print(dudu.hobby)      # 拥有自己的属性
dudu.studay()          # 自己方法

class GrandFather(object):     # 间接父类
    work = "土夫子"
    def ee(self):
        print("会打盗洞")

class Father(GrandFather):
    job = "鉴别古董"
    def collect(self):
        print("收藏古董")

class Son(Father):
    hobby = "考古"
    def protect(self):
        print("保护文物...")

# 实例化
wexie = Son()
print(wexie.work, wexie.job, wexie.hobby)
wexie.ee()   # 子类继承了父类的父类，可以调用
wexie.collect()
wexie.protect()

import time
# __del__方法:叫做析构函数，类魔法方法，python具有垃圾对象回收机制，当某个实例对象所有引用被清除之后，所占内存空间自动释放，python提供的__del__()会处理
name = "司马迁"
print(name)
del name
# print(name)
# 定义类
class Zhz(object):

    def __init__(self, name):
        self.name = name
        print("对象实例化，init函数被调用")

    def __del__(self):
        # 当程序结束，实例化对象会被回收，会调用这个函数
        print("实例对象%s被删除会调用这个del函数" % self.name)

if __name__ == '__main__':
    # 实例化对象
    zhenhuan = Zhz(name="甄嬛")
    # time.sleep(3)
    # print("结束程序")

    # 手动删除对象
    del zhenhuan         # 执行del语句，对象会调用__del__函数删除这个数据
    time.sleep(3)
    print("结束程序")

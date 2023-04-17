class Student(object):
    def __init__(self, id, name, sex, phone):
        self.id = id
        self.name = name
        self.sex = sex
        self.__phone = phone

    @property  # 将这个方法调用方式变成属性方式获取
    def phone(self):
        # 类的内部可以调用私有属性
        return self.__phone
    @phone.setter   # 将修改属性方法
    def phone(self, p):
        # 内部修改私有属性
        self.__phone = p

if __name__ == '__main__':
    chang = Student(id="123456", name="常溪倩", sex="女", phone="18238575153")
    # 通过方法获取修改私有属性
    # print(chang.get_hidden)
    # chang.set_hidden(p="18238576688")
    # print(chang.get_hidden())
    # 共有属性获取修改
    print(chang.name)
    chang.name = "倩倩"
    print(chang.name)
    # 让方法变成属性调用方式
    cai = Student(id="456789", sex="女", name="蔡萌", phone="2646876")
    print(cai.phone)
    cai.phone = "13548554"
    print(cai.phone)
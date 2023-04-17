# -- coding:utf-8 --
lis=[]

def fun():
    print("""
            ----菜单选项----
            1.添加功能
            2.删除功能
            3.查询功能
            4.展示功能
            5.修改功能
            -----------------
            """)
# fun()

def add():
    print("""-----添加学生信息-----""")
    name = input('输入姓名')
    age = int(input('输入年龄'))
    sex = input('输入性别')
    for i in lis:
        if i['name'] == name and i['age'] == age and i['sex'] == sex:
            print('您输入的信息已存在')
            return

    dic = {}
    dic['name'] = name
    dic['age'] = age
    dic['sex'] = sex
    lis.append(dic)
    print(lis)
# add()

def delete():
    print('-------欢迎进入删除学生页面--------')
    num = int(input('请输入您要删除的序号'))
    if 0 <= num <= len(lis)-1:
        delete_num = input('你确定要删除?(y/n)')
        if delete_num == 'y' or delete_num == 'yes':
            del lis[num]
            print('删除成功')
        elif delete_num == 'n' or delete_num == 'no':
            print('退出删除操作')
    else:
        print('输入的序号错误，请重新操作')
# delete()

def show():
    for i, j in enumerate(lis):
        print('序号%d 姓名%s 年龄%d 性别%s' % (i,j['name'], j['age'], j['sex']))
# show()

def update():
    print('-------欢迎进入更新学生页面---------')
    show()
    print('-------以上是所有学生信息---------')
    num = int(input('请输入您要修改的信息:'))
    if 0 <= num <= len(lis) - 1:
        lis[num]['name'] = input('请输入你修改后的姓名:')
        lis[num]['age'] = int(input('请输入你修改后的年龄:'))
        lis[num]['sex'] = input('请输入你修改后的性别:')
        print('修改成功')
        print(lis[num])
    else:
        print('您输入的序号错误')
# update()

# 查询
def find():
    print('-------欢迎进入查询页面----------')
    name = input('请输入您想要查询的名字:')
    for i in lis:
        if i['name'] == name:
            print(i)
        else:
            print('该学生不存在')
# find()


def main():
    while True:
        fun()
        num = int(input('请输入需要的功能:'))
        if num == 1:
            add()
        elif num == 2:
            delete()
        elif num == 3:
            find()
        elif num == 4:
            show()
        elif num == 5:
            update()
        else:
            break

if __name__ == '__main__':
    main()


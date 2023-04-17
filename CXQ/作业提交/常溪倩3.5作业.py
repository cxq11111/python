# 1. 写出所学的基本数据类型与英文符号  int-整型 str-字符串 float-浮点型 bool-布尔型

# 2.设置闰年判断程序.py 写出标识符的命名规则
"""
   命名规则：只能使用数字，字母，下划线，切记不能使用数字开头，数字开头会报错
   规范：
       1.区分大小写，例如name 和 NAME 不一样
         mysql 不区分大小写，Linux区分大小写 ，ls 和LS 不一样
       2.用小写字母给变量，对象，函数等命名，类的开头需要大写
       3.见名知意，看见名字就要知道内容数据的大概情况，例如： name，title，age，phone_number...
       4.不要混淆，例如：字母O和数字0，字母l和数字1
       5.不要跟系统的关键字冲突，例如： if for while in and
 """

 # 3. 定义一个学生的信息变量: 姓名, 性别, 年龄, 学号, 班级, 专业, 家庭地址   格式化输出信息
name = "常溪倩"
gender = "女"
age = 19
student_number = 202115050202
grade= "2班"
specialty = "人工智能"
house_address = "河南省安阳市"
print("name%s\ngender%s\nage%s\nstudent_number%s\ngrade%s\nspecialty%s\nhouse_address%s" % (name,gender,age,student_number,grade,specialty,house_address))

# 4. 将上述改为键盘输入每一项信息, 然后打印格式化输出
name = input("请输入您的姓名： ")
print("姓名：%s"  % name)
gender = input("请输入您的性别： ")
print("性别：%s"  % gender)
age = input("请输入您的年龄： ")
print("年龄：%s"  % age)
student_number = input("请输入您的学号： ")
print("学号：%s"  % student_number)
grade = input("请输入您的班级： ")
print("班级：%s"  % grade)
specialty = input("请输入您的专业： ")
print("专业：%s"  % specialty)
house_address = input("请输入您的家庭住址： ")
print("家庭住址：%s"  % house_address)

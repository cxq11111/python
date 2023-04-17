# 标识符：在编程中要起名字，比如：给变量，函数，类，对象等起名字


"""
   例如：姓氏-名字
   命名规则：只能使用数字，字母，下划线，切记不能使用数字开头，数字开头会报错
   规范：
   1.区分大小写，例如：name 和 NAME 不一样
     mysql 不区分大小写， Linux区分大小写，ls 和 LS 不一样
   2.用小写字母给 变量，对象，函数等命名，类的开头需要大写
   3.见名知意，看见名字就要知道内容数据大概情况，例如： name，title,age,phone_number...
   4.不要混淆，例如：字母O与数字0，字母l与数字1
   5.不要跟系统的关键字冲突，例如：if for while in and
   命名写法：多个单词命名时，可以用下划线连接：one_two_three,air_shool,ai_two_class
   驼峰命名法：多个单词，第一个单词小写，后边的单词首字母大写 geyYouName,fullLove,   定义类时：FirstPerson
"""

a=10
import  keyword
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

"""

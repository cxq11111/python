# print(): 打印输出

# 1. 输出函数
# 1) 输出变量或常量
print("梅花香自苦寒来")
say = "宝剑锋从磨砺出"
print(say)
print("常溪倩",20,100)
# 2）每次print都会换行，这是有一个参数：end，默认为 end = "\n"
# \n：换行符，让字符串在这个地方另起一行
print("咱们试一试\n试试就试试",end="!!???")
print("看看呗")
"""
\n 这种前边带 \后边跟字母或数字，叫做转义字符
\ 会将后边的字母或数字一起转义，赋予其他意义
\t 制表符，相当于一个tab键
"""
print("姓名：常溪倩\n年龄：18\n性别：女")
print("貂蝉\t小乔\t甄姬\t安琪拉")
# print("\" )
# len():计算字符串长度
print(len(" \ "))
print("\\")
print(len("\\"))
print("貂蝉\\小乔\\甄姬\t安琪拉")
# 字符串前添加r也可以让字符串中的转义字符不再转义
print(r"姓名：黄忠\n年龄：99\n性别：男")
print(r"老话说得好：'世上无难事，只要肯努力！'")
print(r"老话说得好：\"世上无难事，只要肯努力！\"")
# \u4e00-\u9fa5:一，龥 所有汉字编码范围在这个区间
print("\u4e00     \u9fa5")

# 2.input():输入函数，可以接收来自键盘输入的内容
#name = input("宝，你叫什么名字：")
#print(name)
#number = input("请输入您的余额：")
#print(number,type(number))
# 有时候需要数据类型转换
#number = int(number)
#print(number,type(number))
print("name = 常溪倩\nage= 19\ngrade= 100")
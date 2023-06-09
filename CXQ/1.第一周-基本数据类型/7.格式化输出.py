# 格式化字符串 （p22）

# 输出到文件中,open()：打开第一个文件，第一个参数是文件名字第二参数是操作文件方式,w:write 写入
file1 = open("data.txt","w")
# "".replace(":","\n")
print("通知：明天你们好像没有课",file=file1)

# 1.%s: 占位符，可以拼接字符串型数据，拼接数据前判断是否为字符串，不是字符串就是转化型类型，str(),实际上可以拼接任何数据类型
name = "擎天柱"
print("汽车人首领：%s" % name)
number = 18238576688
print("我的电话号码是： %s" % number)
age = 19
money = 152.36
print("%s 的年龄是%s，零花钱是%s" % (name,age,money))
# %6.3s：里面的6表示拼接的字符串所占的位数，
#        .3表示取拼接的字符串前三个，
#        如果占的位置不够，会自动变成与字符串本身长度一样单位
word = "abcdefghijklmnopqrst"
print("%s" % word)
print("%.3s" % word)
print("%6.3s" % word)
print(len(word))

# %d：可以拼接整型，拼接数字类型数据可以，字符串不行，纯数字的字符串也会报错
print("常溪倩电话:%d" % number)
f1 = 6.235
print("拼接小数：%d" % f1)
s1 = "980"
# TypeError: %d format: a number is required, not str
# print("拼接字符串：%d" % s1)
# %02d:里面0表示在位数不够2的时候前面添加0,2表示占两个位置，当数字大于位置的时候，按数字的长度占位
year = 2002
month = 10
day = 1
print("常溪倩的生日：%d-%d-%d" % (year,month,day))
print("常溪倩的生日：%10d-%02d-%02d" % (year,month,day))

# 3.%f:可以拼接浮点型数据，默认保留小数点后六位，不够六位，补0
pi = 3.14
print("π的值是：%f" % pi)
zs = 100
print("拼接整数看看：%f" % zs)
# %.3f：.3表示保留小数点后三位，四舍五入
pai = 3.1415926
print("π后保留两位：%.2f" % pai)
pa = 3.14159
print("pa后保留小数点后四位： %.4f" % pa)
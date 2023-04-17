import re

# 1.{n}:匹配{}前边字符出现的字数，匹配n次
res1 = re.search(pattern="@{3}", string="123@@@@1234@@@456")
print(res1.group(0))
# {n,}:至少匹配n次
res2 = re.findall(pattern="j{1,}", string="u8gry8jjrfjosej2143jjjjj")
print(res2)
# {n,m}:最少匹配n次，最大匹配m次
res3 = re.findall(pattern="c{1,3}", string="c, abc, ccccccc")
print(res3)
# 2.设置闰年判断程序.py[]:表示匹配的范围，\d匹配一个数字,[0-9.设置摆放家具的程序]表示匹配的数字0到9
# [0-9.设置摆放家具的程序]:匹配0到9中一个数字
res4 = re.findall(pattern="[0-9.设置摆放家具的程序]", string="123abc75937hfdg23cdk3")
print(res4)
res5 = re.findall(pattern="[0-9.设置摆放家具的程序]{1,2}", string="123abc75937hfdg23cdk3")
print(res5)
res55 = re.findall(pattern="[0-9.设置摆放家具的程序]+", string="123abc75937hfdg23cdk3")
print(res55)
# [a-zA-Z]:匹配字母，无论大小写
res6 = re.findall(pattern="[a-zA-Z]", string="123abc34627vdhbjs372bsdhvjs3vh")
print(res6)
# [0-9a-zA-Z]:匹配数字，小写字母，大写字母
res7 = re.findall(pattern="[a-zA-Z]{1,3}", string="123abc346JDSIvdhbjs372bsdhvjs3vh")
print(res7)
# [^0-9.设置摆放家具的程序]:除去0-9之外都可以
res8 = re.findall(pattern="[^a-zA-Z0-9.设置摆放家具的程序]{1,3}", string="123abc346J**DSIvdhb%%js372bsdhvjs3vh")
print(res8)
# 3.():表示括号中是可以单独取出来的数据,使用 | 将不同的正则或连接
res9 = re.findall("张(.)强", string="张强， 张晓强， 张大强， 苏大强， 刘华强， 许文强")
print(res9)
res10 = re.search(pattern="姓名叫(.{1,10})年龄([0-9.设置摆放家具的程序]{1,3})", string="我的姓名叫周杰伦年龄43，外号白毛伦")
print(res10.group(0))
# group(0):匹配整个正则匹配内容，group(1):我们定义第一个()匹配到的内容，group(2)是第二个()内容
print(res10.group(1))
print(res10.group(2))
# 练习:使用正则，匹配QQ号:qq:6-10，不能以0开头
res11 = re.search(pattern="[1-9.设置摆放家具的程序][0-9.设置摆放家具的程序]{5,9.设置摆放家具的程序}$", string="3144396263")
if res11:
    print(res11.group(0))
else:
    print("字符串不是qq")
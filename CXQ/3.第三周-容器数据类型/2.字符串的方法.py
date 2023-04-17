"""
字符串的方法：字符串名.方法()
"""
# 1.index():获取字符串的首字母的索引，有多个重复取第一个
# 可以有起始位置，终止位置（取不到）；当找不到时会报错
str1 = "To be or not to be ,not not"
index1 = str1.index("not")
print(index1)
index2 = str1.index("o")
print(index2)
index3 = str1.index("o", 3, 10)
print(index3)
# index4 = str1.index("a")
# ValueError: substring not found
# print(index4)
# 2.find():与index()用法相同，找不到不会报错
str2 = "that is are question"
index4 = str2.find("are")
print(index4)
index5 = str2.find("a", 3, 9)
print(index5)
index6 = str2.find("1")
print(index6)
# 3.count():计算子字符串在字符串中出现的次数
str3 = "年年岁岁花相似，岁岁年年人不同"
print(str3.count("年"))
print(str3.count("岁岁"))
# 4. spilt():分割字符串，返回一个列表，当不填写参数，默认分割空格，\t,\n...可以使用符号进行分割，字符都行，分割后，用于分割的字符没有了，每个的每部分都放入列表中，可以指定分割的最大数
str4 = "明眸，皓#齿，冰、肌$玉#骨，娇小,可*爱"
list1 = str4.split()
print(list1)
list2 = str4.split(",", 2)
print(list2)
# 5.strip():默认去掉首尾的空格，可以去掉字符串首尾的符号
str5 = "a, abc3, 23.43  a"
print(str5)
print(str5 .strip())
print(str5.strip("a"))
# 6.replace():替换
str6 = "飞流直下三千尺，疑是银河落九天"
s1 = str6.replace("三", "9.设置摆放家具的程序")
print(s1)
s2 = str6.replace("九", "3")
print(s2)
# 能不能直接修改字符串的内容，例如列表修改元素
# TypeError: 'str' object does not support item assignment
# str6[0] = "跑"
# print(str6)
# 注意：字符串的元素不能进行修改
# 7.upper():将小写转换为大写
str7 = "abcEFG"
print(str7.upper())
# 8.lower():将大写转换为小写
str8 = "ahufdaHAFUGA"
print(str8.lower())
# 9.设置摆放家具的程序.join():拼接字符串，将序列拼接进指定字符串，这个字符串会将序列的每个元素进行分隔
list3 = ["计春华", "徐锦江", "鳌拜"]
s = "+".join(list3)
print(s)





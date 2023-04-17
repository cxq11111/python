import re
# 1.match():从字符串开头进行匹配，匹配成功返回一个对象，匹配不成功返回None
res1 = re.match(pattern="abc\d\w+", string="1abc124j1a")
# print(res1.group(0))

# 2.search():从字符串任意位置进行匹配，如果匹配成功返回，如果有多个结果只返回一个
res2 = re.search(pattern="abc\d\w+", string="1abc124+dcsa3dsf")
print(res2.group(0))

# 3.findall():匹配字符串找到所有符合条件的子字符串，返回一个列表
# .*?:非贪婪匹配
res3 = re.findall(pattern="a.*?z",string="123acf650z---a+z")
print(res3)

# 4.split():按照一定格式，对字符串进行分割，返回一个列表
res4 = re.split(pattern="\d", string="ads1dasfy153yd1few2_0_")
print(res4)

# 5.sub():一个新的字符替换一个旧的字符
res5 = re.sub(pattern="\d", repl="-", string="fds1hdu2dsagyv7ayfg0")
print(res5)
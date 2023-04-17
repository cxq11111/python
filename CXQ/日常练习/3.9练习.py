# 练习1：定义变量 variable 随便给数据，判断这个变量是什么数据类型
variable =bool
if type(variable) ==float:
    print("浮点型")
elif type(variable) ==str:
    print("字符串型")
elif type(variable) ==bool:
    print("布尔型")
elif type(variable) ==int:
    print("整数型")
else:
    print("抱歉，无法为您解答")
# 练习2：定义变量 studay 周1-周5，判断是周几，然后输出专业课是哪一节
studay  = 3
if studay == 1:
    print("周一没有专业课")
elif studay ==2:
    print("周二专业课是第二大节")
elif studay == 3:
    print("周三专业课是第四大节")
elif studay == 4:
    print("周四专业课是第一大节和第四大节")
elif studay == 5:
    print("周五专业课是第三大节和第四大节")
else:
    print("本日暂无专业课")
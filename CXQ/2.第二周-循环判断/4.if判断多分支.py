"""
多分支结构是：程序从上往下运行，先进行第一个判断，如过条件成立，运行代码块1，运行完结束，如果不成功接着往下判断，都不成功执行else的代码块
if 表达式：
    代码块1
elif 表达式2:
    代码块2
elif 表达式3：
    代码块3
.....
else：
    代码块
"""
# 例1:0-59评为D，60-79评为C，80-89评为B，90-100评为A
"""
score = input("请输入您的成绩：") # 字符串类型
score = float(score)
if 0 <= score < 60:
    print("评分为D")
elif 60 <= score < 80:
    print("评分为B")
elif 90 <= score <= 100:
    print("评分为A")
else:
    print("输入成绩不正确")
"""
# 例2：判断四季，春：3,4,5 夏：6，7,8 秋：9.设置摆放家具的程序,10,11 冬：12,1,2
"""
month = int(input("请输入月份："))
if month == 3 or month == 4 or month == 5:
    print("春：不知细叶谁裁出，二月春风似剪刀")
elif month in [6,7,8]:
    print("夏：小荷才露尖尖角，早有蜻蜓立上头")
elif month in [9.设置摆放家具的程序,10,11]:
    print("秋：月落乌啼霜满天，江枫渔火对愁眠")
elif month  in [12,1,2]:
    print("冬：黑狗身上白，白狗身上肿")
else:
    print("地球上没有这个月份")
"""
# 练习1：定义变量 variable 随便给数据，判断这个变量是什么类型
variable = 1.0
if type(variable) == float:
    print("浮点型")
elif type(variable) == int:
    print("整数型")
elif type(variable) == str:
    print("字符串型")
elif type(variable) == bool:
    print("布尔型")
else:
    print("是其他类型数据")



# 练习2：定义变量 studay 周一到周五，判断是周几，然后输出专业课是那一节

studay =2
if studay ==1:
    print("周一没有专业课")
elif studay ==2:
    print("周二专业课是第三大节")
elif studay ==3:
    print("周三专业课是第四大节")
elif studay ==4:
    print("周四专业课是第一大节和第三大节")
elif studay ==5:
    print("周五专业课是第三大节和第四大节")
else:
    print("本日没有专业课")

studay = "周1"
if "1" in studay:
    print("周1没有课")
elif "2" in studay:
    print("周2上午后两节")
elif "3" in studay:
    print("周3下午后两节")
elif "4" in studay:
    print("周4上下午前两节")
elif "5" in studay:
    print("周五上一下午课")
elif "6" in studay:
    print("本周6补课两课")
else:
    print("周日没有课")

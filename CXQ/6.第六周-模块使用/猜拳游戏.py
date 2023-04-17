import random
caiq = ["石头", "剪刀", "布"]
stu = {"ming": 0, "mao": 0}
for n in range(10000):
    ming = random.choice(caiq)
    mao = random.choice(caiq)
    if ming == mao:
        print(ming, mao)
        print("平局，不得分")
    else:
        if ming == "石头" and mao == "剪刀":
            print("小明 +1")
            stu["ming"] += 1
        elif ming == "剪刀" and mao == "布":
            print("小明+1")
            stu["ming"] += 1
        elif ming == "布" and mao == "石头":
            print("小明 +1")
            stu["ming"] += 1
        else:
            print("小毛 +1")
            stu["mao"] += 1
print(stu)

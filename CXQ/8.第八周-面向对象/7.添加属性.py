# 定义类，在外部添加属性
class Hero:
    pass
# 实例化对象
daji = Hero()
# 添加属性，通过对象添加属性
daji.name = "妲己"
daji.occ = "法师"
daji.hp = 4600
daji.mp = 800
daji.attact = 180
# 利用对象调用属性
print(f"{daji.name},职业{daji.occ}, 血量{daji.hp}, 魔法值{daji.mp}, 攻击力{daji.attact}")

# 2.定义类，添加类属性
class BoyFriend:
    # 定义类属性
    height = 175
    weight = 150
    fuse = "黄黑"
    job = "程序员"
    salary = 1000000
# 实例化对象，这个对象会带有类属性
chenzhenwei = BoyFriend()
print(f"你的男朋友是{chenzhenwei.job},年薪{chenzhenwei.salary}")
czw = BoyFriend()
print(f"你的男朋友是{chenzhenwei.job},年薪{chenzhenwei.salary}")
# 1.通过类给类添加属性，这个属性会是类属性，所有实例化的对象都会拥有这个属性
BoyFriend.say = "i love you"
czw2 = BoyFriend()
print(czw2.say)
print(czw.say)
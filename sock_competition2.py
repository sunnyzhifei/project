from random import choice
from time import sleep

u_count = 0
c_count = 0
times = 0
dict1=['上','下','左','右','中']


def u_attack():
# 用户进攻
    global u_count, c_count
    print("玩家请选择进攻方向[1,2,3,4,5]:")
    u_num = input()
    c_num = choice(dict1)
    print ("玩家进攻方向:%s" % u_num)
    print ("电脑防守方向:%s" % c_num)
    if u_num != c_num:
        print ("球进了，玩家得1分")
        u_count = u_count + 1
    else:
        print ("进攻失败")


def u_defend():
# 用户防守
    global u_count, c_count
    print ("玩家请选择防守方向[1,2,3,4,5]:")
    u_num = input()
    c_num = choice(dict1)
    print ("玩家防守方向:%s" % u_num)
    print ("电脑进攻方向:%s" % c_num)
    if u_num != c_num:
        print ("防守失败，电脑的得1分")
        c_count = c_count + 1
    else:
        print ("防守成功")


while times < 5:
    # 进行最基本的5次点球大战
    print ("-------第 %d 局--------" % (times + 1))
    u_attack()  # 用户进攻

    # 判断用户进攻后，能否提前结束比赛
    if u_count > c_count:
        if u_count - c_count > (5 - (times + 1)) + 1:
            print ("玩家提前获胜!")
            print ("比分 玩家_%d:电脑_%d" % (u_count, c_count))
            break
    else:
        if c_count - u_count > 4 - times:
            print ("电脑提前获胜!")
            print ("比分 玩家_%d:电脑_%d" % (u_count, c_count))
            break

    u_defend()  # 用户防守
    # 判断用户防守后，能否提前结束比赛
    if u_count > c_count:
        if u_count - c_count > 4 - times and 4 - times != 0:
            print ("玩家提前获胜!")
            print ("比分 玩家_%d:电脑_%d" % (u_count, c_count))
            break
    else:
        if c_count - u_count > 4 - times and 4 - times != 0:
            print ("电脑提前获胜!")
            print ("比分 玩家_%d:电脑_%d" % (u_count, c_count))
            break

    times = times + 1
    print ("比分 玩家_%d:电脑_%d" % (u_count, c_count))

while u_count == c_count:
    # 当5轮比赛结束后，双方比分相同时，继续点球比赛
    print ("比分相同，继续下一轮")
    print ("-------第 %d 局--------" % (times + 1))
    u_attack()
    u_defend()
    times = times + 1
    print ("比分 玩家_%d:电脑_%d" % (u_count, c_count))

if u_count > c_count:
    print ("玩家获胜!")
else:
    print ("电脑获胜!")

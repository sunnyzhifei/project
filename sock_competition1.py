from random import randint

u_count=0
c_count=0
times=0

def u_attack():
    #用户进攻
    global u_count
    print("玩家请选择进攻方向[1,2,3,4,5]:")
    u_num=int(input())
    c_num=randint(1,5)
    print ("玩家进攻方向:%s" %u_num)
    print ("电脑防守方向:%s" %c_num)
    if u_num!=c_num:
        print ("球进了，玩家得1分")
        u_count=u_count+1
    else:
        print ("进攻失败")

def u_defend():
    #用户防守
    global c_count
    print ("玩家请选择防守方向[1,2,3,4,5]:")
    u_num=int(input())
    c_num=randint(1,5)
    print ("玩家防守方向:%s" %u_num)
    print ("电脑进攻方向:%s" %c_num)
    if u_num!=c_num:
        print ("防守失败，电脑的得1分")
        c_count = c_count + 1
    else:
        print ("防守成功")
while 1==1:
    #进行最基本的5次点球大战
    print ("-------第 %d 局--------" %(times+1
                                     ))
    u_attack() #用户进攻
    u_defend()#用户防守
    times=times+1
    print ("比分 玩家:电脑=%d：%d" %(u_count,c_count))
    if (u_count -c_count>=3 or  c_count -u_count>=3) and times==3:
        if u_count > c_count:
             print("玩家获胜!")
             break
        else:
            print("电脑获胜!")
            break
    elif (u_count -c_count>=2 or  c_count -u_count>=2) and times==4:
        if u_count > c_count:
            print("玩家获胜!")
            break
        else:
            print("电脑获胜!")
            break
    elif times>=5:
        if u_count > c_count:
             print("玩家获胜!")
             break
        elif u_count < c_count:
            print("电脑获胜!")
            break
        else:
            continue
    else:
        continue




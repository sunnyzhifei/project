# a=100
# b=int(input("please enter a number\n"))
# if b==a:
#     print("bingo")
# else:
#     print("a=%d,b=%d" %(a,b))
#
#
# a=int(input("please enter a number to 'a'\n "))
# b=int(input("please enter another number to 'b'\n" ))
# if a>b:
#     if a>10:
#         print("a>10")
#     else :
#         print ("a<=10")
# elif a<b:
#     if b<5:
#         print("b<5")
#     else :
#         print("b>=5")
# else:
#     print("无需比较")
#
#
# 小练习：猜数字游戏，增加游戏次数限制，最多只能猜5次。如果5次都没猜正确，给出提示
# a=10
# b=1
# while b<=5:
#     d=int(input("please enter a number\n"))
#     if d>a:
#         print("too big")
#         b=b+1
#     elif d<a:
#         print("too small")
#         b=b+1
#     else:
#         print("right")
#         b=6
# if  b>5:
#     if d!=a:
#         print("最多猜5次")
#

#
#     for i in range(1,10):
#         for j in range(1,i+1):
#             if j==5:
#                 continue
#             print("%d*%d=%d" %(i,j,i*j),end=" ")
#      print()

# def max(a,b):
#     if a>b:
#         print(a)
#     else :
#         print(b)
#
# max(15,10)


# def aa():
#     global x
#     x=10
#     print(x)
#
# x=5
# print(x)
# aa()

# def aa(c,b=3):
#     print(c*b)
# aa("hello")
#
# def max():
#     a=int(input("please enter a number"))
#     b=int(input("please enter a number"))
#     if a>b:
#         return a
#     else :
#         return b
# print(max())

# import random as sa
# def compare(a,b):
#     if a>b:
#         print("big")
#     elif a<b:
#         print("small")
#     else:
#         print("right")
# number=sa.randint(1,1)
# while  1==1:
#     c=int(input("please enter a number\n"))
#     compare(c,number)
#     if c==number:
#         break


from random import randint
def sa():
    global suma
    suma=0
    for c in range(1,3):
        a=randint(0,1)
        suma=suma+a
def sb():
    global sumb
    sumb=0
    for d in range(1,3):
        b=randint(0,1)
        sumb=sumb+b
sa()
sb()
times = 3
while 1==1:
    if abs(suma-sumb)<3 and times==3:
        x=randint(0, 1)
        suma=suma+x
        y=randint(0, 1)
        sumb=sumb+y
        times=times+1
    elif abs(suma-sumb)<2 and times==4:
        x=randint(0, 1)
        suma=suma+x
        y=randint(0, 1)
        sumb=sumb+y
        times=times+1
    else :
        if suma>sumb:
            print("A队和B队共比赛%d局" %times)
            print("A is winner")
            break
        elif suma<sumb:
            print("A队和B队共比赛%d局" %times)
            print("B is winner")
            break
        else :
            x=randint(0, 1)
            suma=suma+x
            y=randint(0, 1)
            sumb=sumb+y
            times=times+1



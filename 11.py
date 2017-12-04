a=95
b=int(input("请输入你认为的数字：\n"))
while (b!=a):
    if (b>a):
        b=int(input("too big,again:"))
    else:
       b=int(input("too small,again:"))
print("you win")
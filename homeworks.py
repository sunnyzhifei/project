#1、题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# n=0
# a=[]
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and i!=k and j!=k:
#                 a.append("%d%d%d" %(i,j,k))
#                 n=n+1
# print ("能组成互不相同且无重复数字的三位数的个数为： %d" %n)
# print("他们分别是：\n%s"%a)


# 2、题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
# 　　　于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
# 　　　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
# 　　　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
# 　　　100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# 1.程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。


# i=int(input("请输入当月利润(万元)\n"))
# a1=10*0.1
# a2=a1+100.075
# a4=a2+20*0.05
# a6=a4+20*0.03
# a10=a6+40*0.015
# if i <=10:
#     b=i*0.1
# elif i>10 and i<=20:
#     b=(i-10)*0.075+a1
# elif i>20 and i<=40:
#     b=a2+(i-20)*0.05
# elif i>40 and i<=60:
#     b=a4+(i-40)*0.03
# elif i>60 and i<=100:
#     b=a6+(i-60)*0.015
# else:
#     b=a10+(i-100)*0.01
#
# print("应发的总奖金为%.2f(万元)" %b)


# 题目：一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？
# 1.程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后的结果满足如下条件，即是结果。请看具体分析：

# from math import sqrt
# for i in range(1,100000):
#     a=int(sqrt(i+100))
#     b=int(sqrt(i+268))
#     if a*a==i+100 and b*b==i+268:
#         print(i)


# 题目：输入某年某月某日，判断这一天是这一年的第几天？

# year=int(input("year:\n"))
# month=int(input("month:\n"))
# day=int(input("day:\n"))
# sum=0
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
#
# if month>=1 and month<=12:
#     sum=int(months[month-1])
# else:
#     print("月份输入错误")
#
# sum=sum+day
# if year%4==0 and month>2:
#     sum=sum+1
# print("当天是%d年的第%d天" %(year,sum))



#5、题目：输入三个整数x,y,z，请把这三个数由小到大输出。

# x=int(input("请输入第一个整数"))
# y=int(input("请输入第二个整数"))
# z=int(input("请输入第三个整数"))
#
# if x>=max(y,z):
#     if y>=z:
#         print("三个数由小到大分别为%d<%d<%d" %(z,y,x))
#     else:
#         print("三个数由小到大分别为%d<%d<%d" % (y, z, x))
# elif y>=max(x,z):
#     if x>=z:
#         print("三个数由小到大分别为%d<%d<%d" % (z, x, y))
#     else:
#         print("三个数由小到大分别为%d<%d<%d" % (x, z, y))
# elif z>=max(x,y):
#     if x>=y:
#         print("三个数由小到大分别为%d<%d<%d" % (y, x, z))
#     else:
#         print("三个数由小到大分别为%d<%d<%d" % (x, y, z))



#6 题目：用*号输出字母C的图案

# print("          *  *")
# print("       *")
# print("    *")
# print("   *")
# print("  *")
# print("  *")
# print("  *")
# print("   *")
# print("     *")
# print("       *")
# print("         *  *")


# 7\题目：输出特殊图案，请在c环境中运行，看一看，Very Beautiful!

# 8\题目：输出9*9口诀。

# for i in range(1,10):
#     for j in range(1,10):
#         if j <=i:
#             print("%d*%d=%d" %(i,j,i*j),end=" ")
#     print()
#9、题目：要求输出国际象棋棋盘。

# 10、题目：打印楼梯，同时在楼梯上方打印两个笑脸。

# print("                   _-0-_")
# print("               _-0-_")
# print("            _-0-_")
# print("        _-0-_")
# print("     _-0-_")
# 11 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
# 后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

#1,1,2,3,5,8,13,

# f1 = 1
# f2 = 1
# for i in range(1,21):
#     print ('%12d %12d' % (f1,f2))
#     if (i % 2) == 0:
#         print ('')
#     f1 = f1 + f2
#     f2 = f1 + f2

# 12 题目：判断101-200之间有多少个素数，并输出所有素数。

for i in range(1,101):
    n=0
    for j in range(2,i):
        if i%j !=0:
            n=n+1
    if n==i-2:
        print(i)


# 【程序13】
# 题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数
# 　　　本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。

# for i in range(100,1000):
#     a=int(i/100)
#     b=int(i/10)%10
#     c=i%10
#     if a*a*a+b*b*b+c*c*c==i:
#         print(i)


# 【程序14】
# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。


# n = int(input("请输入一个正整数\n"))
# m=n
# x=[]
# if n < 0:
#     print("数据不满足要求")
# else:
#     a=[]
#     c=0
#     for i in range(2,n):
#         if n%i == 0:
#             a.append(i)
#             n=int(n/i)
#             b=0
#             c=c+1
#             for j in range(2,n):
#                 if n%j !=0:
#                     b=b+1
#             if n-2==b:
#                 c=c+1
#                 a.append(n)
#     print(a)
#     f=0
#     for k in a:



# x = []
# print('输入个啥：')
# n = int(input())
# for i in range(2,n + 1):
#     while n != i:
#         if n % i == 0:
#             x.append(i)
#             n = n / i
#         else:
#             break
# b = int(n)
# x.append(b)
# print (x)
# a=['1','2','3']
# x='*'.join(a)
# print(x)
#

# 【程序15】
# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

# n=int(input("请输入成绩"))
# if n>=90:
#     print("A")
# elif n>=60 and n<=89:
#     print("B")
# else :
#     print("C")

#【程序17】
#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# print("请输入一行字符")
# s=str(input())
# n=len(s)
# n1=0
# n2=0
# n3=0
# for i in s:
#     for j in range(26):
#         if i in (chr(j+ord("A")),chr(j+ord("a"))):
#                 n1+= 1
#     if i==" ":
#         n2+=1
#     else:
#         for j in range(0,10):
#             if i==str(j):
#                 n3+= 1
# n4=n-n1-n2-n3
# print("共输入%d个字符，其中英文字母%d个,空格%d个,数字%d个，其他字符%d个"  %(n,n1,n2,n3,n4))

#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

# a=int(input("请输入一个数字\n"))
# b=int(input("请输入相加的个数\n"))
# s=0
# for i in range(b):





#题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数。
#
# for n in range(2,1000):
#     m=1
#     k=n
#     for i in range(2,k):
#         if k%i==0:
#             m=m+i
#     if m==n:
#         print(n)

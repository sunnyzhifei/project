# # # 利用到目前为止的学习的知识点做一个程序练习（面向对象）：自动取款机（以文件形式存储用户数据-账号、密码、余额）（参考-案例3）
# # # 使用登录功能替代银行卡插卡动作，登录需正确校验账号和密码
# # # 登录成功后，可选择不同服务-查询余额、取款、转账、退出
# # # 取款需满足-取款金额以50为单位、账号余额充足、单笔限额1000
# # # 转账需满足-账号余额充足、单笔限额2000
# # from time import sleep
# #
# # '''
# # class User:
# #     #域-对象变量：name、password、money
# #     #1、登陆
# #     #2、选择服务
# #
# # class ATM:
# #     #域-类变量：保存正确的用户信息（用户名、密码、余额）
# #     #1、能够校验用户名
# #     #2、能够校验密码
# #     #3、能够校验金额
# #     #3.1、校验用户余额信息
# #     #4、能够查询登陆用户对应的余额信息
# #     #5、在用户取款完成后，调整用户余额信息
# #     #6、在用户完成转账后，调整转出方和转入方余额信息
# # '''
# #
# # class User:
# #     def __init__(self):
# #         self.name=0
# #         self.password=0
# #         self.money=0
# #
# #     def login(self):
# #         login_right=False
# #         while login_right==False:
# #             print("请输入用户名")
# #             self.name=input()
# #             print("请输入密码")
# #             self.password=int(input())
# #
# #             if ATM().get_username(self.name)==False:
# #                print("用户名错误")
# #             elif ATM().get_userpwd(self.name,self.password)==False:
# #                 print("密码错误")
# #             else :
# #                 login_right=True
# #
# #         print(self.name)
# #     def login_successfull(self):
# #         print("登录成功")
# #         print(self.name)
# #         is_quit=False
# #         while is_quit==False:
# #             print("请选择服务：1-查询余额 2-取款 3-转账 4-退出")
# #             num=int(input())
# #             if num == 1:
# #                 ATM().yue(self.name)
# #             if num == 2:
# #                 print("请输入取款金额")
# #                 self.money=int(input())
# #                 ATM().qukuan(self.name,self.money)
# #                 while 1==1:
# #                     if ATM().check_get_money(self.name,self.money)==1:
# #                         break
# #             if num == 3:
# #                 while 1==1:
# #                     print("请输入转账账户")
# #                     send_account=input()
# #                     ATM().check_send_account(send_account)
# #                     if self.send_account_is_right==True:
# #                         break
# #                 while 1==1:
# #                     print("请输入转账金额")
# #                     send_money=input()
# #                     ATM().check_send_money(send_account,send_money)
# #
# #             if num == 4:
# #                 is_quit == True
# #                 print("系统即将退出")
# #                 sleep(3)
# #
# #
# # class ATM:
# #     def __init__(self):
# #         self.open()
# #     def open(self):
# #         f=open("user_info.txt")
# #         ATM.account=f.readlines()
# #         f.close()
# #     def get_username(self,n1):
# #         name_is_right = False
# #         for i in ATM.account:
# #             l=i.split()
# #             if n1==l[0]:
# #                 name_is_right = True
# #                 break
# #         return name_is_right
# #
# #     def get_userpwd(self,n2,c):
# #         password_is_right = False
# #         for i in ATM.account:
# #             l=i.split()
# #             if n2==l[0] and c==int(l[1]):
# #                 password_is_right=True
# #         return password_is_right
# #
# #     def yue(self,n1):
# #         self.open()
# #         for i in ATM.account:
# #             l=i.split()
# #             if n1==l[0]:
# #                 print("您的余额为%s" % l[2])
# #                 break
# #
# #     def qukuan(self,n,m):
# #         k=0
# #         for i in ATM.account:
# #             l=i.split()
# #             if n==l[0]:
# #                 l[2]=str(int(l[2])-m)
# #                 ATM.account[k]=" ".join(l)+"\n"
# #                 break
# #             k=k+1
# #         f=open("user_info.txt" "w")
# #         f.writelines(ATM.account)
# #         f.close()
# #         print("取款成功")
# #     def check_get_money(self,n,m):
# #         if m%50==0:
# #             print("取款金额必须以50为单位")
# #         elif ATM().yue(self.name)<m:
# #             print("您的余额不足")
# #         elif m>1000:
# #             print("单笔限额1000元")
# #         else:
# #             return 1
# #
# #     def check_send_account(self,s):
# #         self.send_account_is_right=False
# #         for i in ATM.account:
# #             l=i.split()
# #             if s==l[0]:
# #                 self.send_account_is_right=True
# #                 break
# #             return self.send_account_is_right
# #         if self.send_account_is_right==False:
# #             print("对方账户不存在,请重新输入")
# #
# #         def check_send_money(self,m):
# #             if ATM().yue(self.name) < m:
# #                 print("您的余额不足")
# #             elif m > 2000:
# #                 print("单笔限额2000元")
# #             else:
# #                 return 1
# #
# #
# # User().login()
# # User().login_successfull()
#
# from time import sleep
#
# class User:
#     def __init__(self):
#         self.name=0
#         self.password=0
#         self.money=0
#
#
#     def login(self):
#         loginstatus = False
#         while loginstatus==False:
#             print("请输入用户名")
#             self.name=input()
#             print("请输入密码")
#             self.password=int(input())
#
#             if atm.get_username(self.name)==False:
#                print("用户名错误")
#             elif atm.get_userpwd(self.name,self.password)==False:
#                 print("密码错误")
#             else :
#                 loginstatus = True
#
#
#     def login_successfull(self):
#         print("登录成功")
#         is_quit=False
#         while is_quit==False:
#             print("请选择服务：1-查询余额 2-取款 3-转账 4-退出")
#             num=int(input())
#             if num == 1:
#                atm.yue(self.name)
#             if num == 2:
#                 print("请输入取款金额")
#                 self.money=int(input())
#                 if atm.check_get_money(self.name,self.money)==True:
#                     atm.qukuan(self.name,self.money)
#
#
#             if num == 3:
#                 while 1==1:
#                     print("请输入转账账户")
#                     send_account=input()
#                     atm.check_send_account(send_account)
#                     if self.send_account_is_right==True:
#                         break
#                 while 1==1:
#                     print("请输入转账金额")
#                     send_money=input()
#                     atm.check_send_money(send_account,send_money)
#
#             if num == 4:
#                 print("系统即将退出")
#                 sleep(3)
#
#
# class ATM:
#     def __init__(self):
#         self.open()
#     def open(self):
#         f=open("user_info.txt")
#         ATM.account=f.readlines()
#         f.close()
#     def get_username(self,n):
#         name_is_right = False
#         for i in ATM.account:
#             l=i.split()
#             if n==l[0]:
#                 name_is_right = True
#                 break
#         return name_is_right
#
#     def get_userpwd(self,n,c):
#         password_is_right = False
#         for i in ATM.account:
#             l=i.split()
#             if n==l[0] and c==int(l[1]):
#                 password_is_right=True
#         return password_is_right
#
#     def yue(self,n1):
#         self.open()
#         l=[]
#         for i in ATM.account:
#             l=i.split()
#             if n1==l[0]:
#                 print("您的余额为%s" % l[2])
#                 break
#         return l[2]
#
#     def qukuan(self,n,m):
#         k=0
#         for i in ATM.account:
#             l=i.split()
#             if n==l[0]:
#                 l[2]=str(int(l[2])-m)
#                 ATM.account[k]=" ".join(l)+"\n"
#                 break
#             k=k+1
#         f=open("user_info.txt","w")
#         f.writelines(ATM.account)
#         f.close()
#         print("取款成功")
#     def check_get_money(self,n5,m5):
#         get_money_isright=False
#         if m5%50!=0:
#             print("取款金额必须以50为单位")
#         elif atm.yue(n5)<m5:
#             print("您的余额不足")
#         elif m5>1000:
#             print("单笔限额1000元")
#         else:
#             get_money_isright=True
#         return get_money_isright
#
#     def check_send_account(self,s):
#         self.send_account_is_right=False
#         for i in ATM.account:
#             l=i.split()
#             if s==l[0]:
#                 self.send_account_is_right=True
#                 break
#             return self.send_account_is_right
#         if self.send_account_is_right==False:
#             print("对方账户不存在,请重新输入")
#
#         def check_send_money(self,m):
#             if ATM().yue(self.name) < m:
#                 print("您的余额不足")
#             elif m > 2000:
#                 print("单笔限额2000元")
#             else:
#                 return 1
#
# user=User()
# atm=ATM()
# user.login()
# user.login_successfull()





#一份文件中保存的是各位同学的各科成绩，编写程序计算出各位同学的总成绩写入文件中每行末尾
import os

t=['张三 90 90 80\n','李四 90 100 90\n','王五 90 80 70\n']
f=open("test.txt","w+")
f.writelines(t)

#f.close()
f=open("test.txt")
x=f.readlines()

l=[]
n=0
for i in x:
    l=i.split( )
    #print(l)
    sum1=int(l[1])+int(l[2])+int(l[3])
    l.append(str(sum1))
    x[n]=(" ").join(l)+'\n'
    n=n+1
print(x)

f=open("test.txt","w")
f.writelines(x)


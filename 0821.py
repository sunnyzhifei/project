# names=['TOM','JHON']
# Names=[i+'\n'for i in names]
# print(Names)

# class Persion():
#
#     from random import choice
#     __num=choice(['我','是','大','神'])
#     def __init__(self, ss):
#         self.name=ss
#     def aa(self):
#         print('my name is %s' %self.name)
#         print("%s" %Persion.__num)
# Persion("lizhifei").aa()


# 假如有一辆汽车，速度是60km/h，从A地行驶到B地（距离100km），计算耗费的时间，分别以面向过程、面向对象两种不同的编程思想设计程序

#再假设换一辆汽车，速度是100km/h，从A地行驶到C地（距离350km）,计算耗费的时间，考虑在原有的代码基础上应该如何调整

# distance=100
# speet=60
# time=float(distance/speet)
# print('time of A to B is %.2f hour' %time)
# print()
#
# class che:
#     def __init__(self,s,d):
#         self.s=s
#         self.d=d
#         print("当前的速度是%d" %s)
#         print("当前的距离是%d" %d)
#     def time(self):
#         t=float(self.d/self.s)
#         print('还有%.2f小时到达目的地' %t)
#
# x=Car(60,100)
# x.time()


# class Animal():
#     def eat(self):
#         print("animal can eat")
#     def  sleep(self):
#         print("animal can sleep")
# class Animal2(Animal):
#     def drink(self):
#         print("animal can drink")
#
# Animal2().drink()
# Animal2().eat()


# 还是从A地出发去B地（距离100km）, 这次除了可以使用汽车，还有另外一种方式 - 自行车，汽车速度60km / h, 自行车速度20km / h，计算耗时
# 同时针对汽车，这次再增加一个属性 - 油耗，每公里0 .1升的耗油量，输出到达目的地汽车总油耗
#提示：汽车和自行车都具有“速度”这样的域，同时具有相同的方法“行驶”，因此可以创建具备这两个属性的超类“车”

# class Che:
#     def __init__(self,s,d):
#         self.s=s
#         self.d=d
#         print("当前的速度是%d" %s)
#         print("当前的距离是%d" %d)
#     def time(self):
#         t=float(self.d/self.s)
#         print('还有%.2f小时到达目的地' %t)
# class Car(Che):
#     def you(self):
#         y=self.d*0.1
#         print("汽车总油耗是%d" %y)
# class Bicycle(Che):
#     pass
#
# x=Car(60,100)
# x.time()
# x.you()
# z=Bicycle(20,100)
# z.time()



# 利用到目前为止的学习的知识点做一个程序练习（面向对象）：自动取款机（以文件形式存储用户数据-账号、密码、余额）（参考-案例3）
# 使用登录功能替代银行卡插卡动作，登录需正确校验账号和密码
# 登录成功后，可选择不同服务-查询余额、取款、转账、退出
# 取款需满足-取款金额以50为单位、账号余额充足、单笔限额1000
# 转账需满足-账号余额充足、单笔限额2000

# 利用到目前为止的学习的知识点做一个程序练习（面向对象）：自动取款机（以文件形式存储用户数据-账号、密码、余额）（参考-案例3）
# 使用登录功能替代银行卡插卡动作，登录需正确校验账号和密码
# 登录成功后，可选择不同服务-查询余额、取款、转账、退出
# 取款需满足-取款金额以50为单位、账号余额充足、单笔限额1000
# 转账需满足-账号余额充足、单笔限额2000
from time import sleep

'''
class User:
    #域-对象变量：name、password、money
    #1、登陆
    #2、选择服务

class ATM:
    #域-类变量：保存正确的用户信息（用户名、密码、余额）
    #1、能够校验用户名
    #2、能够校验密码
    #3、能够校验金额
    #3.1、校验用户余额信息
    #4、能够查询登陆用户对应的余额信息
    #5、在用户取款完成后，调整用户余额信息
    #6、在用户完成转账后，调整转出方和转入方余额信息
'''


class User:
    def __init__(self):
        self.name = 0
        self.password = 0
        self.money = 0

    def login(self):
        # 验证是否能成功登陆
        login_right = False
        while login_right == False:
            print("请输入用户名:")
            self.name = input()
            print("请输入密码:")
            self.password = input()

            if atm.get_user_name(self.name) == False:
                print("用户名错误!请重新输入")
            elif atm.get_user_password(self.name, self.password) == False:
                print("密码错误!请重新输入")
            else:
                login_right = True

    def login_success(self):

        print("成功登陆")
        is_quit = False
        while is_quit == False:
            print("请选择所需服务[1-查询余额 2-取款 3-转账 0-退出]:")
            num = int(input())
            # atm=ATM()#创建ATM对象
            if num == 1:
                atm.show_user_money(self.name)
                sleep(1)
            elif num == 2:
                print("请输入取款金额：")
                self.money = input()
                if atm.check_money1(self.name, self.money) == True:
                    atm.change_user_money(self.name, self.money)
                    atm.show_user_money(self.name)
                    sleep(1)
            elif num == 3:
                print("请输入收款方账户：")
                s_name = input()
                if atm.get_user_name(s_name) == False:
                    print("收款方不存在")
                else:
                    print("请输入转账金额：")
                    self.money = input()
                    if atm.check_money2(self.name, self.money) == True:
                        atm.move_user_money(self.name, self.money, s_name)
                        atm.show_user_money(self.name)
                        sleep(1)
            else:
                print("系统即将退出")
                is_quit = True


class ATM:
    user_info = 0

    # 初始化
    def __init__(self):
        self.get_userinfo()

    # 读取文件中的用户信息
    def get_userinfo(self):
        f = open("user_info.txt")
        ATM.user_info = f.readlines()
        f.close()

    # 校验用户姓名
    def get_user_name(self, n1):
        name_is_right = False
        for user1 in ATM.user_info:
            l_user1 = user1.split()
            if n1 == l_user1[0]:
                name_is_right = True
                break
        return name_is_right

    # 校验用户密码
    def get_user_password(self, n2, p2):
        password_is_right = False
        for user2 in ATM.user_info:
            l_user2 = user2.split()
            if n2 == l_user2[0] and p2 == l_user2[1]:
                password_is_right = True
                break
        return password_is_right

    # 校验余额
    def get_user_money(self, n3, m3):
        money_is_right = False
        for user3 in ATM.user_info:
            l_user3 = user3.split()
            if n3 == l_user3[0] and int(m3) <= int(l_user3[2]):
                money_is_right = True
                break
        return money_is_right

    # 显示余额
    def show_user_money(self, n6):
        self.get_userinfo
        for user6 in ATM.user_info:
            l_user6 = user6.split()
            if n6 == l_user6[0]:
                print("余额: %s" % l_user6[2])
                break

    # 取款处理
    def change_user_money(self, n4, m4):
        k = 0
        for user4 in ATM.user_info:
            l_user4 = user4.split()
            if n4 == l_user4[0]:
                l_user4[2] = str(int(l_user4[2]) - int(m4))
                ATM.user_info[k] = ' '.join(l_user4) + '\n'
                break
            k = k + 1
        f4 = open('user_info.txt', 'w')
        f4.writelines(ATM.user_info)
        f4.close()

        print("取款成功，请取走钞票!")

    # 取款金额校验
    def check_money1(self, n4, m4):
        money1_is_right = False
        if int(m4) % 50 != 0:
            print("金额必须以50为单位.")
        elif int(m4) > 1000:
            print("单笔限额必须小于1000.")
        elif self.get_user_money(n4, m4) == False:
            print("余额不足.")
        else:
            money1_is_right = True
        return money1_is_right

    # 转账处理
    def move_user_money(self, n5, m5, n5_1):
        k = 0
        for user5 in ATM.user_info:
            l_user5 = user5.split()
            if n5 == l_user5[0]:
                l_user5[2] = str(int(l_user5[2]) - int(m5))
                ATM.user_info[k] = ' '.join(l_user5) + '\n'
                break
            k = k + 1
        k = 0
        for user5 in ATM.user_info:
            l_user5 = user5.split()
            if n5_1 == l_user5[0]:
                l_user5[2] = str(int(l_user5[2]) + int(m5))
                ATM.user_info[k] = ' '.join(l_user5) + '\n'
                break
            k = k + 1
        f4 = open('user_info.txt', 'w')
        f4.writelines(ATM.user_info)
        f4.close()

        print("转账成功!")

    # 转账金额校验
    def check_money2(self, n5, m5):
        money2_is_right = False
        if int(m5) > 2000:
            print("单笔转账限额必须小于2000.")
        elif self.get_user_money(n5, m5) == False:
            print("余额不足.")
        else:
            money2_is_right = True
        return money2_is_right


# 程序开始执行---
atm = ATM()  # 找到一台ATM
u = User()  # 有用户来使用
u.login()  # 用户登陆
u.login_success()  # 成功登陆，选取服务

sleep(3)





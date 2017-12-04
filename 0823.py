# import pymysql
# conn=pymysql.connect(host='192.168.246.129',user='root',password='Lzf1258',db='learn',charset='utf8',port=3306)
# cur=conn.cursor()
# data=cur.execute("select * from dept")
# c=cur.fetchall()
# # print(data)
# # print(c)
# cur.callproc('pro_2',args=(7369,))
# result=cur.fetchall()
# print(result)
# # cur.callproc('pro_2',7369)
# # result1=cur.fetchall()
# # print(result1)
# conn.commit()
# conn.close()


#
# import copy
#
# a=[[1],[2],[3,2]]
#
# b=copy.copy(a)
# c=copy.deepcopy(a)
#
# a[2][1]=0
#
# print(a)
# print(b)
# print(c)

# import time
# now=time.localtime()
# print(now)
# a=time.strftime("%y/%m/%d %H:%M",now)
# print(a)



import re
text="Hi,nyss nam1 name@is lizhifeSi,WO"
m=re.findall(r"e\Bi",text)
if m:
    print (m)
    # print(m.group(0))
    # print(m.group(1))
    # print (m.group(2))
    # print(m.group(3))
    # print(m.group(4))
    # print(m.group(5))
else:
    print("something is wrong")
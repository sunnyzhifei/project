# import urllib.request  as url
# data=url.urlopen("http://www.youku.com")
# c=data.read()
# code=c.decode("utf8")
# print(code)

import urllib.request as url

# r=url.get("http://music.163.com/#/song?id=500353026")
#
# arr=r.json()["result"]["tracks"]
# for i in range(10):
#     name=str(i+1)+" "+arr[i]["name"]+".mp3"
#     link=arr[i]["mp3Url"]
#     url.urlretrieve((link,'网易云音乐\\'+name))
#     print(name+"下载完成")

# import urllib.request as re
# def report(a,b,c):
#     f=100*a*b/c
#     if f>100:
#         f=100
#     print("%.2f%%" %f)
#
# re.urlretrieve("http://www.baidu.com","g:\\test",report)

# import os
# import urllib.request as re
# def report(a,b,c):
#     f=100*a*b/c
#     if f>100:
#         f=100
#     print("%.2f%%" %f)
# url1="https://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2"
# dir=os.path.abspath("g:\\.")
# work_path=os.path.join(dir,"python-2.tar.bz2")
# re.urlretrieve(url1,work_path,report)

#
# import socket
# sk=socket.socket()
# sk.bind(("192.168.6.68",8880))
# sk.listen(5)
# while True:
#     conn, addr = sk.accept()
#     while True:
#         a=conn.recvfrom(1024)
#         b=str(a[0],encoding="utf-8")
#         print("接收到的信息： %s" %b)
#         print(a[1])
#         if b=="byebye":
#             break
#         else:
#             c=input("请输入回应信息\n")
#             conn.sendto(bytes(str(c),encoding="utf-8"),a[1])
#     conn.close()

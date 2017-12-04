# import socket
# sk=socket.socket()
# sk.connect(("192.168.6.68",8880))
# while True:
#     send_data=input("请输入需要发送的信息\n")
#     sk.sendall(bytes(send_data,encoding="utf-8"))
#     if send_data=="byebye":
#         break
#     accpt_data=sk.recv(1024)
#     c=str(accpt_data,encoding="utf-8")
#     print("接收的内容是%s" %c)
#
# sk.close()




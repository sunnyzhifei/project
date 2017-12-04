f=open("C:/Users/Administrator/Desktop/登录数据.txt")
x=f.readlines()
f.close()

for i in x[1:]:
    l=i.split(" ")
    print(l)

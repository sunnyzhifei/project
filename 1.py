#一份文件中保存的是各位同学的各科成绩，编写程序计算出各位同学的总成绩写入文件中每行末尾
import os

t=['张三 90 100 80\n','李四 90 100 80\n','王五 90 100 80\n']
f=open("test.txt","w+")
f.writelines(t)

#f.close()
f=open("test.txt")
zhaolan=f.readlines()
print(zhaolan)
l=[]
n=0
for i in zhaolan:
    l=i.split( )
    print(l)
    sum1=int(l[1])+int(l[2])+int(l[3])
    l.append(str(sum1))
    "".join(l)
    print(l)
    zhaolan[n]=l
    "".join(zhaolan[n])
    n += 1
#print(zhaolan)

#(" ").join(zhaolan[0])
#print(zhaolan[0])
#f=open("test.txt","w+")
#f.write(zhaolan)
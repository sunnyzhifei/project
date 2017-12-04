# list=[1,2,3,2,1,"abc"]
# tuple=(3,3,7,7,66,8,'abc')
# tuple1=()
# tuple2=(9,)
# dict1={'a':1,'b':2,'c':3}
#
# for  i in list:
#     for j in tuple:
#         if i==j:
#             print("%s" %j,end=' ')
# print()
#
# del list[0]
# print(list)
# del dict1['a']
# print(dict1)


# f=open('121.py','w')
# x=f.write('welcome to my home 中文')
# f.close()
#
# f=open('121.txt','w')
# f.write('中文shurufa12313')
# f=open('121.txt')
# x=f.read()
# print(x)
# f.close()
#

# f=open('121.txt')
# x=f.read()
# print(x)
#
# f=open('222.txt','a')
# f.write(x)
# f.close()
# f=open('222.txt')
# y=f.read()
# print(y)
# f.close()


o=open('student_info.txt')
r=o.read()
print(r)
a=r.split('\n')
print(a)
z=a[0].split( )
l=a[1].split( )
w=a[2].split( )
print(z)
print(l)
print(w)
sumz=str(int(z[1])+int(z[2])+int(z[3]))
suml=str(int(l[1])+int(l[2])+int(l[3]))
sumw=str(int(w[1])+int(w[2])+int(w[3]))
z.append(sumz)
l.append(suml)
w.append(sumw)
print(z)
print(l)
print(w)

z1=' '.join(z)
l1=' '.join(l)
w1=' '.join(w)
print(z1)
print(l1)
print(w1)

f1=open('student_info1.txt','w')
f1.writelines(z1)
f1.close()
f2=open('student_info1.txt','a')
f2.writelines('\n')
f2.close()
f2=open('student_info1.txt','a')
f2.writelines(l1)
f2.close()
f3=open('student_info1.txt','a')
f3.writelines('\n')
f3.close()
f3=open('student_info1.txt','a')
f3.writelines(w1)
f3.close



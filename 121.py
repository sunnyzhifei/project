try:
    n=int(input("请输入一个数字\n"))
    raise ValueError
    if n >10:
        print('too big')
    if n <=10:
        print('too small')
except ValueError:
    print('not in scope')








#
# o=open('student_info.txt')
# r=o.read()
# print(r)
# a=r.split('\n')
# print(a)
# z=a[0].split( )
# l=a[1].split( )
# w=a[2].split( )
# print(z)
# print(l)
# print(w)
# sumz=str(int(z[1])+int(z[2])+int(z[3]))
# suml=str(int(l[1])+int(l[2])+int(l[3]))
# sumw=str(int(w[1])+int(w[2])+int(w[3]))
# z.append(sumz)
# l.append(suml)
# w.append(sumw)
# print(z)
# print(l)
# print(w)
#
# z1=' '.join(z)
# l1=' '.join(l)
# w1=' '.join(w)
# print(z1)
# print(l1)
# print(w1)
#
#


# f1=open('student_info1.txt','w')
# f1.writelines(z1)
# f1.close()
# f2=open('student_info1.txt','a')
# f2.writelines('\n')
# f2.close()
# f2=open('student_info1.txt','a')
# f2.writelines(l1)
# f2.close()
# f3=open('student_info1.txt','a')
# f3.writelines('\n')
# f3.close()
# f3=open('student_info1.txt','a')
# f3.writelines(w1)
# f3.close
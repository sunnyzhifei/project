from time import sleep

#读取文件中的各行数据，并存放到l列表中
f=open('student_info.txt',encoding='utf-8')
l=f.readlines()
#print (l)
f.close()

#将l列表中的各个元素分别处理，将每个元素中的成绩信息汇总算出总成绩
m=0
for i in l:
    l1=i.split() #将通过遍历提取出来的文件中一行数据从字符串格式转换成列表
    sum=int(l1[1])+int(l1[2])+int(l1[3])#从列表中提取成绩信息，计算总成绩
    l1.append(str(sum))#把总成绩追加到列表中

    l[m]=' '.join(l1)+'\n'#把列表转换成字符串，同时用新的字符串将原有字符串替换
    #print (l[m])

    m=m+1 #计数器

#print (l)

#将修改好的l列表写回文件中
f=open('student_inf2.txt','w',encoding='utf-8')
f.writelines(l)
f.close()


#读取文件，查看结果是否正确
f=open('student_info2.txt',encoding='utf-8')
print(f.read())
f.close()

sleep(3)


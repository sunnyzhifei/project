from time import sleep

#��ȡ�ļ��еĸ������ݣ�����ŵ�l�б���
f=open('student_info.txt',encoding='utf-8')
l=f.readlines()
#print (l)
f.close()

#��l�б��еĸ���Ԫ�طֱ�����ÿ��Ԫ���еĳɼ���Ϣ��������ܳɼ�
m=0
for i in l:
    l1=i.split() #��ͨ��������ȡ�������ļ���һ�����ݴ��ַ�����ʽת�����б�
    sum=int(l1[1])+int(l1[2])+int(l1[3])#���б�����ȡ�ɼ���Ϣ�������ܳɼ�
    l1.append(str(sum))#���ܳɼ�׷�ӵ��б���

    l[m]=' '.join(l1)+'\n'#���б�ת�����ַ�����ͬʱ���µ��ַ�����ԭ���ַ����滻
    #print (l[m])

    m=m+1 #������

#print (l)

#���޸ĺõ�l�б�д���ļ���
f=open('student_inf2.txt','w',encoding='utf-8')
f.writelines(l)
f.close()


#��ȡ�ļ����鿴����Ƿ���ȷ
f=open('student_info2.txt',encoding='utf-8')
print(f.read())
f.close()

sleep(3)


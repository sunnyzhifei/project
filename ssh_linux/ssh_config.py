import paramiko
import re

#import Crypto
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.0.103",22,"root", "Lzf1111")
stdin, stdout, stderr = ssh.exec_command("ip addr")
x=stdout.read()
print x
f={}
ll = []
# f=re.split(r'\s',x)

# print re.split(r'\n',x,re.S)
list=re.split(r'\n',x,re.S)
n=0
flag=0
name=''
for i in list:
    n=n+1
    value=re.findall(r'\w+:\s(<.+)',i)
    if re.search(r'\w+:\s<.+',i):
        flag=n
        ll = []
        ll.append(''.join(value))
        name = ''.join(re.findall(r'(\w+):\s<',i))
        f[name]=ll
    else:
        ll.append(i)
        f[name]=ll
print f

print f['lo']
ssh.close()
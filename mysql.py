import pymysql
conn=pymysql.connect(host='localhost',port=3306,db='zhaolan',user="root",password="1",charset='utf8')
#print(conn)
cur=conn.cursor()
# cur.execute('''
# create table love(
# id int(10),
# name varchar(20)
# )charset='utf8'
# '''
#cur.execute("insert into love values(1,'lizhifei');")

#cur.execute("select * from love;")
values=[]
for i in range (10):
   value=(str(i),"admin"+str(i))
   values.append(value)
cur.executemany("insert into love values (%s,%s)",values)
#print(cur.fetchall())
cur.execute("select * from love;")
print(cur.fetchall())
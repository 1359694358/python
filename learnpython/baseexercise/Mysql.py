import pymysql
con=pymysql.connect(host="localhost", user="root", password="Qvbvjai1989!",
                 database="test")
print(con)

cur=con.cursor()
cur.execute("create table  IF not exists test1 (id int(20) primary key ,name varchar(30) )")
# cur.execute("insert into test1 values(2,'zouxudong')")
# con.commit()
cur.execute("select * from test1")
result=cur.fetchall()
print(result,type(result))
cur.close()
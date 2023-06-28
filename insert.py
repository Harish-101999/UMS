import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='Hari@1432'
)

cur=conn.cursor()

class insert:
    def deptinsert(x,deptid,deptname):
        cur.execute(f"insert into department values({deptid},'{deptname}')")
        conn.commit()

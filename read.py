import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='Hari@1432'
)

cur=conn.cursor()

class read:
    def deptread(x,id):
        cur.execute(f"select * from department where departmentid={id}")
        conn.fetchall()
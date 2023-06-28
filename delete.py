import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='Hari@1432'
)

cur=conn.cursor()

class deleted:
    def deptdelete(x,id):
        cur.execute(f"delete from department where departmentid={id}")
        conn.commit()

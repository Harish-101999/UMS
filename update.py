import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='Hari@1432'
)

cur=conn.cursor()

class updated:
    def dptupdate(x,colname,newval,oldval):
        cur.execute(f"update department set {colname}='{newval}' where {colname}='{oldval}'")
        conn.commit()
obj=updated()
obj.dptupdate('departmentname','JAVA','python')


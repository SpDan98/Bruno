import sqlite3
import hashlib

# """insert into Products(name,price,category) values ('курица',500,1)"""
# """insert into Products(name,price,category) values ('яблоки',100,2)"""
# """insert into Products(name,price,category) values ('помидоры',150,3)"""
# """insert into Products(name,price,category) values ('черный хлеб',50,4)"""



# conn=sqlite3.connect('lesson10/products.db')
# cur=conn.cursor()
# cur.execute("""insert into Products(name,price,category) values ('черный хлеб',50,4)""")
# conn.commit()
# conn.close()


# conn=sqlite3.connect('lesson10/products.db')
# cur=conn.cursor()
# data=cur.execute(f"""SELECT * from Products join Category on Products.category=Category.id   """).fetchall()
# print(data)
# conn.commit()
# conn.close()

shpass=hashlib.sha256(b'pavel123')
data=('Pavel',str(shpass.hexdigest()))
conn=sqlite3.connect('lesson10/products.db')
cur=conn.cursor()
cur.execute("""insert into Users(login,password) values (?,?)""",data)
conn.commit()
conn.close()

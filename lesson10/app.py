import sys
import sqlite3
import hashlib

def signin(data):
    conn=sqlite3.connect('products.db')
    cur=conn.cursor()
    d=cur.execute(f"""select * from Users where Users.login='{data[0]}' and Users.password='{data[1]}' """).fetchall()
    conn.close()
    if d:
        return True
    else:
        return False
    
def signup(data):
    print(data[0],data[1])
    conn=sqlite3.connect('products.db')
    cur=conn.cursor()
    try:
        newdata=data[0],hashlib.sha256(data[1].encode('utf-8')).hexdigest()
        cur.execute(f"""insert into Users(login,password) values(?,?) """,newdata).fetchall()
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
    

if __name__=='__main__':
    if sys.argv[1]=='signin':
        if signin(('Dan21',str(hashlib.sha256(b'dan12421').hexdigest()))):
            print('ok')
        else:
            print('neok')
    elif sys.argv[1]=='signup':
        signup(('Dan21','dan12421'))
    else:
        print('no')
       


import hashlib
import sqlite3


def register(username, passwd, confirm_passwd):
    con = sqlite3.connect("account.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS 'login' (Username VARCHAR, Password VARCHAR)")
    con.commit()
    
    user_exist = f"SELECT Username from login WHERE Username='{username}'"
    cur.execute(user_exist)
    if cur.fetchone():
        return 1
    
    if passwd != confirm_passwd:
        return 2

    hashing = passwd.encode()
    hexformat = hashlib.md5(hashing).hexdigest()

    query = "INSERT INTO login (Username, Password) VALUES (?, ?)"
    cur.execute(query, (username, hexformat))
    con.commit()

    cur.close()
    con.close()
    return 0

def login(username, passwd):
    con = sqlite3.connect("account.db")
    cur = con.cursor()

    hashing = passwd.encode()
    hexformat = hashlib.md5(hashing).hexdigest()
    
    user_exist = f"SELECT Username from login WHERE Username='{username}'"
    verify = f"SELECT Username from login WHERE Username='{username}' AND Password = '{hexformat}';"

    cur.execute(user_exist)
    if cur.fetchone():
        cur.execute(verify)
        if cur.fetchone():
            cur.close()
            con.close()
            return 0
        else:
            cur.close()
            con.close()
            return 1
    else:
        return 2

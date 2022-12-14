import hashlib
import sqlite3
import os.path


def register(username, passwd, confirm_passwd):
    conn = sqlite3.connect("account.db")
    cursor = conn.cursor()

    if os.path.exists("./account.db") == False:
        cursor.execute("DROP TABLE IF EXISTS login")
        conn.commit()
        
        cursor.execute("CREATE TABLE login(Username VARCHAR UNIQUE, Password VARCHAR)")
        conn.commit()
    
    sql = 'SELECT EXISTS (SELECT 1 FROM login WHERE Username = ?)'
    cursor.execute(sql, (username,))
    if cursor.fetchone()[0]:
        return 1
    
    if passwd != confirm_passwd:
        return 2

    hashing = passwd.encode()
    hexformat = hashlib.md5(hashing).hexdigest()

    query = "INSERT INTO login (Username, Password) VALUES (?, ?)"
    cursor.execute(query, (username, hexformat))
    conn.commit()

    cursor.close()
    conn.close()
    return 0

def check(username, passwd):
    conn = sqlite3.connect("account.db")
    cursor = conn.cursor()

    sql = 'SELECT EXISTS (SELECT 1 FROM login WHERE Username = ?)'
    cursor.execute(sql, (username,))
    if cursor.fetchone()[0]:
        hashing = passwd.encode()
        hexformat = hashlib.md5(hashing).hexdigest()
    
        query = 'SELECT * FROM login WHERE Username = ? AND Password = ?'
        cursor.execute(query, (username, hexformat))
        result = cursor.fetchone()
        conn.commit()
        print('[DEBUG][check] result:', result)
    
        cursor.close()
        conn.close()
        return result
    else:
        cursor.close()
        conn.close()
        return 2

def login(username, passwd):
    if check(username, passwd):
        return 0
    else:
        return 1


import hashlib
import sqlite3


# initialize account database
def create_table():
    con = sqlite3.connect("account.db")
    cur = con.cursor()

    # create table for logins
    cur.execute("CREATE TABLE IF NOT EXISTS 'accounts' (Username VARCHAR, Password VARCHAR, Admin BOOLEAN)")
    con.commit()

    # create admin account
    register("admin", "admin", "admin", admin=True)

    cur.close()
    con.close()


# register accoun to account.db
def register(username, passwd, confirm_passwd, admin=False):
    con = sqlite3.connect("account.db")
    cur = con.cursor()

    # verify if user exist
    user_exist = f"SELECT Username from accounts WHERE Username='{username}'"
    cur.execute(user_exist)
    if cur.fetchone():
        cur.close()
        con.close()
        return 1
    
    # compare pass and confirm pass
    if passwd != confirm_passwd:
        cur.close()
        con.close()
        return 2

    # code hashing
    hashing = passwd.encode()
    hexformat = hashlib.md5(hashing).hexdigest()

    # record data to database
    query = "INSERT INTO accounts (Username, Password, Admin) VALUES (?, ?, ?)"
    cur.execute(query, (username, hexformat, admin))
    con.commit()

    cur.close()
    con.close()
    return 0


# verify account login details
def login(username, passwd):
    con = sqlite3.connect("account.db")
    cur = con.cursor()

    # hash password to match password in database
    hashing = passwd.encode()
    hexformat = hashlib.md5(hashing).hexdigest()
    
    user_exist = f"SELECT Username from accounts WHERE Username='{username}'"
    verify = f"SELECT Username from accounts WHERE Username='{username}' AND Password = '{hexformat}';"

    # check if user exist
    cur.execute(user_exist)
    if cur.fetchone():
        # verify matching input to password
        cur.execute(verify)
        # login
        if cur.fetchone():
            cur.close()
            con.close()
            return 0
        # wrong password
        else:
            cur.close()
            con.close()
            return 1
    # user not registered
    else:
        cur.close()
        con.close()
        return 2

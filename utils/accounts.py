from utils import randompic
import hashlib
import sqlite3

database_file = "invento.db"

def create_table():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS accounts (Username VARCHAR, Password VARCHAR, Admin BOOLEAN)")
        cur.execute("CREATE TABLE IF NOT EXISTS sessions (Username VARCHAR)")
        cur.execute("SELECT * FROM accounts WHERE Username = 'admin' AND Admin = 1")
        if not cur.fetchone(): # if admin is not in the accounts table
            cur.execute("INSERT INTO accounts (Username, Password, Admin) VALUES (?, ?, ?)", ("admin", hashlib.md5(b"admin").hexdigest(), True))
            randompic.generate_box_image("admin")
        con.commit()


def register(username, passwd, confirm_passwd, admin=False):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT Username from accounts WHERE Username=?", (username,))
        if cur.fetchone():
            return 1    # username already exists
        if passwd != confirm_passwd:
            return 2    # password and confirm password don't match
        cur.execute("INSERT INTO accounts (Username, Password, Admin) VALUES (?, ?, ?)", (username, hashlib.md5(passwd.encode()).hexdigest(), admin))
        con.commit()
        randompic.generate_box_image(username)
        return 0        # success


def login(username, passwd):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT * from accounts WHERE Username=? AND Password=?", (username, hashlib.md5(passwd.encode()).hexdigest()))
        if cur.fetchone():
            cur.execute("INSERT INTO sessions (Username) VALUES (?)", (username,))
            return 0    # if user and passwd match
        cur.execute("SELECT * from accounts WHERE Username=?", (username,))
        if cur.fetchone():
            return 1    # if user exists but incorrect passwd
        return 2        # if user account doesn't exist


def get_session():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT Username FROM sessions")
        result = cur.fetchone()
        return result[0] if result else None


def logout():
    if get_session():
        with sqlite3.connect(database_file) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM sessions")
            con.commit()

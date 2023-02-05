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


def change_pass(username, passwd, new_passwd, confirm_passwd):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT * from accounts WHERE Username=? AND Password=?", (username, hashlib.md5(passwd.encode()).hexdigest()))
        if not cur.fetchone():
            return 1    # incorrect password
        if new_passwd != confirm_passwd:
            return 2    # password and confirm password don't match
        cur.execute("UPDATE accounts SET Password=? WHERE Username=?", (hashlib.md5(new_passwd.encode()).hexdigest(), username))
        con.commit()
        return 0    # password change successful

# current logged in account
def get_session():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT Username FROM sessions")
        result = cur.fetchone()
        return result[0] if result else None


# if admin(1) or user(0) 
def get_permission_level(username):
    with sqlite3.connect(database_file) as con:
        if username == None:
            return 0
        cur = con.cursor()
        cur.execute("SELECT Admin from accounts WHERE Username=?", (username,))
        return bool(cur.fetchone()[0])


def get_all_accounts():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT Username, Admin from accounts")
        return cur.fetchall()


def delete_user(username):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM accounts WHERE Username=?", (username,))
        con.commit()


def delete_all_users():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM accounts WHERE Admin = 0")
        con.commit()


def grant_admin_privilege(username):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("UPDATE accounts SET Admin = 1 WHERE Username = ?", (username,))
        con.commit()


def remove_admin_privilege(username):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("UPDATE accounts SET Admin = 0 WHERE Username = ?", (username,))
        con.commit()


def logout():
    if get_session():
        with sqlite3.connect(database_file) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM sessions")
            con.commit()

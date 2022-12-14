import hashlib
import sqlite3


def register(username, passwd, confirm_passwd):
    cursor.execute("DROP TABLE IF EXISTS login")
    conn.commit()
    
    cursor.execute("CREATE TABLE login(Username VARCHAR UNIQUE, Password VARCHAR)")
    conn.commit()

def enter(username, password):
    query = "INSERT INTO login (Username, Password) VALUES (?, ?)"
    cursor.execute(query, (username, password))
    conn.commit()

def check(username, password):
    query = 'SELECT * FROM login WHERE Username = ? AND Password = ?'
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.commit()
    print('[DEBUG][check] result:', result)
    return result

def login():
    answer = input("Login (Y/N): ")

    if answer.lower() == "y":
        username = input("Username: ")
        password = input("Password: ")
        if check(username, password):
            print("Username correct!")
            print("Password correct!")
            print("Logging in...")
        else:
            print("Something wrong")

# --- main ---


conn = sqlite3.connect("account.db")
cursor = conn.cursor()

register()

Username = input("Create username: ")
Password = input("Create password: ")

enter(Username, Password)

#check(Username, Password)

login()

cursor.close()
conn.close()

from datetime import datetime
import sqlite3
from utils import accounts

database_file = "invento.db"

def create_inventory_table():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS products (
            item TEXT NOT NULL,
            category TEXT NOT NULL,
            in_stock INTEGER NOT NULL,
            buying_price REAL NOT NULL,
            selling_price REAL NOT NULL,
            date_modified TEXT NOT NULL,
            modified_by TEXT NOT NULL,
            permission_level TEXT NOT NULL
        );
        ''')
        cur.execute("CREATE TABLE IF NOT EXISTS categories (category_name TEXT NOT NULL);")
        con.commit()


# Function to add product to the database
def add_product(item, category, in_stock, buying_price, selling_price):
    date_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    modified_by = str(accounts.get_session())
    permission_level = accounts.get_permission_level(modified_by)
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("""
        INSERT INTO products (item, category, in_stock, buying_price, selling_price, date_modified, modified_by, permission_level)
        VALUES (?,?,?,?,?,?,?,?)
        """, (item, category, in_stock, buying_price, selling_price, date_modified, modified_by, permission_level))
        con.commit()


def add_category(category_name):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO categories (category_name) VALUES (?)", (category_name,))
        con.commit()

def get_all_category():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM categories")
        return cur.fetchall()

def remove_category(category_name):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM categories WHERE category_name=?", (category_name,))
        con.commit()


def delete_product(product):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM products WHERE item=?", (product,))
        con.commit()

def edit_product(product):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("""
            UPDATE products SET
                name=?,
                category=?,
                in_stock=?,
                buying_price=?,
                selling_price=?,
                date_modified=?,
                modified_by=?,
                permission_level=?
            WHERE id=?
        """, (product))

# Function to view all products
def view_inventory():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT item, category, in_stock, buying_price, selling_price, date_modified FROM products")
        return cur.fetchall()

# Function to view updates of a product
def view_modified():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT item, date_modified, modified_by, permission_level FROM products")
        return cur.fetchall()

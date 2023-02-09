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
            permission_level TEXT NOT NULL);
        ''')
        cur.execute("CREATE TABLE IF NOT EXISTS categories (category_name TEXT NOT NULL);")
        con.commit()

def search_product(item_name):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM products WHERE item LIKE ? COLLATE NOCASE", ('%'+item_name+'%',))
        return cur.fetchall()

# add product to the database
def add_product(item, category, in_stock, buying_price, selling_price):
    date_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    modified_by = str(accounts.get_session())
    permission_level = accounts.get_permission_level(modified_by)
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT item FROM products WHERE item = ?", (item,))
        if cur.fetchone() is None:
            cur.execute("""
            INSERT INTO products (item, category, in_stock, buying_price, selling_price, date_modified, modified_by, permission_level)
            VALUES (?,?,?,?,?,?,?,?)
            """, (item, category, in_stock, buying_price, selling_price, date_modified, modified_by, permission_level))
            con.commit()
            return 0    # product added
        return 1    # product already exists


def add_category(category_name):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT category_name FROM categories WHERE category_name = ?", (category_name,))
        if cur.fetchone():
            return 1    # category already exists
        cur.execute("INSERT INTO categories (category_name) VALUES (?)", (category_name,))
        con.commit()
        return 0    # category created


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

def delete_all_products():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM products")
        con.commit()

def edit_product(product, category, in_stock, buying_price, selling_price, product_focus):
    date_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    modified_by = str(accounts.get_session())
    permission_level = accounts.get_permission_level(modified_by)
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("""
            UPDATE products SET
                item=?,
                category=?,
                in_stock=?,
                buying_price=?,
                selling_price=?,
                date_modified=?,
                modified_by=?,
                permission_level=?
            WHERE item=?
        """, (product, category, in_stock, buying_price, selling_price, date_modified, modified_by, permission_level, product_focus))


def count_category():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM categories")
        return cur.fetchone()[0]

def count_products():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM products")
        return cur.fetchone()[0]

# view all products
def view_inventory():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT item, category, in_stock, buying_price, selling_price, date_modified FROM products")
        return cur.fetchall()


# view updates of a product
def view_modified():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT item, date_modified, modified_by, permission_level FROM products ORDER BY date_modified DESC")
        return cur.fetchall()

def sort_table(column, ascending):
    order = "ASC" if ascending == True else "DESC"
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute(f"SELECT item, category, in_stock, buying_price, selling_price, date_modified FROM products ORDER BY {column} COLLATE NOCASE {order}")
        return cur.fetchall()

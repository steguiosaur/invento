from utils import accounts
from datetime import datetime
import sqlite3
import time

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
        cur.execute("CREATE TABLE IF NOT EXISTS sales (total_sales REAL NOT NULL, date_sale TEXT NOT NULL);")
        con.commit()


# view all products
def view_inventory():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT item, category, in_stock, buying_price, selling_price, date_modified FROM products")
        return cur.fetchall()


def get_sales_data():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT total_sales, strftime('%m-%d', date_sale) as date_sale FROM sales;")
        return cur.fetchall()


def get_today_sales():
    current_date = time.strftime('%Y-%m-%d')
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT total_sales FROM sales WHERE date_sale=?", (current_date,))
        result = cur.fetchone()
        if result:
            return result[0]
        return 0


def update_stock(item_name, new_stock):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("UPDATE products SET in_stock = ? WHERE item = ?", (new_stock, item_name))
        con.commit()


def get_selling_price(item_name):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT selling_price FROM products WHERE item=?", (item_name,))
        return cur.fetchone()[0]
    

def add_sales(earned):
    current_date = time.strftime('%Y-%m-%d')
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT total_sales FROM sales WHERE date_sale=?", (current_date,))
        result = cur.fetchone()
        if result:
            updated_sales = result[0] + earned
            cur.execute("UPDATE sales SET total_sales=? WHERE date_sale=?", (updated_sales, current_date))
        else:
            cur.execute("INSERT INTO sales (total_sales, date_sale) VALUES (?,?)", (earned, current_date))
        con.commit()


def reduce_sales(remove_earned):
    current_date = time.strftime('%Y-%m-%d')
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT total_sales FROM sales WHERE date_sale=?", (current_date,))
        result = cur.fetchone()
        if result:
            updated_sales = result[0] - remove_earned
            cur.execute("UPDATE sales SET total_sales=? WHERE date_sale=?", (updated_sales, current_date))
        else:
            return 1 # no sales to reduce 
        con.commit()


def get_current_date_sales():
    current_date = time.strftime('%Y-%m-%d')
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT total_sales FROM sales WHERE date_sale=?", (current_date,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            return 0


def get_current_in_stock(item_name):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT in_stock FROM products WHERE item=?", (item_name,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            return 0


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

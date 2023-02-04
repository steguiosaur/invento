from datetime import datetime
import sqlite3

database_file = "invento.db"

def create_inventory_table():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        con.commit()


# Function to add product to the database
def add_product(item, category, in_stock, buying_price, selling_price, modified_by, permission_level):
    date_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("""
        INSERT INTO products (name, category, in_stock, buying_price, selling_price, date_modified, modified_by, permission_level)
        VALUES (?,?,?,?,?,?,?,?)
        """, (item, category, in_stock, buying_price, selling_price, date_modified, modified_by, permission_level))
        con.commit()

def delete_product(product_id):
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM products WHERE id=?", (product_id,))

def edit_product(product_id, product):
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
        """, (*product, product_id))

# Function to view all products
def view_inventory():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT name, category, in_stock, buying_price, selling_price, date_modified FROM products")
        return cur.fetchall()

# Function to view updates of a product
def view_modified():
    with sqlite3.connect(database_file) as con:
        cur = con.cursor()
        cur.execute("SELECT item, modified_by, permission_level FROM products")
        return cur.fetchall()

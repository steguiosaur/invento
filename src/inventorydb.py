import sqlite3

#productName, requiredStock, currentStock, marketPrice, sellingPrice

# Create database on first login
def Database():
    global conn, cursor
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Product_Name TEXT, Required_Stock TEXT, Current_Stock TEXT, Market_Price TEXT, Selling_Price TEXT)")


def AddNew(productName, requiredStock, currentStock, marketPrice, sellingPrice):
    Database()
    cursor.execute("INSERT INTO `product` (Product_Name, Required_Stock, Current_Stock, Market_Price, Selling_Price) VALUES(?, ?, ?, ?, ?)", (str(productName.get()),int(requiredStock.get()), int(currentStock.get()), int(marketPrice.get()), int(sellingPrice.get())))
    conn.commit()
    cursor.close()
    conn.close()


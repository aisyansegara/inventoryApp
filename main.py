import mysql.connector
import os
from datetime import datetime, timedelta

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "db_inventory"
)

def insert_items(db):
    print("=== INSERT ITEMS ===")
    today_date = datetime.now().strftime('%d-%m-%Y')
    print(f"Date: {today_date}")
    name = input("Item name: ")
    merk = input("Merk name: ")
    desc = input("Add description: ")
    quantity = input("Add quantity: ")

    cursor = db.cursor()
    val = ('', name, merk, desc, quantity, datetime.now())
    query = "INSERT INTO tb_items (item_id, name, merk, description, quantity, date_of_entry) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, val)
    db.commit() 
    print("{} item added successfully!". format(cursor.rowcount))

def show_items(db):
    cursor = db.cursor()
    query = "SELECT * FROM tb_items"
    cursor.execute(query)
    items = cursor.fetchall()

    if cursor.rowcount <= 0:
        print("=== SHOW ITEMS ===")
        print("No items\n")
        show_menu(db)
    else:
        print("=== SHOW ITEMS ===")
        for item in items:
            print(f"Item ID: {item[0]}")
            print(f"Name: {item[1]}")
            print(f"Merk: {item[2]}")
            print(f"Description: {item[3]}")
            print(f"Quantity: {item[4]}")
            print(f"Date of Entry: {item[5].strftime("%d-%m-%Y %H:%M:%S")}\n")

def update_item(db):
    cursor = db.cursor()
    show_items(db)
    print("=== UPDATE ITEM ===")
    item_id = int(input("Select item ID: "))
    name = input("Change item name: ")
    merk = input("Change item merk: ")
    desc = input("Change item description: ")
    quantity = int(input("Change item quantity: "))

    val = (name, merk, desc, quantity, item_id)
    query = "UPDATE tb_items SET name = %s, merk = %s, description = %s, quantity = %s WHERE item_id = %s"
    cursor.execute(query, val)
    db.commit()
    print("{} item data changed successfully!".format(cursor.rowcount))
    
def delete_item(db):
    cursor = db.cursor()
    show_items(db)
    print("=== DELETE ITEM ===")
    item_id = int(input("Select item ID: "))
    val = (item_id,)
    query = "DELETE FROM tb_items WHERE item_id = %s"
    cursor.execute(query, val)
    db.commit()
    print("{} item deleted successfully!".format(cursor.rowcount))

def search_item(db):
    cursor = db.cursor()
    print("=== SEARCH ITEM ===")
    keyword = input("Enter keywords: ")
    val = (keyword,)
    query = "SELECT * FROM tb_items WHERE name LIKE %s"
    cursor.execute(query, val)
    items = cursor.fetchall()

    if cursor.rowcount <= 0:
        print("The item name was not found, please check the item name again!")
        exit()
    else:
        for item in items:
            print(f"\nItem ID: {item[0]}")
            print(f"Name: {item[1]}")
            print(f"Merk: {item[2]}")
            print(f"Description: {item[3]}")
            print(f"Quantity: {item[4]}")
            print(f"Date of Entry: {item[5].strftime("%d-%m-%Y %H:%M:%S")}\n")

def pickup_item(db):
    cursor = db.cursor()
    show_items(db)
    print("=== PICKUP ITEM ===")
    today_date = datetime.now()
    item_id = int(input("Select item ID: "))
    days = int(input("How many days: "))

    val = (item_id,)
    query = "SELECT * FROM tb_items WHERE item_id = %s"
    cursor.execute(query, val)
    items = cursor.fetchall()

    for item in items:
        name = item[1]
        merk = item[2]
        quantity = item[4]
        date_of_entry = item[5]
    date_of_return = today_date + timedelta(days=days)
    if days > 1:
        cost = 10000 * days
    else:
        cost = 20000 * days

    val2 = ('', name, merk, quantity, date_of_entry, date_of_return, cost)
    query2 = "INSERT INTO tb_transactions (transaction_id, name, merk, quantity, date_of_entry, date_of_return, cost) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query2, val2)
    query3 = "DELETE FROM tb_items WHERE item_id = %s"
    cursor.execute(query3, val)
    db.commit()
    print("{} item transaction added successfully!". format(cursor.rowcount))

def transactions_history(db):
    cursor = db.cursor()
    print("=== TRANSACTION HISTORY ===")
    query = "SELECT * FROM tb_transactions"
    cursor.execute(query)
    transactions = cursor.fetchall()

    if cursor.rowcount <= 0:
        print("No item transactions")
        show_menu(db)
    else:
        for transaction in transactions:
            print(f"Transaction ID: {transaction[0]}")
            print(f"Name: {transaction[1]}")
            print(f"Merk: {transaction[2]}")
            print(f"Quantity: {transaction[3]}")
            print(f"Date of Entry: {transaction[4].strftime("%d-%m-%Y %H:%M:%S")}")
            print(f"Date of Return: {transaction[5].strftime("%d-%m-%Y %H:%M:%S")}")
            print(f"Cost: Rp{transaction[6]:,}\n")

def show_menu(db):
    print("=== INVENTORY APP ===")
    print("1. Insert item")
    print("2. Show items")
    print("3. Update item")
    print("4. Delete item")
    print("5. Search item")
    print("6. Pickup item")
    print("7. Transaction history")
    print("0. Exit")
    print("------------------")
    menu = input("Select menu>> ")

    os.system("cls")

    if menu == "1":
        insert_items(db)
    elif menu == "2":
        show_items(db)
    elif menu == "3":
        update_item(db)
    elif menu == "4":
        delete_item(db)
    elif menu == "5":
        search_item(db)
    elif menu == "6":
        pickup_item(db)
    elif menu == "7":
        transactions_history(db)
    elif menu == "0":
        exit()
    else:
        print("Wrong menu!\n")

if __name__ == "__main__":
    while(True):
        show_menu(db)
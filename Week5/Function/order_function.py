import product_function as pf
import courier_function as cf
import mysql.connector

mydb = mysql.connector.connect(

    user = 'root',
    password = 'pass',
    port = 3306,
    database = "MINIDB"
    )

cursor = mydb.cursor()

# cursor.execute ('CREATE TABLE Orders(OrdersID int AUTO_INCREMENT PRIMARY KEY, customer_name VARCHAR(50),Customer_address VARCHAR(250),Customer_phone VARCHAR(50),Courier int(10),Status INT(10), Items VARCHAR(255))')
# cursor.execute ('CREATE TABLE OrderStatus(OrderStatusID int AUTO_INCREMENT PRIMARY KEY, Order_Status VARCHAR(100))')
# cursor.execute("INSERT INTO OrderStatus(Order_Status) Values ('Delivered')")
mydb.commit()
items = []

def read_orders():
    cursor.execute('SELECT * FROM Orders')
    for x in cursor:
        print(x)

def order_items_loop():
    exit = int(input("0,To Exit , 1 To Add New Product"))
    while exit != 0:
        pf.read_product()
        item_basket =(input("Use ID to add products: "))
        items.append(item_basket)
        exit = int(input("0,To Exit , 1 To Continue"))
    return ",".join(items)

def order_status():
    cursor.execute("select * from OrderStatus")
    for x in cursor:
        print(x)


def create_order():
    customer_name = input("What is your name?: ")
    customer_address = input("what is your address?: ")
    customer_number = input("what is your number?:")
    cf.read_courier()
    couriername = int(input("Put in courier ID: "))
    order_status()
    status = int(input("Use the status ID: "))
    items = order_items_loop()
    cursor.execute(f"INSERT INTO Orders(customer_name,Customer_address,Customer_phone,Courier,Status,Items)  VALUES ('{customer_name}','{customer_address}','{customer_number}',{couriername},{status},'{items}') ")
    mydb.commit()

    
def change_order_status():
    read_orders()
    change_status = int(input(" Select the index of Status:  "))
    cursor.execute('SELECT * FROM OrderStatus')
    for x in cursor:
        print(x)
    update_status = int(input("what would you like to change Order Status too?"))
    cursor.execute(f"UPDATE INTO Orders SET Status = '{update_status}' WHERE  OrdersID = {change_status} ")
    mydb.commit()
    


def change_order():
    read_orders()
    change_id = int(input(' Select Order ID you would to update '))
    customer_name = input("What is your name?: ")
    customer_address = input("what is your address?: ")
    customer_number = input("what is your number?:")
    cf.read_courier()
    couriername = int(input("Put in courier ID: "))
    order_status()
    status = int(input("Use the status ID: "))
    items = order_items_loop()
    cursor.execute(f"Update Orders set customer_name = '{customer_name}', customer_address = '{customer_address}', customer_phone = '{customer_number}', Courier = {couriername}, status = {status}, Items = '{items}' WHERE OrdersID = {change_id}")
    mydb.commit()



def delete_order():
    read_orders()
    delete_id = int(input('Select the OrdersID you would like to delete: '))
    cursor.execute(f'DELETE FROM Orders WHERE OrdersID = {delete_id}')
    mydb.commit()








from datetime import datetime
import mysql.connector
import csv

mydb = mysql.connector.connect(

    user = 'root',
    password = 'pass',
    port = 3306,
    database = "MINIDB"
    )

cursor = mydb.cursor()

# for x in cursor:
#     print(x)
# cursor.execute("CREATE TABLE IF NOT EXIST Product(ProductID int AUTO_INCREMENT PRIMARY KEY,name VARCHAR(250),price VARCHAR(250))")
# dummy_data = [('chips',"1.25"),('pepsi','2.50'),('Coke','4.00')]
# cursor.execute("INSERT INTO Product(name,price) Values ('Chicken','6.00')")
# mydb.commit()

# with open('productss.csv','r') as file:
#    productss_reader = csv.reader(file)
#    for count, row in enumerate(productss_reader):
#         if count == 0:
#             continue
#         cursor.execute(f"INSERT INTO Product(name,price) VALUES ('{str(row[0])}', {str(row[1])})")
# mydb.commit()


def read_product():
    cursor.execute('SELECT * FROM Product')
    for x in cursor:
        print(x)
    #     line += x
    # return line
    

def create_product():
    read_product()
    new_product = input("add new Product: ")
    new_price = input("add New Price: ")
    cursor.execute(f"INSERT INTO Products(name,price)  VALUES ('{new_product}','{new_price}') ")
    mydb.commit()
    
def update_product():
    read_product()
    update_product = int(input('Select ProductID'))
    new_product = input('insert new product: ')
    new_price = input('Set Price:')
    cursor.execute(f"update Products set name = '{new_product}', price = '{new_price}' WHERE Productid = {update_product}")
    mydb.commit()


def delete_product():
    read_product()
    delete_id = int(input("select productid to delete: "))
    cursor.execute(f'DELETE FROM Products WHERE Productid = {delete_id}')
    mydb.commit()


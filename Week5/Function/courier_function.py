import mysql.connector
import csv

mydb = mysql.connector.connect(

    user = 'root',
    password = 'pass',
    port = 3306,
    database = "MINIDB"
    )

cursor = mydb.cursor()

# cursor.execute("CREATE TABLE Courier(CourierID int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250),number bigint)")
# cursor.execute("INSERT INTO Courier(name,number) Values ('sheikh',12374)")
# cursor.execute(num1,person)
# with open('courier.csv','r') as file:
#     Courier_reader = csv.reader(file)
#     for count, row in enumerate(Courier_reader):
#         if count == 0:
#             continue
#         cursor.execute(f"INSERT INTO Courier (name,number) VALUES ('{str(row[0])}', {int(row[1])})")

# mydb.commit()

def read_courier():
    cursor.execute('SELECT * FROM Courier')
    for x in cursor:
        print(x)


def create_courier():
    read_courier()
    new_courier = input("add new courier: ")
    new_number = int(input(" Enter New Number: "))
    cursor.execute(f"INSERT INTO Courier(name,number)  VALUES ('{new_courier}',{new_number}) ")
    mydb.commit()

def update_courier():
    read_courier()
    idx_courier = int(input("courier index that needs to be changed: "))
    updated_courier = input("Put in updated courier: ")
    update_number = int(input("Put in updated number: "))
    cursor.execute(f"UPDATE Courier set name = '{updated_courier}', number = '{update_number}' WHERE CourierID = {idx_courier}")
    mydb.commit()



def delete_courier():
    read_courier()
    delete_id = int(input("select CourierID to delete: "))
    cursor.execute(f'DELETE FROM Courier WHERE Courierid = {delete_id}')
    mydb.commit()


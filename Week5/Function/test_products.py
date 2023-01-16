
import courier_function as cf
import unittest
import order_function as of
import product_function as pf
from unittest.mock import patch
import mysql.connector
import pytest
 
@pytest.fixture
def set_up_database():
    mydb = mysql.connector.connect(

    user = 'root',
    password = 'pass',
    port = 3306,
    database = "MINIDB"
    )
    cursor = mydb.cursor()
    
    # cursor.execute("CREATE TABLE  Product(ProductID int AUTO_INCREMENT PRIMARY KEY,name VARCHAR(250),price VARCHAR(250))")
    # dummy_data = [('chips',"1.25"),('pepsi','2.50'),('Coke','4.00')]
    # cursor.execute("INSERT INTO Product(name,price) Values ('?','?')",dummy_data)

def test_fixture_setup(set_up_database):
    cursor = set_up_database
    assert list(cursor.execute('SELECT * FROM Products')) == 3 
    


# def test_view_product(set_up_database):

#     #assemble
#     a_list = ['a','b','c']
#     #Act
#     actual_list = pf.read_product()
#     #assert


# @patch("builtins.input",side_effect =['sheikh','999'])
# def test_add_courier(mock_input):
#     cf.create_courier()
#     assert cf.Courier_list[-1] == {'name': 'sheikh', 'number': '999'}


# @patch("builtins.input",side_effect =['bob','bobs house','09809',2,'preparing','1','1','1'])
# def test_add_orders(mock_input):
#     of.create_order()
#     assert of.orders_list[-1] == {'customer_name: ': 'bob', 'customer_address: ': 'bobs house', 'customer_phone': '09809', 'courier': 2, 'status': 'preparing', 'items': [1]}

# @patch('builtins.print')
# def test_print_order(mock_print):
#     of.print_order()
#     mock_print.assert_called_with({'customer_name: ': 'bob', 'customer_address: ': 'bobs house', 'customer_phone': '09809', 'courier': 2, 'status': 'preparing', 'items': [1]})

# def test_courier_list():
#     cf.Courier_list
#     assert len(cf.Courier_list) == 10

# def test_courier_list():
#     cf.load_courier()
#     cf.Courier_list
#     assert len(cf.Courier_list) == 10
    

    
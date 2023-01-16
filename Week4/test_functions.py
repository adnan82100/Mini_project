
import courier_function as cf
import unittest
import order_function as of
import product_function as pf
from unittest.mock import patch 
 

cf.load_courier
of.load_orders
pf.load_products

 
# @patch("builtins.print")
# def test_prints_hello_world(mock_print): 
#     hello_world() # Act 
#     mock_print.assert_called_with("Hello World!")

@patch("builtins.input",side_effect =['Pepsi','1.00'])
def test_add_product(mock_input):
    pf.create_product()
    assert pf.product_list[-1] == {'name': 'Pepsi', 'price': '1.00'}

@patch("builtins.input",side_effect =['sheikh','999'])
def test_add_courier(mock_input):
    cf.create_courier()
    assert cf.Courier_list[-1] == {'name': 'sheikh', 'number': '999'}


@patch("builtins.input",side_effect =['bob','bobs house','09809',2,'preparing','1','1','1'])
def test_add_orders(mock_input):
    of.create_order()
    assert of.orders_list[-1] == {'customer_name: ': 'bob', 'customer_address: ': 'bobs house', 'customer_phone': '09809', 'courier': 2, 'status': 'preparing', 'items': [1]}

@patch('builtins.print')
def test_print_order(mock_print):
    of.print_order()
    mock_print.assert_called_with({'customer_name: ': 'bob', 'customer_address: ': 'bobs house', 'customer_phone': '09809', 'courier': 2, 'status': 'preparing', 'items': [1]})

# def test_courier_list():
#     cf.Courier_list
#     assert len(cf.Courier_list) == 10

# def test_courier_list():
#     cf.load_courier()
#     cf.Courier_list
#     assert len(cf.Courier_list) == 10
    

    
shopping_basket = {}
order_status = 'preparing'
orders_list = []

order_menu = int(input(""" 0 To Return to Main Menu
  1 To print Order 
  2 Customer information
  3 to update existing order status
  4 to update order
  5 to delete order
  """))
while order_menu != 0:
    if order_menu == 1:
        print(orders_list)
    elif order_menu == 2:
       customer_name = input("What is your name?: ")
       customer_address = input('what is your address?: ')
       customer_number = input('what is your number?:')
       shopping_basket['Customer Name: '] = customer_name
       shopping_basket['Customer Address: '] = customer_address
       shopping_basket['Customer Number'] = customer_number
       shopping_basket['order_status'] = order_status
       print(shopping_basket)
       orders_list.append(shopping_basket)
    elif order_menu == 3:
        update_status = input('what would you like to change Order Status too?')
        shopping_basket['order_status'] = update_status
        print(shopping_basket)
    elif order_menu == 4:
        for i in enumerate(orders_list):
            print(i)
        Change_o = int(input("which order would you like to change"))
        print(orders_list[Change_o])
        new_name = input("What is your name?: ")
        new_address = input('what is your address?: ')
        new_number = input('what is your number?:')
        new_status = input('what is the status')
        Dictionary2 = {'Customer Name:': new_name,'Customer Address:': new_address,'Customer Number:': new_number,'Order Status': new_status,}
        orders_list[Change_o] = Dictionary2
        print(orders_list)
        
    elif order_menu == 5:
        shopping_basket.clear()
        print(shopping_basket)
    order_menu = int(input(""" 0 To Return to Main Menu
    1 To print Order 
    2 Customer information
    3 to update existing order status
    4 to update order
    5 to delete order
    """))
    
# ELSE IF user input is 2: 
#     IF user input is 0: 
#         RETURN to main menu 
 
#     ELSE IF user input is 1: 
#         PRINT orders dictionary 
 
#     ELSE IF user input is 2: 
#         GET user input for customer name 
#         GET user input for customer address 
#         GET user input for customer phone number 
 
#         SET order status to be 'PREPARING' 
#         APPEND order to orders list 
 
#     ELSE IF user input is 3: 
#         # UPDATE existing order status 
 
#         PRINT orders list with its index values 
#         GET user input for order index value 
 
#         PRINT order status list with index values 
#         GET user input for order status index value 
#         UPDATE status for order 
 
#     ELSE IF user input is 4: 
#         # STRETCH - UPDATE existing order 
 
#         PRINT orders list with its index values 
# mini_project_week_2.md 10/26/2022
# 3 / 3
#         GET user input for order index value 
 
#         FOR EACH key-value pair in selected order: 
#             GET user input for updated property 
#             IF user input is blank: 
#                 do not update this property 
#             ELSE: 
#                 update the property value with user input 
 
#     ELSE IF user input is 5: 
#         # STRETCH GOAL - DELETE order 
                     
#         PRINT orders list 
#         GET user input for order index value 
#         DELETE order at index in order list

        # products = input(" what would you like to add to your basket: ")
        # if products not in  drink_list and products  not in product_list:
        #     print("Error not in menu")
        # else:    
        #     shopping_basket["Basket "] = [products]
        #     print(shopping_basket)
product_list = []
Courier_list = []
shopping_basket = {}
order_status = 'preparing'
orders_list = []

def products_order():
    with open('products123.txt', 'r') as f:
        for line in f.readlines():
            product_list.append(line.strip("\n"))
            print()


def create_product():
    new_product = input("add new product: ")
    product_list.append(new_product)
    print(product_list)

def update_product():
     for i in enumerate(product_list):
            print(i)
            idx_product = int(input("Product index that needs to be changed: "))
            upd_product = input("Put in updated product")
            product_list[idx_product] = upd_product
            print(product_list)
def delete_product():
    for i in enumerate(product_list):
        print(i)
    index_p = int(input( " choose index that needs to be deleted: "))
    del product_list[index_p]
    print(product_list)



def courier_order():
    with open('people.txt', 'r') as f:
        for line in f.readlines():
            Courier_list.append(line.strip("\n"))
        


def create_courier():
    new_product = input("add new courier: ")
    Courier_list.append(new_product)
    print(Courier_list)

def update_courier():
     for i in enumerate(Courier_list):
            print(i)
            idx_product = int(input("courier index that needs to be changed: "))
            upd_product = input("Put in updated courier")
            Courier_list[idx_product] = upd_product
            print(Courier_list)
def delete_courier():
    for i in enumerate(Courier_list):
        print(i)
    index_p = int(input( " choose index that needs to be deleted: "))
    del Courier_list[index_p]
    print(Courier_list)
    
def close_save_product():
    with open('products123.txt','w') as f:
        for x in product_list:
            f.write(f'{x}\n') 

def close_save_courier():
    with open('people.txt','w') as f:
        for x in Courier_list:
            f.write(f'{x}\n') 

def create_order():
    customer_name = input("What is your name?: ")
    customer_address = input('what is your address?: ')
    customer_number = input('what is your number?:')
    shopping_basket['Customer Name: '] = customer_name
    shopping_basket['Customer Address: '] = customer_address
    shopping_basket['Customer Number'] = customer_number
    shopping_basket['order_status'] = order_status
    print(shopping_basket)
    orders_list.append(shopping_basket)
def view_order():
    print(orders_list)
def change_order_status():
    update_status = input('what would you like to change Order Status too?')
    shopping_basket['order_status'] = update_status
    print(shopping_basket)
def change_order():
    for i in enumerate(orders_list):
        print(i)
        Change_o = int(input("which order would you like to change"))
        print(orders_list[Change_o])
        new_name = input("What is your name?: ")
        new_address = input('what is your address?: ')
        new_status = input('what is the status')
        new_number = input("what is the number")
        Dictionary2 = {'Customer Name:': new_name,'Customer Address:': new_address,'Customer Number:': new_number,'Order Status': new_status,}
        orders_list[Change_o] = Dictionary2
        print(orders_list)
def delete_order():
    shopping_basket.clear()
    print(shopping_basket)
    
    



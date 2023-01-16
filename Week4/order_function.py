import csv
import product_function as pf
import courier_function as cf
shopping_basket = {}
orders = []
orders_list = []
items = []

def load_orders():
    with open("order.csv", "r") as orderfile:
        order_reader = csv.DictReader(orderfile)
        for order in order_reader:
            orders_list.append(order)
def order_items_loop():
    exit = int(input("0,To Exit , 1 To Continue"))
    while exit != 0:
        for product in enumerate(pf.product_list):
            print(product)
        item_basket = int(input("Use index to add products,"))
        items.append(item_basket)
        exit = int(input("0,To Exit , 1 To Continue"))
        return items


def create_order():
    customer_name = input("What is your name?: ")
    customer_address = input("what is your address?: ")
    customer_number = input("what is your number?:")
    for people in enumerate(cf.Courier_list):
        print(people)
    couriername = input("Put in courier index: ")
    status = input("whats the status: ")
    items = order_items_loop()
    shopping_basket["customer_name: "] = customer_name
    shopping_basket["customer_address: "] = customer_address
    shopping_basket["customer_phone"] = customer_number
    shopping_basket["courier"] = couriername
    shopping_basket["status"] = status
    shopping_basket["items"] = items
    print(shopping_basket)
    orders_list.append(shopping_basket)

    # shopping_basket["customer_name: "] = customer_name --> CRASH
    # shopping_basket.get("customer_name: ") = customer_name --> ERROR


def print_order():
    for order in orders_list:
        print(order)


def change_order_status():
    for order in enumerate(orders_list):
        print(order)
    change_status = int(
        input(" Choose the index of the order you would like to change")
    )
    update_status = input("what would you like to change Order Status too?")
    orders_list[change_status]["status"] = update_status
    print(orders_list)


def change_order():
    for i in enumerate(orders_list):
        print(i)
    Change_o = int(input("which order would you like to change"))
    print(orders_list[Change_o])
    new_name = input("What is the name?: ")
    new_address = input("what is the address?: ")
    new_status = input("what is the status")
    new_number = input("what is the number")
    for people in enumerate(cf.Courier_list):
        print(people)
    new_courier = input("index of new courier")
    items = order_items_loop()
    Dictionary2 = {
        "Customer Name:": new_name,
        "Customer Address:": new_address,
        "Customer Number:": new_number,
        "courier": new_courier,
        "Status": new_status,
        "items": items,
    }
    orders_list[Change_o] = Dictionary2
    print(orders_list)


def delete_order():
    for order in enumerate(orders_list):
        print(order)
    deleted_order = int(input("Pick the index of the order you want to delete"))
    del orders_list[deleted_order]
    print(orders_list)


def save_orders():
    with open("order.csv", "w") as file:
        fields = [
            "customer_name",
            "customer_address",
            "customer_phone",
            "courier",
            "status",
            "items",
        ]
        headers = csv.DictWriter(file, fieldnames=fields)
        headers.writeheader()
        headers.writerows(orders_list)

# 1. Refactor functions into separate modules/files
# 2. Look at the code and think how you can refactor some functions
# 3. To exception handling in core parts of code --> Test case: trying to update a list that is empty
# 3. Can you test some of those functions?


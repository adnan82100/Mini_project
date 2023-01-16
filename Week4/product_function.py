import csv
product_list = []
product = {}

def load_products():
    with open("productss.csv", "r") as file:
        product_reader = csv.DictReader(file)
        for line in product_reader:
            product_list.append(line)

def create_product():
    new_product = input("add new product: ")
    new_price = input("add New Price: ")
    product["name"] = new_product
    product["price"] = new_price
    product_list.append(product)
    print(product_list)


def update_product():
    for i in enumerate(product_list):
        print(i)
    idx_product = int(input("Product index that needs to be changed: "))
    upd_product = input("Put in updated product")
    upd_price = input(" Put in price")
    product_list[idx_product]["name"] = upd_product
    product_list[idx_product]["price"] = upd_price
    print(product_list)


def delete_product():
    for i in enumerate(product_list):
        print(i)
    index_p = int(input(" choose index that needs to be deleted: "))
    del product_list[index_p]
    print(product_list)


def save_products():
    with open("productss.csv", "w") as file:
        fields = ["name", "price"]
        headers = csv.DictWriter(file, fieldnames=fields)
        headers.writeheader()
        headers.writerows(product_list)

import csv
Courier_list = []
courier = {}

def load_courier():
    with open("courier.csv", "r") as file:
        courier_reader = csv.DictReader(file)
        for courier in courier_reader:
            # print(courier)
            Courier_list.append(courier)

def create_courier():
    new_courier = input("add new courier: ")
    new_number = input(" Enter New Number")
    courier["name"] = new_courier
    courier["number"] = new_number
    Courier_list.append(courier)
    print(Courier_list)


def update_courier():
    for i in enumerate(Courier_list):
        print(i)
    idx_courier = int(input("courier index that needs to be changed: "))
    update_courier = input("Put in updated courier")
    update_number = input("Put in updated number")
    Courier_list[idx_courier]["name"] = update_courier
    Courier_list[idx_courier]["number"] = update_number
    print(Courier_list)


def delete_courier():
    for i in enumerate(Courier_list):
        print(i)
    index_p = int(input(" choose index that needs to be deleted: "))
    del Courier_list[index_p]
    print(Courier_list)


def save_courier():
    with open("courier.csv", "w") as file:
        fields = ["name", "number"]
        headers = csv.DictWriter(file, fieldnames=fields)
        headers.writeheader()
        headers.writerows(Courier_list)

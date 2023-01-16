# with open('products.txt', 'r') as f:
    # for line in f:
    #     print(line, end = "")
    
    # f_contents = f.read()
    # print(f_contents)
# with open('products.txt', 'a') as f:
def view():
    with open('products.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())

def change():
    with open('products.txt', 'r' ) as f:
        lines = f.readlines()
        new_list = []
        for line in lines:
            new_list.append(line.strip())
        print(new_list)

    with open('products.txt') as f:
        new_lines = f.readlines()
        product_index = int(input('Product index that you would like to change: '))
        new_product = input('what would you like to change it to: ')
        new_lines[product_index - 1] = new_product
        print(new_lines)
# make a new variable with all the lines and print it using w 


def add():
    with open('products.txt', 'r+') as f:
        lines = f.readlines()
        print(lines)
        products = input("add product: ")
        f.write(products + "\n")

def delete():
    with open('products.txt', 'r+') as f:
        pass
change()

# .strip("\n")

# f = open('products.txt', 'r')

# print(f.name)

# f.close()
# files = open("products.txt", 'r')
# contents = files.readlines()
# print(line)
# people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"] 
# try:
#     files = open('people.txt', 'w')
#     for x in people:
#         files.write(x + '\n')
# except FileNotFoundError as fnfe:
#     print('Unable to open file: ' + str(fnfe))
# finally:
#     files.close()

# word counter in a file !!!!
# with open('people.txt', 'r') as f:
#     counts = dict()
#     for x in f:
#         words = x.split()
#         for word in words:
#             if word in counts:
#                 counts[word] += 1
#             else:
#                 counts[word] = 1

# print(counts)
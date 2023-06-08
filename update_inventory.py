"""
display product
ask which product do you want to add
how many product do you want to add
confirm
update product json file
"""
import os
import file_handler

base_file = os.path.dirname(__file__)
file_path = os.path.join(base_file, 'data', 'product.json')


class Inventory:
    def __init__(self):
        self.product = file_handler.parse_file(file_path)
        self.select_product = None
        self.quantity_number = None
        self.confirm = None

    def main(self):
        select_operation = input("What do you want to do? \n"
                                 "For Updating current product type 1 \n"
                                 "For Add new Product type 2 ")
        if select_operation == 1:
            self.display_product()
            self.select_product_index()
            self.confirm_update()
        elif select_operation == "2":
            self.add_product()
            self.display_product()
        else:
            print("Choose Given Number")

    def display_product(self):
        print("Product Details : ")
        print(f'{"Index": <5} {"Name": <20} {"in-stock": <10} {"price":0>2}')
        for key, values in self.product.items():
            print(f'{key: <5} {values.get("name"): <20} {values.get("in-stock"): <10} {values.get("price"):0>2}')

    def add_product(self):
        product_name = input("Enter Product name : ")
        product_stock = input("Enter Product Quantity : ")
        product_price = input("Enter Product Price : ")
        number = str(len(self.product)+1)
        self.product[number] = {"name" : product_name, "in-stock" : product_stock, "price" : product_price}
        file_handler.write_file(file_path, self.product)

    def select_product_index(self):
        self.select_product = self.check_int(input("Please Enter the Index Number : "))
        if not(0 < self.select_product <= len(self.product)):
            raise ValueError(f'Please Select Index from 1 to {len(self.product)}')
        self.select_product = str(self.select_product)

    def check_int(self, _input):
        try:
            return int(_input)
        except ValueError:
            raise ValueError(f'Please Enter Integer Number')

    def confirm_update(self):
        self.quantity_number = int(input("How many Product do you want to add? "))
        self.confirm = input("Do you want to add to cart?")
        if self.confirm.lower() in ['yes', 'y']:
            self.product[self.select_product]["in-stock"] += self.quantity_number
            file_handler.write_file(file_path, self.product)
            self.display_product()


if __name__ == '__main__':
    i = Inventory()
    i.main()
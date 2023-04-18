import Product
class ShoppingCart():
    def __init__(self):
        self.product = Product.product
        self.cart = {}
        self.select_product = None
        self.quantity_number = 1

    def main(self):
        self.display_product()
        self.select_product_index()
        self.get_number_of_item()
        self.conform_order()
        self.display_product()
        self.display_cart()

    def display_product(self):
        print("Product Details : ")
        print(f'{"Index": <5} {"Name": <20} {"in-stock": <10} {"price":0>2}')
        for key, values in self.product.items():
            print(f'{key: <5} {values.get("name"): <20} {values.get("in-stock"): <10} {values.get("price"):0>2}')

    def select_product_index(self):
        self.select_product = self.check_int(input("Please Enter the Index Number : "))
        if not(0 < self.select_product <= len(self.product)):
             raise ValueError(f'Please Select Index from 1 to {len(self.product)}')

    def get_number_of_item(self):
        while True:
            self.quantity_number = self.check_int(input("Enter the Number of Quantity : "))
            if self.quantity_number > self.product.get(self.select_product).get("in-stock"):
                print(f'Only {self.product.get(self.select_product).get("in-stock")} Items are available')
            else:
                break

    def check_int(self, _input):
        try:
            return int(_input)
        except ValueError:
            raise ValueError(f'Please Enter Integer Number')

    def conform_order(self):
        self.confirm = input("Do you want to add to cart?")
        if self.confirm.lower() in ['yes', 'y']:
            self.cart[self.select_product] = {'quantity': self.quantity_number,
                                              'total_price': self.quantity_number * self.product.get(self.select_product).get("price")}
            self.product[self.select_product]["in-stock"] -= self.quantity_number

    def display_cart(self):
        print("Conform Cart ")
        print(f'{"Index": <5} {"Name": <20} {"quantity": <10} {"Total Price":0>2}')
        for key, values in self.cart.items():
            print(f'{self.select_product: <5} {self.product[self.select_product]["name"]: <20} {values.get("quantity"): <10} {values.get("total_price"):0>2}')


if __name__ == '__main__':
    sc = ShoppingCart()
    sc.main()
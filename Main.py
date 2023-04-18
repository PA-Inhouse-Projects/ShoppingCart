import Product
class ShoppingCart():
    def __init__(self):
        self.product = Product.product

    def main(self):
        self.display_product()

    def display_product(self):
        print("Please Select Product : ")
        print(f'{"Name": <20} {"in-stock": <10} {"price":0>2}')
        for key, values in self.product.items():
            print(f'{key: <20} {values.get("in-stock"): <10} {values.get("price"):0>2}')


cart = ShoppingCart()
cart.main()

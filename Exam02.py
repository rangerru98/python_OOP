class Cashier:
    def __init__(self, products):
        self.products = products

    def recommend(self):
        product_name = ''

        for value in  self.products:
            product_name += " " + value

        print("We have{}".format(product_name))

cashier = Cashier(['apple', 'bana', 'orange',])
cashier.recommend()
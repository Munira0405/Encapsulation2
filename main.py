class Basket:
    def __init__(self):
        self.data = []

    def add(self, product):

        self.data.append(product)
        print(f"{product['name']} mahsuloti basketga qo'shildi.")

    def remove(self, product_name):

        for product in self.data:
            if product['name'] == product_name:
                self.data.remove(product)
                print(f"{product_name} mahsuloti basketdan olib tashlandi.")
                return
        print(f"{product_name} mahsuloti basketda mavjud emas.")

    def show(self):

        if not self.data:
            print("Basket bo'sh.")
        else:
            print("Basketdagi mahsulotlar:")
            for product in self.data:
                print(f"{product['name']} - {product['price']} so'm")

    def calc(self):

        total = sum(product['price'] for product in self.data)
        print(f"Basketdagi jami narx: {total} so'm")

product1 = {'name': 'Telefon', 'price': 1500000}
product2 = {'name': 'Televizor', 'price': 3000000}
product3 = {'name': 'Kompyuter', 'price': 4500000}


basket = Basket()
basket.add(product1)
basket.add(product2)
basket.add(product3)
basket.show()
basket.calc()
basket.remove('Telefon')
basket.show()
basket.calc()


import os

class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        if not os.path.isfile(self.__file_name):
            return ''
        file = open(self.__file_name, 'r')
        data = file.read()
        file.close()
        return data

    def add_products(self, *products):
        data = self.get_products()
        new_data = ''
        for p in products:
            if p.name in data + new_data:
                print(f'Продукт {p.name} уже есть в магазине.')
            else:
                new_data += str(p) + '\n'
        if new_data:
            file = open(self.__file_name, 'a')
            file.write(new_data)
            file.close()

def main():
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2) # __str__

    s1.add_products(p1, p2, p3)

    print(s1.get_products())


if __name__ == '__main__':
    main()
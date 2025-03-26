class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, products):
        self.products.append(products)
    
    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product[0] == first_letter]
    
    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += '\n'.join(sorted(self.products))
        return result
    
    def __str__(self):
        return self.__repr__()
    
class Product():
    
    def __init__ (self, name, category, price, unit):
        self.name = name
        self.category = category
        self.price = price
        self.unit = unit

    def is_eatable (self):
        if self.category != 'household_and_chemicals':
            return True
        return False
 
    def price_total (self):
        return self.unit * self.price
    
class Cart (Product):

    def __init__ (self):
        self.product_list = []

    def add_product (self, name, category, price, unit):
        prod = Product(name, category, price, unit)
        self.product_list.append(prod)

    def price_total (self):
        sum=0
        for item in self.product_list:
            sum+=item.price_total()
        return sum

    def totally_eatable (self):
        for item in self.product_list:
            if not item.is_eatable():
                return False
        return True



cheese = Product('cheese', 'food', 250, 2)
wine = Product('wine', 'alcohol', 300, 1)
wineglass = Product('wineglass', 'household_and_chemicals', 100, 2)

res_cart = Cart()
res_cart.add_product('cheese', 'food', 250, 2)
res_cart.add_product('wine', 'alcohol', 300, 1)
res_cart.add_product('wineglass', 'household_and_chemicals', 100, 2)

print(res_cart.price_total())
print(res_cart.totally_eatable())
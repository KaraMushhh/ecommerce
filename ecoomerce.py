# Use the module copy
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

new_list[1] [2] = 'BB'

print(old_list)
print(new_list)

class Product():

    def __init__(self,id,name,price):
            self.id =id
            self.name = name
            self.price = price

    def stampa(self):
        print("ID:" + str(self.id) + " PRODUCT:" + self.name + " PRICE:" + str(self.price))      
   
a = Product(1,"Mattia",345)
print(a.stampa())        

# other similar solution

class PriceList:

  def __init__(self):
    self.products = list()

  def add(self, product):
    self.products.append(product)

  def find_price(self, id):
    for x in self.products:
      if x.id==id:
        return x.price
    return None
      
  def total(self):
    total=0
    for x in self.products:
      total = total + x.price
    return total     
  

  # add a main to check if all is working properly
if __name__ == "__main__":
    price_list_test = PriceList()
    price_list_test.add(Product(1, 'pasta', 1.))
    price_list_test.add(Product(2, 'rice', 2.))
    
    print(f"The price of the article with id 1 is: {price_list_test.find_price(1)}")
    print(f"The total value of the pricelist is : {price_list_test.total()}")

# code here the class Cart considering the functionalities mentioned before

# To solve this point, I create a CartItem class as a support 

class CartItem():
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity 

class Cart():
    def __init__(self):
        self.products = []

    def add(self, product, quantity):
        self.products.append(CartItem(product, quantity))
        
    def total(self):
        total = 0
        for cart_item in self.products:
            total += cart_item.total_price()
        return total 

 # code here the class PremiumPriceList considering the functionalities mentioned before
class PremiumPriceList(PriceList):

    def __init__(self, discount_quantity: int, discount: float):
        super().__init__()
        self.discount_quantity = discount_quantity
        self.discount = discount
        
    def find_price(self, productId: int, quantity: int = 1):
        if quantity < 0:
          print("Only positive quantaties")
          return
        price = super().find_price(productId)
        total = price * quantity
        if quantity < self.discount_quantity:
            return total
        else:
            return total * (1 - self.discount)
        
    def contains(self, productId):
        for product in self.products:
            if product.id == productId:
                return True
        return False
    

    def copy(self, pricelist):
        for product in pricelist.products:
            if not self.contains(product.id):
                self.add(product) 

# add a main to check if all is working properly
if __name__ == "__main__":
    premium_price_list_test = PremiumPriceList(10, 0.1)
    premium_price_list_test.add(Product(1, 'pasta', 1.))
    premium_price_list_test.add(Product(2, 'rice', 2.))
    
    print(f"The price of the article with id 1 is: {premium_price_list_test.find_price(1)}")
    print(f"The total value of the premium pricelist is: {premium_price_list_test.total()}")
    
    print(f"The price of the article with id 1 is by buying 10 items is: {premium_price_list_test.find_price(1, 10)}")
      
    premium_price_list_test_2 = PremiumPriceList(10, 0.1)
    premium_price_list_test_2.add(Product(1, 'pasta', 1))
    premium_price_list_test_2.add(Product(3, 'hamburgers', 3.))
    
  
    premium_price_list_test.copy(premium_price_list_test_2)
    print(f"The total value of the premium pricelist is: {premium_price_list_test.total()}")               
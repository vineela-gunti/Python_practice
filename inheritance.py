#parent class
class OnlineStore:
    noOfItems = 0
    s1 = []
    t=0
    def __init__(self, item, price):
        self.item = item
        self.price = price
        OnlineStore.noOfItems += 1
        
    def itemInfo(self):
        print("Item name:", self.item)
        print("Price:", self.price)
        
    def total(self):
      
      OnlineStore.s1.append(self.price)
      OnlineStore.t = sum(OnlineStore.s1)

#child class
class Quantity(OnlineStore):
    def __init__(self, item, price, quantity):
      super().__init__(item, price)
      self.quantity = quantity
    def quant(self):
        print("Quantity:", self.quantity)
      
# Create a virtual cart
print("PARENT CLASS\n")
i1 = OnlineStore("Apples", 20)
i1.itemInfo()
i1.total()
print("\nCHILD CLASS\n")
x = Quantity("banana", 50, 2)
x.itemInfo()
x.quant()
x.total()
print("No of items:", OnlineStore.noOfItems)
print("Total cart price:", OnlineStore.t)

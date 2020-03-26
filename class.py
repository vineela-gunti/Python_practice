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
        print("Price:", self.price,"\n")
        
    def total(self):
      
      OnlineStore.s1.append(self.price)
      OnlineStore.t = sum(OnlineStore.s1)
      
  
      
# Create a virtual cart
i1 = OnlineStore("Apples", 20)
i2 = OnlineStore("Oranges", 40)
i3 = OnlineStore("Kiwi", 50)

# call member functions for each object
i1.itemInfo()
i1.total()
i2.itemInfo()
i2.total()
i3.itemInfo()
i3.total()
print("No of items:", OnlineStore.noOfItems)
print("Total cart price:", OnlineStore.t)

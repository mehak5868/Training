"""
customer HAS AN Order

identifacation of objects
customer :
     Name
     phone
     email
     address

Order:
    food name
    price
    quantity
    no.of orders

"""
class Person :
    def __init__(self,name ,phone,email,address,order):

        self.name = name
        self.phone= phone
        self.email= email
        self.address = address
        self.order=order
    def showPerson(self):
        print("====", self.name, "======")
        print("Phone :", self.phone)
        print("Email :", self.email)
        print("address :", self. address)
        #self.order.showOrder()
        for a in range(0,len(self.order)):
            print("============OrderNO.",a+1,"============")
            self.order[a].showOrder()




class Order :
    def __init__(self,foodname, price,quantity):
        self.foodname = foodname
        self.price = price
        self.quantity = quantity

    def showOrder(self):

        print("====", self .foodname,"======")
        print("Price :", self.price)
        print("Quantity :", self.quantity)


oref = Order ("Burger", 35, 2)
o1 = Order ("Hotdog", 40, 2)
o2 = Order("Kathi Rool", 50 , 1)
Orders =[oref,o1,o2]
pref = Person("Alice","+91 98765 43210","alice@example.com", "Ludhiana", Orders  )


print(pref.__dict__)
print(oref.__dict__)
print("Order :" ,oref)

pref.showPerson()
print(pref.__dict__)
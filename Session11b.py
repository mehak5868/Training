class  Order:

    def __init__(self, foodname , price , quantity):
        self.foodname=foodname
        self.price=price
        self.quantity=quantity
    def show(self):
        print("======", self.foodname, "======")
        print("Price:\u20b9",self.price)
        print("Quantity :",self.quantity)
Orders =[]

reply ="yes"
while reply =="yes":
    print("========ADD ORDER========")
    foodname = input("Enter ur Dish :")
    quantity = int(input ("Quantity :"))
    o = Order(foodname , quantity)







class  Order:
    def __init__(self , oid , foodname , price , quantity):
        self.oid = oid
        self.foodname = foodname
        self.price = price
        self.quantity = quantity

    def showOrderDetails(self):
        print("====",self.oid ,"|" , self.foodname,"======")
        print("Dish :",self.foodname)
        print("Price :", self.price)
        print("Quantity :",self.quantity)

class PersonDetails(Order):
    def __init__(self ,oid,foodname, price, quantity, personname, phoneno , address , emailid , payment ):
        Order.__init__(self,oid,foodname, price, quantity )
        self.person = personname
        self.phone = phoneno
        self.address = address
        self.email=emailid
        self.payment=payment

    def showPersonDetails(self):
        Order.showOrderDetails(self)
        print("========Customer Details=========")
        print("Customer Name :", self.person)
        print("Phone Number :", self.phone)
        print("Address :", self.address)
        print("Email Id :",self.email )
        print("Payment Method :", self.payment)

s1 = PersonDetails(101 , "Pasta" , 200 , 1 , "Alice", 9874561230, "RedwoodShores,Belgium","alice123@example.com","COD" )
s1.showPersonDetails()



class order :
    def __init__(self , oid , restaurant , price ):
        self.oid=oid
        self.restaurant = restaurant
        self.price = price

    def orderToCSV(self):
        return "{},{},{} \n" .format(self.oid , self.restaurant, self.price)



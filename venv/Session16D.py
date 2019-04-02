class order :
    def __init__(self , oid , restaurant , price ):
        self.oid=oid
        self.restaurant = restaurant
        self.price = price

    def orderToCSV(self):
        return "{},{},{} \n" .format(self.oid , self.restaurant, self.price)

o1 = order(1 , "HotBreads" , 1500)
o2 = order(2, "PentHouse",2000)
o3 = order(3 , "Picnic Square", 1000)
print(o1. orderToCSV())
print(o2. orderToCSV())
print(o3. orderToCSV())
a=order ("sno" ,"restaurnant","Bill" )

file = open("o2.csv" ,"a")
#file.write("sno ,")
#file.write("restaurnant , ")
#file.write("Bill")
file.write(a.orderToCSV())
file.write(o1. orderToCSV())
file.write(o2. orderToCSV())
file.write(o3. orderToCSV())

file.close()
print(">>Data is saved in file")
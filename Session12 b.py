class whatsapp:
    status = "One who wants to wear the crowns ,Bears the crown :)"
    def __init__(self,groupTitle):
        self.groupTitle= groupTitle
        whatsapp.status = "One who wants to wear the crowns ,Bears the crown :)"
    def update(self):
        self.groupTitle = input("Title").upper()

    def show(self):
        print(self.status)
        print(self.groupTitle)

groupTitle = input("Title").upper()

w  = whatsapp(groupTitle)
w1 = whatsapp(groupTitle)
w.show()
w1.show()

reply = "yes"

while reply == "yes":

    w.update()
    w1.update()

    w.show()
    w1.show()
    reply = input("would u like to change the title of group : ")
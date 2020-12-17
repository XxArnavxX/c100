class Piano(object):
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    def keys(self, keytype):
        print("keytype getting played is: " + keytype)
    def unaCorda(self): 
        print("una Corda is pressed")

        
#creating objects 
piano1 = Piano("Yamaha 629", "Yamaha")
print(piano1.brand)
piano1.keys("C")
piano1.unaCorda()




class car:

    color = "black"

    @staticmethod 
    def start():
        print("car started")

    @staticmethod 
    def stop():
        print("car stoped")    

class toyotacar(car):
    def __init__(self, name):
        self.name= name

class fortuner(toyotacar):
    def __init__(self, brand):
        self.brand = brand        

car1 = toyotacar("fortuner")
car2 = toyotacar("prius")

car3 = fortuner("diesel")

print(car1.start())
print(car1.color)
print(car3.start())
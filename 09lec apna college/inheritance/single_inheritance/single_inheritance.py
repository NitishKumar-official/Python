

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

car1 = toyotacar("fortuner")
car2 = toyotacar("prius")

print(car1.start())
print(car1.color)
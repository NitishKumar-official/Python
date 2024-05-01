

# wrapping data and function into a single unit(object)


class car:
    def __init__(self):
        self.cluch=False
        self.brk = True

    def start(self):
        self.cluch = True
        self.brk = True
        print("car started") 


car1 = car()  
car1.start()         
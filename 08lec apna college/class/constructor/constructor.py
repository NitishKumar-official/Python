

# constructor
# all classes have a funtion called __init__() 
#which is always executed when the classis being initiated.


#the seld paramenter is a refernece to the current instance of the class
# and is used to access variables that belongs to the class

class student:  
     # default constructor
    def __init__ (self):
        pass

    #prametrised constructor
    def __init__(self, name, marks):
        self.name= name
        self.mark = marks
        print("this is constructor")  
    nam = "karan"

#creating objects

s1 = student("rana",89)
print(s1.nam)
print(s1.name)
print(s1.mark)

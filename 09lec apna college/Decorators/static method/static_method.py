

# method that don't use the self parameter (work at class level)

"""
decorators allow us to wrap anothe function in order to extend
the behaviour of the wrapped function without permanently mofiying it

"""
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

    def welcome(self):   #koi bhi function ho usme self likhna important hai
        print("welcome all of u",self.name)

    def getmarks(self):
        return self.mark
    
    @staticmethod       # jab hme self ka use nhi krna ho to staticmethod ka use 
                        #krte hain and isko decorator bolte hain
    def hello():
        print("hello mitro")

#creating objects
s1 = student("rana",89)
print(s1.nam)
print(s1.name)
print(s1.mark)
s1.welcome()
print(s1.getmarks())

#calling static method
s1.hello()
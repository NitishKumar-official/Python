
#del keyword is used to delete object properties or object itself

class student:
    def __init__(self,name):
        self.name= name

s1 = student("rana") 
print(s1.name)

del s1              # now s1 is deleted
print(s1)



# a class method is bound to the clas and receives the class as 
# argument an implicit first 


#static method can't access or modify class state and 
#generally for utility





"""class Person:
    name = "nitish "

    def changename(self, name):
        self.name= name         

p1 = Person()
p1.changename("rana")
print(p1.name)      
print(Person.name)  
"""

#Note:- hm chahte hain ki changename funtion se jo name var ke andar nitish 
# save hai usko change krna pr waisa is way se possible nhi hai

class Person:
    name = "nitish "

    """def changename(self, name):
        #Person.name= name         #method 1
        #self.__class__.name = name #method 2"""
    
    #method 3
    
    @classmethod
    def changename(cls, name):
        cls.name = name

p1 = Person()
p1.changename("rana")
print(p1.name)      
print(Person.name)  
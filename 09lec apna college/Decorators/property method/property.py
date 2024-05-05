

#we use @property decorator on an method in the class to 
#use the method as a propery

"""class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Student(98,95,23)
print(stu1.percentage)

stu1.phy = 65
print(stu1.phy)

print(stu1.percentage)"""

# Note:- isme jab ham phy ka marks change kiye to 
#percentage bhi change hona chaiye tha pr nhi hua

#method 1

"""class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
        
    def calc_percentage(self):
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"    

stu1 = Student(98,95,23)
print(stu1.percentage)

stu1.phy = 65
print(stu1.phy)

stu1.calc_percentage()
print(stu1.percentage)"""

#method 2

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property    
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"    

stu1 = Student(98,95,23)
print(stu1.percentage)

stu1.phy = 65
print(stu1.phy)

print(stu1.percentage)



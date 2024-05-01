

#private(like ) attributes  and method

#private attrivutes and methods are menat to be used only
# within the class and are not accessible rom outside the class

class person:
    __name = "anonymous "       #defining a private member

    def __hello(self):          #defining of private member function
        print("hello persion!")

    def welcome(self):
        self.__hello()          #calling a private member function

p1 = person()

# print(p1.hello()) :- we cannot access directly hello because it 
                     # it is a private function it is used only by 
                     # a class function 

print(p1.welcome())

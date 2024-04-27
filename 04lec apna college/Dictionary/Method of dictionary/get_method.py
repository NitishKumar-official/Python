student = {
    "name": "nitish rana",

    "subject" : {
        "phy": 56,
        "chemis" : 235,            #nesting of dictionary 
        "eng"   : 458,
        "math"  : 564
    }

}


print(student["name"])              #if any mistake hota hai to ye error through krta hai 
                                    #jisse aaage wala code nhi chala hai

print("before")
# print(student["name3"]) 
print("after")


print(student.get("name"))          #lekin get method me error through nhi krega none pritn kr dega 
                                    #aur aage wala code run hoga 
print(student.get("name2"))
student = {
    "name": "nitish rana",

    "subject" : {
        "phy": 56,
        "chemis" : 235,            #nesting of dictionary 
        "eng"   : 458,
        "math"  : 564
    }

}
 

 #Note:-  it returns all (key, val) pairs as tuples


print(student.items())                #all data in the form of tuples
print(list(student.items()))          #all dictionary key and value in the form of the list
print(len(list(student.items())))    #total no of keys present in the dictionary

print(student["subject"].items())    #keys of nested dictionary in the form of tuple
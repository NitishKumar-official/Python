student = {
    "name": "nitish rana",

    "subject" : {
        "phy": 56,
        "chemis" : 235,            #nesting of dictionary 
        "eng"   : 458,
        "math"  : 564
    }

}
 

 #Note:-  it is used to find the total no of keys in the dictionary


print(student.keys())               #total keys in dictionary
print(list(student.keys()))         #total keys in dictionary in list form
print(len(list(student.keys())))    #total no of keys present in the dictionary

print(student["subject"].keys())    #keys of nested dictionary
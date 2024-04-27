student = {
    "name": "nitish rana",

    "subject" : {
        "phy": 56,
        "chemis" : 235,            #nesting of dictionary 
        "eng"   : 458,
        "math"  : 564
    }

}
 

 #Note:-  it is used to find the total values in the dictionary


print(student.values())               #total values in dictionary
print(list(student.values()))         #total values in dictionary in list form
print(len(list(student.values())))      #total no of keys present in the dictionary

print(student["subject"].values())    #values of nested dictionary
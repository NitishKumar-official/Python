student = {
    "name": "nitish rana",

    "subject" : {
        "phy": 56,
        "chemis" : 235,            #nesting of dictionary 
        "eng"   : 458,
        "math"  : 564
    }

}


print(student)                     #print dictionary
print(student["subject"])          # print nested dictionary
print(student["subject"]["eng"])   #print nested dictionary key
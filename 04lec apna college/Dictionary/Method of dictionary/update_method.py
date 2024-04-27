student = {
    "name": "nitish rana",

    "subject" : {
        "phy": 56,
        "chemis" : 235,            #nesting of dictionary 
        "eng"   : 458,
        "math"  : 564
    }

}

#Note:- using update method we can add new key and also upadate old key and their values
       # duplicate key allow nhi hai dictionary me


#method 1
student.update({"city1": "delhi"})
print(student)

#method 2

new_dic = {
    "city" : "begusarai", "name" : "kumar"
}

student.update(new_dic)
print(student)





# Dictionary are used to store data values in key: value pair
# They are unordered, mutable(chanagable) & dont allow duplicate keys


# Note:- we can not use list and tuple as a key , but use as value, as shown in eg
         # int also be a key


info = {
    "key": "value",
    "name": "apnacollege",
    "list": ["python", "java","c"],  #also store list
    "tup": ("rana","raj","kumar"),   #also store tuple
    "learning": "coding",
    "age": 56,
    "is_adult": True,
    "marks": 94.4,
    12: 56,
    23.3:568
    }

print(info)

print(info["age"])          #access of keys
print(info["list"])         #access of keys
print(info["tup"])          #access of keys
print(info["name"])         #access of keys
print(info[12])             #access of keys


info["name"] = "Nitish"     #we can change the value in the dictionary
info["surname"] = "kumar"   #we can add the new key in the dictionary

print(info)





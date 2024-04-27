
# wap to enter marks of 3 subjects from the user and store them in a dictionary. start with
# an empty dictiionary and add one by one. use subjects name as key and marks as value

math = int(input("enter marks of math"))
science = int(input("enter marks of science"))
dsa = int(input("enter marks of dsa"))

collection = {}

collection.update({"math":math})
collection.update({"science":science})
collection.update({"dsa":dsa})

print(collection)
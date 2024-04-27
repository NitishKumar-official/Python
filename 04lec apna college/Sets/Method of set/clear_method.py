
# set :- mutable
# set-> element :- immutable


collection = set()
collection.add(1)        #adds the element
collection.add(3)
collection.add(8)
collection.add(8)
collection.add("nitish rana")
collection.add((2,3,4,5,5))         #adding tuple
#collection.add([1,2,3])            # it will through error due to list

print(collection)

collection.remove(8)      #removes the element
print(collection)


collection.clear()
print(collection)
print(len(collection))
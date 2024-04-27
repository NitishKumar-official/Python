

# set is the collection of the unordered items.
# each element in the set must be unique and immutale.

#set me hmlog boolean ,int , float, str, tuple ka hi use kr sakte hain
# list and dictionary ka use nhi kr sakte hain



# Note:- set  is unordered (aisa nhi hai ki jo bhi hm pahle likhenge wo pahle print hoga)

collection = {1,2,3,4,"hello", "world"}
print(collection)
print(len(collection))


# Note:-duplicate allow nhi hai agr set me dublicate data hai to wo ignore kr diya jayega koi error nhi aayega

collection = {1,2,3,4,"hello", "world","hello","world",2,2,2,3}
print(collection)
print(len(collection))


#empty set

collection = {}            #it will be like a empty dictionary
print(type(collection))


collection = set()         #it is a empty set
print(type(collection))
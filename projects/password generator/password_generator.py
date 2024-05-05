
#using random
import random
"""

val = random.choice(['a','b','c','d'])
print(val)"""

# string

import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.capwords)
# print(string.digits)
# print(string.hexdigits)
# print(string.__annotations__)



pass_len = 12
charValue = string.ascii_letters + string.digits + string.punctuation


# method 1

# password = ""
# for i in range(pass_len):
#     password+= random.choice(charValue)

# print("your password is:", password) 


"""method 2"""

#list comprehension[function for i in range(n)]

password = "".join([random.choice(charValue) for i in range(pass_len)])
print(password)
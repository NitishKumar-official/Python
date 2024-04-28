

# range functions returns a sequence of numbers starting
# from 0 by default, and increment by 1(by default ) and stops before a specified number
# range(start?,stop,step?)

"""
#method 1
seq = range(10)

for i in seq:
    print(i)
"""

#method 2 

# for i in range(10):      #range(stop)                stop is mandatory
#     print(i)

# for i in range(2,10):    #range(start,stop)          start is optional
#     print(i)

for i in range(2,10,2):        #range(start, stop, step)   step is optional
    print(i)

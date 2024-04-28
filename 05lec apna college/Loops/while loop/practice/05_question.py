

#search for a number x in this tuple using loop

x = int(input("enter a num for search"))
tup = (1,14,9,16,25,36,49,64,81,100)

i=0
while i<len(tup):
    if(tup[i]==x):
        print(x,"is present") 
    i+=1

    
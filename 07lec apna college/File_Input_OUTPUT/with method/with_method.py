


# with method bhi  same as wahi kam krta hai ye bas advance version hai 
# jisme  file close krne ki jarurat nhi hotaa hai

# baki sara kam waisa hi hoga 

with open("demo.txt", "a+") as f:
    f.write("hellllo duniya walo")
    

with open("demo.txt", "a+") as f:
    data = f.read()
    print(data)

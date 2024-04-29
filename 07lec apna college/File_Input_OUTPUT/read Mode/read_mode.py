
f = open(r"F:\PYTHON START\07lec apna college\File_Input_OUTPUT\read Mode\read_mode.txt", "r")

# data = f.read(5)     #by passing parameter we can only print 5 char
data = f.read()

print(data)
print(type(data))

line1 = f.readline()     #at one time one line will be print
print(line1)

line2 = f.readline()     #at one time one line will be print
print(line2)

f.close()
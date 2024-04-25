num1 = int(input("enter num 1"))
num2 = int(input("enter num 2"))
num3 = int(input("enter num 3"))


if(num1>num2):
    if(num2>num3):
        print(num1,"is greater number")
elif(num3>num1):
    print( num3," is greater number")
else:
    print(num2, " is greater number")        

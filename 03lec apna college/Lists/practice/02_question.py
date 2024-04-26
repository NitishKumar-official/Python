
#wap to check if a list contains a palindrome of elemets.

list = []

list.append(int(input("enter element")))
list.append(int(input("enter element")))
list.append(int(input("enter element")))
list.append(int(input("enter element")))
list.append(int(input("enter element")))

list1=list.copy()

list1.reverse()

if(list==list1):
    print("palindrome")
else:
    print("not palindrome")    
str1 = "this is first string"
str2 = "\tthis is second string"

len1 = len(str1)
len2 = len("this is second string")

finalString = str1 + str2

len3 = len(finalString)

print(finalString)
print(len1)
print(len2)
print(len3)


str3 = str1+" "+str2+" "+finalString
print(str3)
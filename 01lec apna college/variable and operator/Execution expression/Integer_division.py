# integer division with float and int will give in displayed as float
# Floor gives closest integer, which is lesser than or equal to the float value 
# Result of (A//B) is same as floor (A/B)

A, B= 11.5, 2
C = A//B 
print(C, A/B)
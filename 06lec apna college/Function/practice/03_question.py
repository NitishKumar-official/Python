

#waf to find the factorial of  n(n is the parameter)

n = int(input("entr n"))


def fact(n):
    factorial = 1
    for i in range(1,n+1,1):
        factorial = factorial*i 

    print(factorial)    

fact(n)
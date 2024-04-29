
# when a function calls itself repeatedly

def show(n):
    if(n==0):       #base case
        return
    print(n)
    show(n-1)

show(5)
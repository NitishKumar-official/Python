

# from a file containing numbers separated by comma,
# print the count of even numbers

with open("practice2.txt", "r") as f:
    data = f.read()
    print(data)
    count = 0
    """
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
        else:
            num += data[i]  """


    nums = data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count +=1
    print(count)          
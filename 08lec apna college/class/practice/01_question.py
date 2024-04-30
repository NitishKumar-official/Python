

#create student class that takes name and marks of 3 subjects as 
#  arguments in constructor  then create a method to print the average

class student:

    def __init__(self, name, marks):
        self.name= name
        self.marks = marks

    def cal_avg(self):
        sum=0
        for i in range(0,len(self.marks),1):
            sum+=self.marks[i]
        avg = sum/len(self.marks)
        print(avg)      

s1=student ("rana", [50,50,50])
print(s1.name)
s1.cal_avg()
    

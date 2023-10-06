from math import sqrt
def prop_div_of_num(num):
    fact=[]
    for i in range(1,int(sqrt(num)+1)):
        if(num%i==0):
            fact.append(i)
            if(i!=1):
                fact.append(int(num/i))
    return sum(fact)
d=prop_div_of_num
n=10000
sumf=0
for i in range(2,n):
    num1=d(i)
    if(num1==i):
        continue
    num2=d(num1)
    if(num2>=10000):
        continue
    if(num2==i):
        sumf=sumf+i+num1
        #print(i,num1)
    
    
            
print(int(sumf/2))
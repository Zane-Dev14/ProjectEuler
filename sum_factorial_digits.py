#find the sum of digits of 100!

def fact1(num):
    prod=1
    i=1
    while(i<=num):
        prod*=i
        i+=1
    return(prod)
n=5    
str1=str(fact1(10))
sum1=0
for num in str1:
    sum1+=int(num)
print(sum1)

from math import sqrt
def isprime(n):
    num=2
    limit=int(sqrt(n))+1
    #print (limit)
    while num<=limit:
        if n%num==0:
            return 0
        num+=1
    return 1       

count=0
i=1
num1=10001
while(True):
    i+=1
    if(isprime(i)):
        #print(i)
        #print(count)
        count+=1
    if (count+1)==num1:
        break

print("The " + str(num1)+"th prime no. is:<"+str(i)+">")


from math import sqrt
def isprime(num):
    for i in range(2,int(sqrt(num))+1):
        if(num%i==0):
            return 0
    return 1

def largest_prime_factor(num):
    large1=0
    for i in range(1,int(sqrt(num))+1):
        if(num%i==0):
            if(isprime(num/i)):
                large1=num/i
                #print(large1)
                break
            elif(isprime(i)):
                large1=i
                #print(large1)
    return (large1)

num=60085147514
print(largest_prime_factor(num))                
            

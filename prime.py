from math import sqrt
def isprime(n):
    num=2
    while num<=sqrt(n):
        if n%num==0:
            return 0
        num+=1
    return 1       
def primes_till_no(num):
    no=2
    while no<=num:
        if isprime(no):
            yield no
        no+=1
        
numb=100       
for i in primes_till_no(numb):
    print (i,)
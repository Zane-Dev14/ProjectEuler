from math import sqrt
prime_no=[2]
def isprime(n):
    num=2
    for num in prime_no:
        if n%num==0:
            return 0
    return 1       
def primes_till_no(num):
    no=3
    sum1=2
    while no<=num:
        if isprime(no):
            sum1+=no
            prime_no.append(no)
        no+=1
    return sum1
        
numb=200000
sum_n=primes_till_no(numb)
print(sum_n)    

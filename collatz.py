def collatz(num):
    n=num
    count=0
    while(True):
        if(n==1):
            break
        while(n%2==1):
            n=(3*n+1)/2
            count+=2
        while(n%2==0):
            n/=2
            count+=1    
    return count
large=0
n=1000000
index=0
for num in range(1,n):
    if num%2==0:
        continue
    gg=collatz(num)
    if gg>large:
        large=gg
        index=num
print(str(index)+" took " +str(large)+" steps")
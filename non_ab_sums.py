import time

from math import sqrt
start = time.time()
def prop_div_of_num(num):
    fact=[]
    for i in range(1,int(sqrt(num)+1)):
        if(num%i==0):
            fact.append(i)
            if(i!=1 and i!=sqrt(num)):
                fact.append(int(num/i))
    return sum(fact)
list_ab=[]    
d=prop_div_of_num
for num in range(1,28124):
    if(d(num)>num):
        list_ab.append(num)     
list1=[]
set_sums=set(list1)
len1=len(list_ab)
for i in range(0,len1):
    for j in range(i,len1):
        sum1=list_ab[i]+list_ab[j]
        if sum1>28123:
            continue
        set_sums.add(sum1)

set1=set(range(1,28124))
sum1=0
list_it=list(set1-set_sums)
#print(28123-len(set_sums))
#print(len(list_it))
for num in list_it:
    sum1+=num
#print(len(set_sums))
print(sum1)
end = time.time()
print("It took:"+str(end - start)+"s")
import time
start = time.time()
from string import ascii_lowercase
f=open("D:\le_coding\python-tut\codes\p022_names.txt","r")
data=(f.read())
list1=data.split(",")
list2=[]
for x in list1:
    list2.append(x.strip('"'))
list2.sort()    
index=1
sum_total=0 
for name in list2:
    total=0
    for letter in name:
        total+=(ord(letter)-64)
    #print(index,name,total)
    sum_total+=total*index
    index+=1
          
print(sum_total)
end = time.time()
print("It took:"+str(end - start)+"s")

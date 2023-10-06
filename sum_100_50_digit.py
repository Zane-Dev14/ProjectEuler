
f=open("D:\le_coding\python-tut\codes\onehun.txt","r")
f1=f.readlines()
first=[]
second=[]
third=[]
i=0
sum1=0
for x in f1:
    x.rstrip()
    sum1+=int(x)
    first.append(int(x[0:10]))
    second.append(int(x[10:50]))
    #third.append(int(x[30:50]))

#sum_3=(sum(third))
#rem_3=int(sum_3/10**20) 
sum_2=sum(second)
#sum_2+=rem_3
rem_2=int(sum_2/10**40)
sum_1=sum(first)
sum_1+=rem_2
ss=str(sum_1)
print(ss[0:10])
  
 
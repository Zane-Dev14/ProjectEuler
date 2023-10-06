from math import sqrt
def list_div(num):
    limit=int(sqrt(num)+1)
    list_f=[]
    for no in range(1,limit):
        if num%no==0:
            list_f.append(no)
            list_f.append(num/no)
    return(len(list_f))
n=1
sum1=1
while(True):
    if(list_div(sum1)>500):
        print(sum1)
        break
    n+=1
    sum1+=n
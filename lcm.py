exponential={}
num=3000
for i in range(2,num+1):
    temp=i
    for j in range(2,temp+1):
        if temp%j==0:
            power=0
            while(temp%j==0):
                power+=1
                temp/=j
            if j not in exponential:
                exponential[j]=power
            elif power>exponential[j]:
                exponential[j]=power
        if temp==1:
            break
            
sum=1   
for factor in exponential:
    sum*=(factor)**(exponential[factor])
print(sum)
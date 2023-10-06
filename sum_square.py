sum_of_square=0
sum_num=0
num=100
for i in range(1,num+1):
    sum_num+=i
    sum_of_square+=i**2

sum_num_sq=sum_num**2
ans=sum_num_sq-sum_of_square
print(ans)
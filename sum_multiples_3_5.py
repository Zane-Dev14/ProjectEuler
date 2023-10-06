sum1=0
list1=[]
for num in range(1000):
    if(num%3==0):
        sum1+=num
        list1.append(num)
        #continue
    elif(num%5==0):
        sum1+=num
        list1.append(num)       
print(list1)
print(sum1)
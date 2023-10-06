def even_num_of_fibb(num):
    i1=1
    i2=1
    sum1=0
    #if num==2||num==1:
    if num>2:
        while True:    
            new_fib=i1+i2
            i1=i2
            i2=new_fib
            if new_fib>=num:
                break
            if new_fib%2==0:
                sum1+=new_fib
        return (sum1)                
            
            
sum2=even_num_of_fibb(4000000)
print(sum2)
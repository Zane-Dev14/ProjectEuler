large=0
def palin(num):
    strnum=str(num)
    revnum=strnum[::-1]
    if revnum==strnum:
        return 1
    else:
        return 0
def largest_palin_prod():
    large=0
    list1=list(range(1000,100,-1))
    for i in list1:
        for j in list1:
            prod=i*j
            if(prod<large):
                break
            if(palin(prod)):
                large=prod
                break
    return large
            
    
print(largest_palin_prod())
#print(palin(343))
dict_num={ 1:["one",""],
           2:["two","twenty"],
           3:["three","thirty"],
           4:["four","forty"],
           5:["five","fifty"],
           6:["six","sixty"],
           7:["seven","seventy"],
           8:["eight","eighty"],
           9:["nine","ninety"],
           0:["",""]}

teens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        }
def uuugh(num):
    number=""
    if(int(num/10)==1):
            return(teens[num])
    else:
            tens=int(num/10)
            ones=num%10
            number=number+str(dict_num[tens][1])+str(dict_num[ones][0])
            return(number)
    

def word_trans(num):
    number=""
    if(int(num/10)==0):
        number+=dict_num[num][0]
        return(number)
    if(int(num/100)==0):
        return(uuugh(num))        
    if(int(num/1000)==0):
        huns=int(num/100)
        rest=num%100
        number=number+dict_num[huns][0]+"hundredand"+uuugh(rest)
        return(number)
kk=1000
sum1=0        
        
        
        
        
for i in range(1,kk):
    len1=len(word_trans(i))
    sum1+=len1                    
        
print(sum1+len("onethousand"))    
#print((word_trans(319)))

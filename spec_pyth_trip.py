#a^2+b^2=c^2
#a+b+c=1000
#find abc
#------------------------------------------------------------
from math import sqrt

def spec_trip():
    for first in range(6,1000):
        for second in range(6,1000):
            first_sq=first**2
            second_sq=second**2
            sum1=first_sq+second_sq
            sum_r=sqrt(sum1)
            if(int(sum_r)==sum_r):
                if((first+second+sum_r)==1000):
                    return first*second*sum_r
            
print(spec_trip())            


dict_days={ 1:31,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31}
def feb_days(year):
    if(year%400==0):
        return(29)
    if(year%100==0):
        return(28)
    if(year%4==0):
        return(29)
    else:
        return(28)            
year=1900
month=1
day=7
count_sun=0
#loop to start trawling through the dates
while(True):
    day+=7
    
    limit=0
    if(year>2000):
        break
    if month==2:
       limit=feb_days(year)
    else:
        limit=dict_days[month]
    if(day>limit):
        day-=limit
        month+=1
        if(month==13):
            month=1
            year+=1
    if(day==1 and year>=1901):
        count_sun+=1
print(count_sun)
#print(feb_days(2004))


            
            
            
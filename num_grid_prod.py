f=open("D:\le_coding\python-tut\codes\sum_rand_num.txt","r")
f1=f.readlines()
list_n=[]
for x in f1:
    list1=x.rstrip().split(' ')
    list_n.append(list1)
largest=0
large=0
ti=0
tj=0
print(list_n)
for i in range(0,20):
    for j in range(0,20):
        try:
            prod_straight=int(list_n[i][j])*int(list_n[i][j+1])*int(list_n[i][j+2])*int(list_n[i][j+3])
        except IndexError:
            None
            #prod_straight=0
        try:
            prod_down=int(list_n[i][j])*int(list_n[i+1][j])*int(list_n[i+2][j])*int(list_n[i+3][j])
        except IndexError:
            None
            #prod_down=0
        try:
            prod_diag=int(list_n[i][j])*int(list_n[i+1][j+1])*int(list_n[i+2][j+2])*int(list_n[i+3][j+3])
        except IndexError:
            None
            #prod_diag=0
            #print(prod_diag)
        try:
            prod_diag_o=int(list_n[i][j])*int(list_n[i-1][j-1])*int(list_n[i-2][j-2])*int(list_n[i-3][j-3])
        except IndexError:
            None
        large=max(prod_straight,prod_down,prod_diag,prod_diag_o)
        if(large>largest):
            largest=large
            ti=i
            tj=j
            
#print(largest)
#print(ti,tj)
#print(list_n[ti][tj])        
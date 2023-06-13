def find_product(lst):
    nlst=[]
    idx=0
    while idx<len(lst):
        mult=1;
        for i,n in enumerate(lst):
            if(i!=idx):
                mult*=n
        idx+=1
        nlst.insert(idx,mult)
    return nlst

print(find_product([1,2,3,4]))

def find_products(lst):
    prd=[]
    left=1
    right=1
    for i in lst:
        prd.append(left)
        left*=i
    print(prd)    
    for i in range(len(lst)-1,-1,-1):
        prd[i]*=right
        right*=lst[i]
    return prd
    
print(find_products([1,2,3,4]))

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

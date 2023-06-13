def max_min(lst):
    nlst=[]
    n=-1
    m=0
    lhalflen = len(lst)//2
    for i in range(lhalflen):
        nlst.insert(m,lst[n])
        nlst.insert(m+1,lst[i])
        n-=1
        m+=2
    if(len(lst)%2!=0):
        nlst.insert(m,lst[lhalflen])
    return nlst

print(max_min([1,2,3,4,5,6,7]))

def max_min_opitmised(lst):
    rlst=[]
    lhalflen = len(lst)//2
    for i in range(lhalflen):
        rlst.append(lst[-(i+1)])
        rlst.append(lst[i])
    if(len(lst)%2!=0):
        rlst.append(lst[lhalflen])
    return rlst
print(max_min_opitmised([1,2,3,4,5,6,7]))

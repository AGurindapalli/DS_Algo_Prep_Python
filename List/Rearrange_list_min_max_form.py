def max_min(lst):
    rlst=[]
    lhalflen = len(lst)//2
    for i in range(lhalflen):
        rlst.append(lst[-(i+1)])
        rlst.append(lst[i])
    if(len(lst)%2!=0):
        rlst.append(lst[lhalflen])
    return rlst
print(max_min([1,2,3,4,5,6,7]))

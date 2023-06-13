def rearrange(lst):
    p=[]
    n=[]
    for num in lst:
        if num>=0:
            p.append(num)
        else:
            n.append(num)
    return n+p

print(rearrange([10,-1,20,4,5,-9,-6]))

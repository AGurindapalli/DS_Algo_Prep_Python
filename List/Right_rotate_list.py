def right_rotate(lst, k):
    if k is len(lst):
        return lst;
    if len(lst)==0:
        k=0
    else:
        k=k%len(lst)
    return lst[-k:]+lst[:-k]

print(right_rotate([1,2,3,4,5],3))

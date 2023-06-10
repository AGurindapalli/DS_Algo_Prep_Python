def find_first_unique(lst):
    nset=[]
    for num in lst:
        if num in nset:
            nset.remove(num)
        else:
            nset.append(num)
    return list(nset)[0]

print(find_first_unique([4, 5, 1, 2, 0,4,5,9,0,2,1]))

def find_second_maximum(lst):
    max=float('-inf')
    sMax=float('-inf')
    for num in lst:
        if(num>max):
            sMax=max
            max=num
        else:
            if sMax<num:
                sMax=num
    return sMax

print(find_second_maximum([4,2,1,5,0]))

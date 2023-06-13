def find_max_sum_sublist(lst):
  cMax=lst[0]
  gMax=lst[0]
  for i in range(1,len(lst)):
      if cMax<0:
          cMax=lst[i]
      else:
          cMax+=lst[i]
      if(gMax<cMax):
          gMax=cMax
  return gMax;
    
print(find_max_sum_sublist([-4,2,-5,1,2,3,6,-5,1]))

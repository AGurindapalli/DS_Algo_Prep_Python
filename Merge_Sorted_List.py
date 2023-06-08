list1 = [1,3,7,8]
list2 = [2,5,6,9]
def merge_lists(A,B):
  a=0
  b=0
  while a<len(A) and b<len(B):
    if(A[a]>B[b]):
      A.insert(a,B[b])
      a+=1
      b+=1
     else:
      a+=1
  if(b<len(B)):
    A.extend(B[b:0])
  return A

print(merge_lists(list1,list2))
      
    
  

def count(arr,n):
  mp = dict()
  Sum = 0
  count = 0
  
  for i in range(n):
    if (arr[i]==0):
      arr[i] = -1
    
    Sum += arr[i]
    
    if Sum == 0:
      count+=1
      
    if Sum in mp.keys():
      count += mp[Sum]
      
    mp[Sum] = mp.get(Sum,0)+1
    
  return count

arr = [1,0,0,1,0,1,1]
n = len(arr)

print("Count is",count(arr,n))
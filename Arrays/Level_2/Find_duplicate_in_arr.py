arr = [4,3,2,7,8,2,3,1]

#optimize Approch
res = []
for i in range(len(arr)-1):
  indx = abs(arr[i])-1
  val = arr[indx]
  
  if(val<0):
    res.append(indx+1)
  else:
    arr[indx] *=-1
    
print(res)
   
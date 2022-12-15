arr = [7,15,3,18,6,4,19,2,1,21,9]
target  =10
arr.sort()

l = 0
r = len(arr)-1

while(l<r):
  if (arr[l]+arr[r]<target):
    l +=1
  elif (arr[l]+arr[r]>target):
    r -=1
  else:
    print(f"[ {arr[l]},{arr[r]} ]")
    r-=1
    l+=1
    
# O(nLogn)
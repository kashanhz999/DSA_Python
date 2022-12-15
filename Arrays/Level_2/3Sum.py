def find_triplet(arr,n,sum):
  
  arr.sort()
  
  for i in range(n-2):
    
    l = i+1
    r = n-1
    
    while l<r:
      if arr[i]+arr[l]+arr[r] == sum:       
        return [arr[i],arr[l],arr[r]]
      
      elif arr[i]+arr[l]+arr[r]<sum:
        l+=1
        
      else:
        r-=1
        
  return -1


if __name__  == "__main__":
  arr  = [12,3,4,1,6,9]
  sum = 24
  n = len(arr)
  print(find_triplet(arr,n,sum))
  
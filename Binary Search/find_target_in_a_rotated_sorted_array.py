def find(arr,tar):
  l = 0
  h = len(arr)
  
  while l<=h:
    mid = l + (h-l) //2
    
    if arr[mid] == tar: return mid
    
    #the left half is sorted
    if arr[l]<=arr[mid]:
      #figure out if the element lies on left half or not
      if tar >= arr[l] and tar <= arr[mid]:
        #eleminated right half by moving the high to mid-1
        h = mid -1
      else:
        #eleminated left half by moving left to mid +1
        l = mid+1
    
    #the right half is sorted
    else:
      if tar>= arr[mid] and tar <= arr[h]:
        l = mid+1
      else:
        h = mid -1
  return -1
        
if __name__ == '__main__':
  arr =[4,5,6,7,0,1,2]
  tar = 0
  found = find(arr,tar)
  print("found at index {}".format(found))
def minimize_diff(arr,n,k):
  arr.sort()
  ans = arr[n-1] - arr[0]
  largest = arr[n-1] - k
  smallest = arr[0] + k
  
  for i in range(n-1):
    mini = min(smallest,arr[i+1]-k)
    maxi = max(largest,arr[i]+k)    
    ans = min(ans,maxi-mini)
  return ans
    
  
  
  

if __name__ == "__main__":
  arr = [1,5,15,10]
  k = 3
  print(minimize_diff(arr,len(arr),k))
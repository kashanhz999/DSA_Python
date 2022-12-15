def rainwater(arr):
  n = len(arr)
  left = [0 for _ in arr]
  right = [0 for _ in arr]
  
  left[0] = arr[0]
  
  for i in range(1,n):
    left[i] = max(left[i-1],arr[i])
  
  right[n-1] = arr[n-1]
  
  for i in range(n-2,-1,-1):
    right[i] = max(right[i+1],arr[i])
  
  ans = 0
  for i in range(0,n):
    ans += (min(left[i],right[i]) - arr[i])
  return ans
  
    





if __name__ == "__main__":
  arr =list(map(int,input().split()))
  print(rainwater(arr))
  
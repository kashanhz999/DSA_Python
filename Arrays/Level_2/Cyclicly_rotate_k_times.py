arr = [1,2,3,4,5,6,7]

def rotate(arr,k):
  n = len(arr)
  n= n%k
  arr[0:n-k-1] = reversed(arr[0:n-k-1])
  arr[n-k:n-1] = reversed(arr[n-k:n-1])
  arr[0:n-1] = reversed(arr[0:n-1])
  return arr

print(rotate(arr,13))
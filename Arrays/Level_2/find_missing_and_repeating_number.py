def find(arr):
  global x,y
  x = 0
  y = 0
  n = len(arr)
  xor1 = arr[0]
  
  for i in range(1,n):
    xor1 ^= arr[i]
  for i in range(1,n+1):
    xor1 ^= i
  
  rmsb = xor1 & ~(xor1-1)
  
  for i in range(n):
    if (arr[i] & rmsb) !=0:
      x ^= arr[i]
    else:
      y ^= arr[i]
  for i in range(1,n+1):
    if (i & rmsb) != 0:
      x ^= i
    else:
      y ^= i
  
  print("The missing number is",y, "and the repeating number is", x)
  
  
if __name__ == "__main__":
  arr = list(map(int,input().split()))
  find(arr)
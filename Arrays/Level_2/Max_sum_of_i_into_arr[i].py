mod  = 1e9 +7
def maxSum(arr,n):
  arr.sort()
  ans = 0
  for i in range(n):
    ans = (ans%mod+(arr[i]*i)%mod)%mod;
  return ans
if __name__ == "__main__":
  arr =  [5,3,2,4,1]
  print(maxSum(arr,len(arr)))
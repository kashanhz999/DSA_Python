def longest_Subsequence(arr,n):
  s = set()
  ans = 0 
  
  for ele in arr:
    s.add(ele)
  
  for i in range(n):
    if (arr[i]-1) not in s:
      j = arr[i]
      while(j in s):
        j+=1
      ans = max(ans,j-arr[i])
  return ans

if __name__ == "__main__":
  arr= [36,41,56,35,44,33,34,92,43,32,42]
  print(longest_Subsequence(arr,len(arr)))
  
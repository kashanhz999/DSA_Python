def firstMissingPositive(nums)-> int:
  n = len(nums)
  for i in range(n):
    correctPos = nums[i]-1
    
    while 1<=nums[i]<=n and nums[i] != nums[correctPos]:
      nums[i],nums[correctPos] = nums[correctPos],nums[i]
      
  for i in range(n):
    if i+1 != nums[i]:
      return i+1
  return n+1

if __name__ == '__main__':
    arr = [0, 10, 2, -10, -20]
    print(firstMissingPositive(arr))
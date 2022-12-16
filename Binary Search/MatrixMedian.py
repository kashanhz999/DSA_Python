# wrong answer
import sys
def func(arr,val):
  leni = 0
  l = 0
  h=  len(arr) -1
  
  while l<=h:
    mid = l + (h-l)//2
    if arr[mid]<=val:
      l = mid+1
    else:
      h = mid+1
  return leni
  
def findMedian(arr):
  n = len(arr) 
  m = len(arr[0])
  l = 0
  h = sys.maxsize
  
  
  while l<=h:
    mid = l +(h-l) /2
    count = 0
    for i in range(n):
      count+=func(arr[i],mid)
    
    if (count<= (n*m)/2):
      l = mid+1
      res = mid
    else:
      h = mid+1
  return res
    
  

  

if __name__ == '__main__':
  grid = [[1,3,6],[2,6,9],[3,6,9]]
  ans = findMedian(grid)
  print("Median of matrix is: {}".format(ans))
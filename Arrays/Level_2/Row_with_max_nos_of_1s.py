def binarySearch(arr,rn):
  lo = 0
  hi = len(arr[0])-1
  fi1 = len(arr[0])
  
  while(lo<=hi):
    mid = (int) ((hi+lo)/2)
    
    if(arr[rn][mid] == 1):
      fi1 = mid
      hi = mid -1
    else:
      lo = mid+1
  count = len(arr[0]) - fi1
  return count    
      

def find(arr):
  
  omax = 0
  r = 0
  
  for i in range(len(arr)):
    countOne = binarySearch(arr,i)#count of 1's in ith row
    if countOne>omax:
      omax = countOne
      r = i
  
  return r
  
  
if __name__ == "__main__":
  n = int(input())
  m = int(input())
  
  arr = [list(map(int,input().split())) for _ in range(n)]
  print(find(arr))
  


    
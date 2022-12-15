from sys import maxsize

def find(arr,k):
  arr.sort()
  ans= maxsize
  for i in range(0,len(arr)-k):
    minw = arr[i]
    maxw = arr[i+k-1]
    gap = maxw-minw
    
    if gap<ans:
      ans = gap
  return ans 
  
if __name__ == "__main__":
  k = int(input())
  arr = list(map(int,input().split()))
  print(find(arr,k))
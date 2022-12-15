 
def rev(arr,i):
  n = len(arr)
  if i>=n/2:
    return
  arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
  rev(arr,i+1)
  


if __name__ == "__main__":
  
  arr = list(map(int,input().split()))
  rev(arr,0)
  print(arr)
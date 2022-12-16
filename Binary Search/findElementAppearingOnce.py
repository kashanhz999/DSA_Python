''''
find the element which is apearoing once in a sorted array and rest all are appearing twice.

# xor =1
# for i in arr:
#   xor ^= i
# print(xor)
# TC - O(N) SC-> O(1)

'''


arr = [1,1,2,2,3,4,4,8,8]

def find(arr):
  l =0
  h = len(arr)-2

  while(l<=h):
    mid = l + (h-l) //2
    if arr[mid] == arr[mid^1]:
      l = mid+1
    else:
      h = mid-1
  print(arr[l])
  
find(arr)

    
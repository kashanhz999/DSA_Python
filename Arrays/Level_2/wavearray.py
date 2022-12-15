def wave(arr):
  arr.sort()
  for i in range(0,len(arr)-1,2):
    arr[i], arr[i+1] = arr[i+1],arr[i]
  return arr
if __name__ == "__main__":
  arr = list(map(int,input().split()))
  print(wave(arr))
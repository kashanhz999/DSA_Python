def majority(arr):
  count = 0
  ele = 0
  
  for i in arr:
    if count == 0:
      ele = i
    
    if i == ele:
      count+=1
    else:
      count -=1
  return count


if __name__ == "__main__":
  arr = list(map(int,input().split()))
  print(majority(arr))
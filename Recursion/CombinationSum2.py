
def ComboSum2(i,arr,tar,ds,res):
  if i==len(arr):
    if tar ==0:
      res.append(ds)
    return
  if arr[i]<=tar:
    ComboSum2(i+1,arr,tar-arr[i],ds+[arr[i]],res)
  ComboSum2(i+1,arr,tar,ds,res)
if __name__ == '__main__':
  arr = [2,5,6,7]
  res= []
  tar =7
  ComboSum2(0,arr,tar,[],res)
  res.sort()
  print(res)


def SubsetSum2(i,arr,ds,res):
  res.append(ds)
  for j in range(i,len(arr)):
    if j!=i and arr[i] == arr[i-1]: continue
    SubsetSum2(i+1,arr,ds+[arr[i]],res)

arr = [1,2,2,2,3,3]
res= []
arr.sort()
SubsetSum2(0,arr,[],res)
print(res)
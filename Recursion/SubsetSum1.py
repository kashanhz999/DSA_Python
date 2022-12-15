def func(i,sum,arr,seq):
  if i == len(arr):
    seq.append(sum)
    return
  func(i+1,sum+arr[i],arr,seq)
  func(i+1,sum,arr,seq)
  
arr = [3,1,2]
seq = []
func(0,0,arr,seq)
print(seq)
print(sorted(seq))

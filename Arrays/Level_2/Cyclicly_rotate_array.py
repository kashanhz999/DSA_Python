n = int(input())
arr = []

for i in range(n,k):
  el = int(input())
  arr.append(el)

def cyc(ar):
  
  ar[:] = ar[-1:] + ar[:-1]
  return ar

print(cyc(arr))
def multiply(num,n):
  ans = 1.0
  for _ in range(n):
    ans *= num
  return ans

def getNthRoot(n,m):
  l = 1
  h = m
  eps = 1e-7
  
  while (h-l) > eps:
    mid = ((l+h) /2.0)
    if multiply(mid,n) < m:
      l = mid
    else:
      h = mid
  print(l)    
  
if __name__ == '__main__':
  n,m = 3,27  
  getNthRoot(n,m)
  
  
def getPermutation(n,k):
  fact =1
  num = []
  
  for i in range(1,n):
    fact = fact*i
    num.append(i)
  num.append(n)
  
  ans = ""
  k = k-1
  
  while (True):
    ans  = ans + (str)(num[k//fact]) 
    num.remove(num[k//fact])
    if len(num) == 0:
      break
    k = k%fact
    fact = fact//len(num)
  return ans


if __name__ == '__main__':
  n = 4
  k = 17
  ans = getPermutation(n,k)
  print(ans)
  
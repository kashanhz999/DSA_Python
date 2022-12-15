def Minimum_Plateform(a,d,n):
  a.sort()
  d.sort()
  
  cnt=1
  res = 1
  i = 1
  j =0
  
  while (i<n and j<n):
    if (a[i]<= d[j]):
      cnt += 1
      i+=1
    elif (a[i]>d[j]):
      cnt -= 1
      j+=1
    if cnt>res:
      res = cnt
  return res
 

if __name__ == '__main__':
  a = [900, 940, 950, 1100, 1500, 1800]
  d = [910, 1200, 1120, 1130, 1900, 2000]
  print(Minimum_Plateform(a,d,len(a)))
  

  
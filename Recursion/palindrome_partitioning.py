
def func(index,s,path,res):  
  if index == len(s):
    res.append(list(path))
    return
  
  for i in range(index,len(s)):    
    if isPalindrome(s,index,i):
      path.append(s[index:i+1])
      func(i+1,s,path,res)
      path.pop()
      
def isPalindrome(str,i,j):
  while i<=j:
    if str[i] != str[j]:
      return False
    i+=1
    j-=1
  return True

if __name__ == '__main__':
  str = "aabb"
  res = []
  path = []
  func(0,str,path,res)
  print(res)
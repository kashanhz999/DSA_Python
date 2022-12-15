def check(str,i):
  n = len(str)
  if i>=n/2: return True
  if str[i] != str[n-i-1]:
    return False
  return check(str,i+1)
  

if __name__ == '__main__':
  str = input()
  i=0
  print(check(str,i))
  
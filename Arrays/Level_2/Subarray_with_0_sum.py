#Set

def subArrayExist(arr)->bool:
  n = len(arr)
  n_sum = 0
  s = set()
  
  for i in range(n):
    n_sum +=arr[i]
    
    if n_sum == 0 or n_sum in s:
      return True
    s.add(n_sum)
  return False    
    
  
if __name__ == '__main__':
  arr =[1,4,-2,-2,5,-4,3]
  print(subArrayExist(arr))
  
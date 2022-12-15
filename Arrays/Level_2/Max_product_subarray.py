from sys import maxsize
def Max_Prod(arr,n):
  ans = -maxsize -1
  curr_prod = 1
  
  for i in range(0,n):
    curr_prod *= arr[i]
    ans = max(ans, curr_prod)
    if curr_prod==0:
      curr_prod =1
      
  curr_prod = 1 
  
  for i in range(n-1,-1,-1):
    curr_prod *= arr[i]
    ans = max(ans, curr_prod)
    if curr_prod==0:
      curr_prod =1
  return ans
  
  
    
    
if __name__=='__main__':
  arr = [2,3,-2,4]
  print("The Maximum Product SubArray is",Max_Prod(arr,len(arr)))
  
  
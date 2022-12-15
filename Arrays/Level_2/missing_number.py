arr = [1,2,4,6,3,7,8]

def find_by_Sum_Method(ar,n):
  tot = ((n+1) *(n+2)) /2
  sum_Arr = sum(ar)  
  return (int) (tot - sum_Arr)

def find_by_creating_temp_arr(ar,n):
  temp = [0] * (n+1)
  
  for i in range(0,n):
    temp[ar[i]-1] = 1
  for i in range(0,n+1):
    if (temp[i]==0):
      ans = i+1
  return ans

print(find_by_creating_temp_arr(arr,len(arr)))
print(find_by_Sum_Method(arr,len(arr)))
  
    
  
  
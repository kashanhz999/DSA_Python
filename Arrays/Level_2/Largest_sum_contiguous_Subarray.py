def MaxContiguosSum(arr,n):
  current_sum = arr[0]
  overall_sum = arr[0]
  
  for i in range(1,n):
    if current_sum>0:
      current_sum += arr[i]
    else:
      current_sum = arr[i]
    
    if current_sum> overall_sum:
      overall_sum = current_sum
      
  return overall_sum
      
if __name__ == "__main__":
  arr = [-2,-3,4,-1,-2,1,5,-3]
  n = len(arr)  
  mcs = MaxContiguosSum(arr,n)
  print("Maximum Contiguous sum is ",mcs)
  
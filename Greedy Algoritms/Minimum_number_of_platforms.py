def Minimum_Plateform(arr,dep,n):
  arr.sort()
  dep.sort()
  
  plat_needed = 1
  min_plat = 1
  i=1
  j=0
  
  while i<n and j<n:
    
    if arr[i] <= dep[j]:
      plat_needed +=1
      i+=1
      
    elif arr[i] > dep[j]:
      plat_needed -=1
      j+=1
      
    min_plat = max(min_plat,plat_needed)
    
  return min_plat

if __name__ == '__main__':
  arr = [10,50,550,200,700,850]
  dep = [600,550,700,500,900,1000]
  n = len(arr)
  minimumPlateform = Minimum_Plateform(arr,dep,n)
  print("Minimum plateform required are {}".format(minimumPlateform))
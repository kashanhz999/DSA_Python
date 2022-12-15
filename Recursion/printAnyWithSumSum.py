'''
here we only have to print one answer so we will use a trick if the base condition is true return 
'''

def SumSum(i,arr,sub,tar):
  if i == len(arr):
    if tar == sum(sub):
      print(sub)
      return True
  else:
    if SumSum(i+1,arr,sub,tar) == True: return True
    if SumSum(i+1,arr,sub+[arr[i]],tar) == True: return True
    
  return False 
  

if __name__ == '__main__':
  arr = [1,0,1,1,1]
  tar = 2
  SumSum(0,arr,[],tar)
  
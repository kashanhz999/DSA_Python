'''
return 1 -> condition satisfy 
return 0 -> if condition not satisfy

'''

def countSubS(i,arr,sub,tar):
  if i == len(arr):
    if tar == sum(sub):
      return 1
    return 0
    
  l = countSubS(i+1,arr,sub,tar)
  r = countSubS(i+1,arr,sub+[arr[i]],tar)
  return l+r
  

if __name__ == '__main__':
  arr =[1,2,1]
  tar = 2
  numSubSeq = countSubS(0,arr,[],tar)
  print(numSubSeq)
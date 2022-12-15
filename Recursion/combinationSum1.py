'''
Given an array of distinct integer and a  target ,return a list of unique combination where the chosen numbers sum to target.

[2,3,6,7], target =7

[[2,2,3], [7]]

yahan pe is number 2 baaar bhi le sakte hai 

'''

def findCombo(i,tar,arr,ans,ds):
  if i == len(arr):
    if tar ==0:
      ans.append(ds)
    return
  if arr[i]<=tar:
    findCombo(i,tar-arr[i],arr,ans,ds+[arr[i]])
  findCombo(i+1,tar,arr,ans,ds)

if __name__ == '__main__':
  arr = [2,3,6,7]
  ans = [[]]
  findCombo(0,7,arr,ans,[])
  print(ans)
  

'''
printing all the subsequences whose sum is k
arr = [1,2,1]
sum = 2

output:
[1,1]
[2]

'''

def printSubK(i,arr,sub,tar):
  
  if i==len(arr):
    if sum(sub) == tar:
      print(sub)
  else:
    #take condition
    printSubK(i+1,arr,sub,tar)
    
    #not take condition
    printSubK(i+1,arr,sub+[arr[i]],tar)

arr = [1,2,1]
tar =2
printSubK(0,arr,[],tar)
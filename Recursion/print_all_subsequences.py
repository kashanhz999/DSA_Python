"""
Subsequence: A contagious/ Non-contagious sequences which follows the order.
arr-> [3,1,2]  --> [3],[1],[2],[3,1],[1,2],[3,2],[3,1,2]

"""

def printSub(arr,i,sub):
  if i == len(arr):
    print(sub)
  else:
    #without including current element 
    printSub(arr,i+1,sub)
    
    #including the current element
    printSub(arr,i+1,sub+[arr[i]])
  

arr = [1,2,3,4]

printSub(arr,0,[])

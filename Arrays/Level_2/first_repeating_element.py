"""
1st method is using 2 nested loop O(n^2)
2nd method sorted but first coping the arrayO(nlogN)
3rd Hash Map
"""
def find(arr):
  Min = -1
  n = len(arr)
  myset = dict()
  
  for i in range(n-1,-1,-1):
    if arr[i] in myset.keys():
      Min = i
    else:
      myset[arr[i]] = 1
  
  if (Min !=-1):
    print("The first repeating element is",arr[Min])
  else:
    print("There are no repeating element")

if __name__ == "__main__":
  arr = [10,5,3,4,3,5,6]
  find(arr)
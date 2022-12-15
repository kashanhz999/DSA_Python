from collections import defaultdict
def find(arr,n):
  mp = defaultdict(lambda:0)
  
  for i in range(n):
    mp[arr[i]] += 1
  
  for i in range(n):
    if mp[arr[i]] == 1:
      return arr[i]
  return -1
  

if __name__ == "__main__":
  arr= [9,4,9,6,7,4]
  n = len(arr)
  print(find(arr,n))
  
  
def printJobSchedule(arr,t):
  n = len(arr)
  
  #sorting all jobs according to profit(desc)
  arr.sort(key = lambda x:x[2],reverse= True)
  
  result = [False]*t
  
  job = [-1]*t
  
  for i in range(n):
    for j in range(min(t-1,arr[i][1]-1),-1,-1):
      if result[j] is False:
        result[j] = True
        job[j] = arr[i][0]
        break
  print(job)
  
      
      

if __name__ == '__main__':
  arr = [[1,4,20],[2,5,60],[3,6,70],[4,6,65],[5,4,25],[6,2,80],[7,2,10],[8,2,22]]
  t = 6
  printJobSchedule(arr,t)



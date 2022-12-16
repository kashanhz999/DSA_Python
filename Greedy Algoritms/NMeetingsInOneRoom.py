class Meeting:
  def __init__(self,start, end, pos):
    self.start = start
    self.end =end
    self.pos = pos
    
    
def MaxMeet(meet,n):
  ans = []
  meet.sort(key = lambda x:x.end)
  
  ans.append(meet[0].pos)
  prev_end = meet[0].end
  
  for i in range(1,n):
    if meet[i].start>prev_end:
      ans.append(meet[i].pos)
      prev_end = meet[i].end
  print("Selected Meetings are: ",end="")
  for i in ans:
    print(i+1,end=" ")
  

s = [1,0,3,8,5,8]
f = [2,6,4,9,7,9]
pair= []
for i in range(len(s)):
  pair.append(Meeting(s[i],f[i],i))
MaxMeet(pair,len(s))
  
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
  def push(self,data):
    new_n = Node(data)
    
    new_n.next = self.head
    self.head = new_n
  def view(self):
    temp = self.head
    
    while(temp):
      print(temp.data,"->",end="")
      temp = temp.next
  def len(self):
    cnt = 0
    temp = self.head
    
    while(temp):
      cnt +=1
      temp = temp.next
    return cnt
    

def find_mid_iterative(ll,n):
  temp = ll.head
  
  midIdx = n //2
  while midIdx !=0:
    temp = temp.next
    midIdx -=1
  print(temp.data,end="\n")
  
def find_mid_pointer(ll):
  slow = ll.head
  fast = ll.head
  
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  print(slow.data,end="\n")


ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)
ll.push(50)
ll.push(60)
ll.push(70)
ll.push(80)
ll.push(90)
ll.push(100)
ll.view()
print("",end="\n")
n = ll.len()
find_mid_iterative(ll,n)
find_mid_pointer(ll)


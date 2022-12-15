class Node:
  def __init__(self,val):
    self.val= val
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def push(self,data):
    new_node = Node(data)
    
    new_node.next = self.head
    self.head = new_node
  
  def append(self,data):
    new_node = Node(data)
    
    if self.head is None:
      self.head = new_node
      return
    last = self.head 
    while(last.next):
      last = last.next
    last.next = new_node
    
  
  def view(self):
    temp = self.head
    while temp:
      print(temp.val,"->",end="")
      temp = temp.next

def  dele(ll,n):
  slow = ll.head
  fast = ll.head
  
  while n!=0:
    fast = fast.next
    n-=1
  
  while fast.next:
    slow = slow.next
    fast = fast.next
  
  slow.next = slow.next.next
  
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)
ll.view()
dele(ll,2)
ll.view()
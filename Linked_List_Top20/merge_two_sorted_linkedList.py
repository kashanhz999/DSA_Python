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
      

def merge(l1,l2):
  one = l1.head
  two = l2.head
  
  res = LinkedList()
  
  while(one.next and two.next):
    if one.val < two.val:
      res.append(one.val)
      one = one.next
    else:
      res.append(two.val)
      two = two.next
  while(one != None):
    res.append(one.val)
    one = one.next
  while (two != None):
    res.append(two.val)
    two = two.next
  
  temp = res.head
  while(temp):
    print(temp.val,"->", end="")
    temp = temp.next
  

     
l1 = LinkedList()
l2 = LinkedList()

l1.append(1)
l1.append(4)
l1.append(6)
l1.append(8)
l1.append(10)

l2.append(2)
l2.append(5)
l2.append(7)
l2.append(9)
l2.append(12)
  
merge(l1,l2)

    
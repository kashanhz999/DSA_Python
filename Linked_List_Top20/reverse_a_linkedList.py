class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList():
  def __init__(self):
    self.head = None
    
  def push(self,data):
    new_Node = Node(data)    
    new_Node.next = self.head
    self.head = new_Node
    
  def printList(self):
    temp = self.head
    
    while (temp):
      print(temp.data,"->",end="")
      temp = temp.next

def rev(ll):
  if ll.head == None:
    return None
  prev = None
  cur = ll.head
  nex = cur.next
  
  while (cur):
    cur.next = prev
    
    prev = cur
    cur = nex
    
    if nex:
      nex = nex.next
  ll.head = prev

ll = LinkedList()

ll.push(10)
ll.push(20)  
ll.push(30)  
ll.push(40)  

ll.printList()
rev(ll)
ll.printList() 
      
    
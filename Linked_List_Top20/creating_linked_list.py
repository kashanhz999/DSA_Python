# Operations on a LinkedList

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insertAtBeginning(self,val):
    newNode = Node(val)
        
    newNode.next = self.head
    self.head = newNode
  
  def insertAfter(self,prevNode,new_val):
    if prevNode is None:
      print("Node is not in LinkedList")
      return
    new_node = Node(new_val)
    
    new_node.next = prevNode.next
    prevNode.next = new_node
    
          
    
    
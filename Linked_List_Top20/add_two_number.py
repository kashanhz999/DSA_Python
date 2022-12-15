class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def append(self,data):
    
    newNode= Node(data)
    
    if self.head is None:
      self.head = newNode
      return 
    
    last = self.head
    while last.next:
      last = last.next
    last.next = newNode
  
  def view(self):
    if self.head == None:
      print("Empty List")
    
    temp = self.head
    while temp:
      print(temp.data,"->",end="")
      temp = temp.next

class Solution:
  def reverse(self,head):
    if head is None or head.next is None:
      return head
    
    prev = None
    curr = head
    nex = curr.next
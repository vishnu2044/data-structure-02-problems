class Node:
   def __init__(self,data):
       self.data=data
       self.nref=None
       self.pref=None
class Queue:
   def __init__(self):
       self.head=None
   def enqueue(self,data):
       new_node=Node(data)
       if self.head is None:
           self.head=new_node
       else:
           new_node.nref=self.head
           self.head.pref=new_node
           self.head=new_node
   def dequeue(self):
       if self.head is None:
           print("Queue is empty")
           return
       if self.head.nref is None:
           self.head=None
           print("The queue is empty after dequeue")
       else:
           n=self.head
           while n.nref is not None:
               n=n.nref
           n.pref.nref=None
   def print(self):
       if self.head is None:
           print("The queue is empty !")
       else:
           n=self.head
           while n is not None:
               print(n.data," ",end=" ")
               n=n.nref
       print("")
qu=Queue()
qu.enqueue(25)
qu.enqueue(5)
qu.enqueue(12)
qu.enqueue(1)
qu.enqueue(64)
qu.enqueue(32)
qu.enqueue(74)
qu.print()
qu.dequeue()
qu.print()

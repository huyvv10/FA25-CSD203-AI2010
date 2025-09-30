from Node import Node
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def isEmpty(self):
        return self.head==None
    
    def enqueue(self, x):
        newNode=Node(x)
        if self.isEmpty():
            self.head=self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    
    def dequeue(self):
        if self.isEmpty():
            print("Error. Queue is empty now.")
            return
        x=self.head.info
        if self.head.next is None:	#Queue has only 1 node
            self.head=self.tail=None
            return x
        self.head=self.head.next	#Move head to the next node
        return x
    
    def first(self):
        if self.isEmpty():
            print("Queue is empty now.")
            return
        return self.head.info
    
    def size(self):
        count=0
        cur=self.head
        while cur:
            count+=1
            cur=cur.next
        return count        

from Node import Node
class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def isEmpty(self):
        return self.head==None
    
    def addFirst(self, x):
        newNode=Node(x)
        if self.isEmpty():
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    
    def addLast(self, x):
        newNode=Node(x)
        if self.isEmpty():
            self.head=self.tail=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode
    
    def countNode(self):
        cur=self.head
        count=0
        while cur:
            count+=1
            cur=cur.next
        return count

    def removeFirst(self):
        if self.isEmpty():
            print("The list is empty.")
            return
        if self.head.next is None:	#There is only 1 node
            self.head=self.tail=None
            print("The list is empty now.")
            return
        self.head.next.prev=None
        self.head=self.head.next
    
    def removeLast(self):
        if self.isEmpty():
            print("The list is empty.")
            return
        if self.head.next is None:	#There is only 1 node
            self.head=self.tail=None
            print("The list is empty now.")
            return
        self.tail.prev.next=None
        self.tail=self.tail.prev
    
    def addAtPos(self, x, pos):
        n=self.countNode()
        if (pos<0 or pos>n):
            print(f"{pos} is out of range.")
            return
        if pos==0:
            self.addFirst(x)
            return
        if pos==n:
            self.addLast(x)
            return
        i=0
        cur=self.head
        while (i<pos):		#Move i and cur to position of pos
            i+=1
            cur=cur.next
        newNode=Node(x)
        newNode.next=cur        
        newNode.prev=cur.prev        
        cur.prev.next=newNode
        cur.prev=newNode
            
    def removeAtPos(self, pos):
        n=self.countNode()
        if (pos<0 or pos>=n):
            print(f"{pos} is out of range.")
            return
        if pos==0:
            self.removeFirst()
            return
        if pos==n-1:
            self.removeLast()
            return
        i=0
        cur=self.head
        while (i<pos):		#Move i and cur to position of pos
            i+=1
            cur=cur.next        
        cur.prev.next=cur.next		#Node infront of cur
        cur.next.prev=cur.prev		#Node behind cur
        
    #Bubble sort    
    def sortAsc(self):
        if self.isEmpty() or self.head.next is None:
            return
        cur=self.head
        while cur.next:
            q=cur.next
            while q:
                if cur.info>q.info:		#Switch ASC <=> DESC by changing > to <
                    t=cur.info; cur.info=q.info; q.info=t	#swap
                q=q.next
            cur=cur.next    
    
    def sortDesc(self):
        if self.isEmpty() or self.head.next is None:
            return
        cur=self.head
        while cur.next:
            q=cur.next
            while q:
                if cur.info<q.info:		#Switch ASC <=> DESC by changing > to <
                    t=cur.info; cur.info=q.info; q.info=t	#swap
                q=q.next
            cur=cur.next   
    
    def display(self):
        cur=self.head
        while cur:
            print(cur.info,end=' ')
            cur=cur.next
        pass
    
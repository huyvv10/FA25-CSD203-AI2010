from Node import Node
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        pass
    
    def isEmpty(self):
        return self.head==None
    
    #Add a new node to the begining of the list
    def addFirst(self, x):
        newNode=Node(x)
        if (self.isEmpty()):
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
            
    #Traversal the list
    def display(self):
        cur=self.head
        while (cur is not None):
            print(cur.info, end=" ")
            cur=cur.next
        print()        
            
    def addLast(self, x):
        newNode = Node(x)
        if (self.isEmpty()):
            self.head=self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        pass
    #Count number of nodes in the list
    def countNodes(self):
        count=0
        cur=self.head
        while (cur is not None):
            count+=1
            cur=cur.next
        return count
    
    #Add x at position pos. The first position is 0.
    def addAtPos(self, x, pos):
        size = self.countNodes()
        if (pos<0 or pos>size):
            print(f"{pos} is out of range.")
            return
        if (pos==0):
            self.addFirst(x)
            return
        if (pos==size):
            self.addLast(x)
            return
        i=0
        cur=self.head
        while (i+1 != pos):
            cur = cur.next
            i += 1
        newNode = Node(x)
        newNode.next=cur.next
        cur.next=newNode
        
    def removeFirst(self):
        if (self.isEmpty()):
            return
        if (self.head.next is None):	#Check if the list has only 1 node
            self.head=self.tail=None
            print("The list is empty now.")
            return
        self.head=self.head.next	#Move the head to the next node
    
    def removeLast(self):
        if (self.isEmpty()):
            return
        if (self.head.next is None):	#Check if the list has only 1 node
            self.head=self.tail=None
            print("The list is empty now.")
            return
        cur=self.head
        while (cur.next != self.tail): #Move cur to infront of tail
            cur=cur.next
        cur.next=None
        self.tail=cur

    def removeLast2(self):
        if (self.isEmpty()):
            return
        if (self.head.next is None):	#Check if the list has only 1 node
            self.head=self.tail=None
            print("The list is empty now.")
            return
        cur=self.head
        while (cur.next.next != None): #Move cur to infront of tail
            cur=cur.next
        cur.next=None
        self.tail=cur
        
    #Remove node at the position pos
    def removeAtPos(self, pos):
        size=self.countNodes()
        if (pos<0 or pos>=size):
            print(f"{pos} is out of range")
            return
        if pos==0:
            self.removeFirst()
            return
        if pos==size-1:
            self.removeLast()
            return
        i=0
        cur=self.head
        while (i+1 != pos):		#Move cur to infront of pos
            cur=cur.next
            i += 1
        cur.next=cur.next.next

    def getValueAtFirst(self):
        pass
    
    def getValueAtLast(self):
        pass
        
    def getValueAtPos(self, pos):
        pass
    
    def getValuePrev(self, pos):
        pass
    
    def getValueAfter(self, pos):
        pass
    
    def setValueAtPos(self, x, pos):
        pass
    
    def setValuePrev(self, x, pos):
        pass
    
    def setValueAfter(self, x, pos):
        pass
        
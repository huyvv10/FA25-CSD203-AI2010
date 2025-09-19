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
        if self.isEmpty():
            return -999
        return self.head.info
    
    def getValueAtLast(self):
        if self.isEmpty():
            return -999
        return self.tail.info
        
    def getValueAtPos(self, pos):
        n = self.countNodes()
        if (pos<0 or pos>=n):
            print(f"{pos} is out of range")
            return -999
        else:
            cur=self.head
            i=0
            for i in range(n):
                if i==pos:
                    return cur.info
                cur=cur.next
    
    def getValuePrev(self, pos):
        pass
    
    def getValueAfter(self, pos):
        pass
    
    def setValueAtPos(self, x, pos):
        n = self.countNodes()
        if (pos<0 or pos>=n):
            print(f"{pos} is out of range")
            return
        else:
            cur=self.head
            for i in range(n):
                if i==pos:
                    cur.info=x
                    break
                cur=cur.next
    
    def setValuePrev(self, x, pos):
        pass
    
    def setValueAfter(self, x, pos):
        pass
    
    #Remove all nodes with value as x in the list
    def removeAllNode(self, x):
        cur=self.head
        while cur.next:
            if cur.next.info==x:
                cur.next=cur.next.next
            else:
                cur=cur.next
        if self.head.info==x:
            self.removeFirst()    
    #Return the position first found of x in the list; return -1 otherwise
    def findTheFirstPosOfNode(self, x):
        cur=self.head
        i=0
        pos=-1
        while cur:
            if cur.info==x:
                pos=i
                break
            cur=cur.next
            i+=1
        return pos        
    
    def getMaxValue(self):
        max=self.head.info
        cur=self.head
        while cur:
            if cur.info>max:
                max=cur.info
            cur=cur.next
        return max        
    
    def getMinValue(self):
        min=self.head.info
        cur=self.head
        while cur:
            if cur.info<min:
                min=cur.info
            cur=cur.next
        return min  
    #Bubble sort ASC
    def sortListAsc(self):
        cur=self.head
        while cur.next:
            q=cur.next
            while q:
                if cur.info>q.info:		#Swap > < 
                    temp=cur.info; cur.info=q.info; q.info=temp
                q=q.next
            cur=cur.next                
    
    #Bubble sort DESC
    def sortListDesc(self):
        cur=self.head
        while cur.next:
            q=cur.next
            while q:
                if cur.info<q.info:		#Swap > < 
                    temp=cur.info; cur.info=q.info; q.info=temp
                q=q.next
            cur=cur.next        
        pass
    
    #Get the position the-k of x.
    def getPosOfNodeTheK(self, x, k):
        i=0
        count=0;
        pos=-1
        cur=self.head
        while cur:
            if cur.info==x:
                count+=1
                if count==k:
                    pos=i
                    break                
            i+=1
            cur=cur.next
        return pos        
    
    def sortListAscInRange(self, pos1, pos2):
        i=0; j=0
        cur=self.head
        while (i<pos1):	#Move i and cur to pos1
            i+=1
            cur=cur.next               
        while cur.next and i<pos2:
            q=cur.next
            j=i+1
            while q is not None and j<=pos2:
                if cur.info>q.info:		#Swap > < 
                    temp=cur.info; cur.info=q.info; q.info=temp
                q=q.next
                j+=1
            cur=cur.next
            i+=1
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
        pass
    
    def removeFirst(self):
        pass
    
    def removeLast(self):
        pass

    #Remove node at the position pos
    def removeAtPos(self, pos):
        pass
        
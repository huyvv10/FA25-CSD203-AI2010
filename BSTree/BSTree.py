from Queue import Queue
from Node import Node
class BSTree:
    def __init__(self, root=None):
        self.root=None if root is None else Node(root)
        pass
    
    def isEmpty(self):
        return self.root==None
    
    def addATreeNode(self, x):
        newNode=Node(x)
        if self.isEmpty():
            self.root=newNode
            return
        cur=self.root
        while cur:
            if newNode.info==cur.info:
                print(f"{x} is already existed.")
                return
            if newNode.info<cur.info:	#move to the left node
                if cur.left is None:
                    cur.left=newNode
                    return
                else:
                    cur=cur.left
            else:						#Move cur to the right child
                if cur.right is None:
                    cur.right=newNode
                    return
                else:
                    cur=cur.right
            pass
    #PreOrder traversal: Root-Left-Right    
    def preOrder(self, root):
        if self.isEmpty():
            return
        print(root.info, end=' ')		#Visit root
        if root.left is not None:		#Visit left
            self.preOrder(root.left)        
        if root.right is not None:
            self.preOrder(root.right)	#Vissit right

    #InOrder traversal: Left-Root-Right    
    def inOrder(self, root):
        if self.isEmpty():
            return
        if root.left is not None:		#Visit left
            self.inOrder(root.left)
        print(root.info, end=' ')		#Visit root
        if root.right is not None:
            self.inOrder(root.right)	#Vissit right
            
    #PostOrder traversal: Left-Right-Root
    def postOrder(self, root):
        if self.isEmpty():
            return
        if root.left is not None:		#Visit left
            self.postOrder(root.left)        
        if root.right is not None:
            self.postOrder(root.right)	#Vissit right
        print(root.info, end=' ')		#Visit root

    def visit(self, n):
        if n is None:
            return
        print(n.info,end=' ')
    
    def breadthFirstTraversal(self):
        if self.isEmpty():
            return
        myQ=Queue()
        myQ.enqueue(self.root)
        while not myQ.isEmpty():
            p=myQ.dequeue()
            self.visit(p)
            if p.left is not None:
                myQ.enqueue(p.left)
            if p.right is not None:
                myQ.enqueue(p.right)
    
    def countTreeNodes(self):
        if self.isEmpty():
            return 0
        count=0
        myQ=Queue()
        myQ.enqueue(self.root)
        while not myQ.isEmpty():
            p=myQ.dequeue()
            count+=1
            if p.left is not None:
                myQ.enqueue(p.left)
            if p.right is not None:
                myQ.enqueue(p.right)        
        return count

    def countTreeNodesDFS(self, root):
        if self.isEmpty():
            return 0
        c=l=r=0
        if root.left is not None:		#Visit left
            l=self.countTreeNodesDFS(root.left)
        c+=1		#Visit root
        if root.right is not None:
            r=self.countTreeNodesDFS(root.right)	#Vissit right
        return c+l+r            
        
    def countNodesHasTwoChildren(self):
        if self.isEmpty():
            return 0
        count=0
        myQ=Queue()
        myQ.enqueue(self.root)
        while not myQ.isEmpty():
            p=myQ.dequeue()
            if p.left is not None and p.right is not None:	#Check condition
                count+=1
            if p.left is not None:
                myQ.enqueue(p.left)
            if p.right is not None:
                myQ.enqueue(p.right)        
        return count
    
    def countNodesHasOnlyLeftChild(self):
        if self.isEmpty():
            return 0
        count=0
        myQ=Queue()
        myQ.enqueue(self.root)
        while not myQ.isEmpty():
            p=myQ.dequeue()
            if p.left is not None and p.right is None:	#Check condition
                count+=1
            if p.left is not None:
                myQ.enqueue(p.left)
            if p.right is not None:
                myQ.enqueue(p.right)        
        return count
    
    def countNodesHasOnlyRightChild(self):
        if self.isEmpty():
            return 0
        count=0
        myQ=Queue()
        myQ.enqueue(self.root)
        while not myQ.isEmpty():
            p=myQ.dequeue()
            if p.left is None and p.right is not None:	#Check condition
                count+=1
            if p.left is not None:
                myQ.enqueue(p.left)
            if p.right is not None:
                myQ.enqueue(p.right)        
        return count
    
    #Node has atleast one child
    def countInternalNodes(self):
        if self.isEmpty():
            return 0
        count=0
        myQ=Queue()
        myQ.enqueue(self.root)
        while not myQ.isEmpty():
            p=myQ.dequeue()
            if p.left is not None or p.right is not None:	#Check condition
                count+=1
            if p.left is not None:
                myQ.enqueue(p.left)
            if p.right is not None:
                myQ.enqueue(p.right)        
        return count
    
    #Count number of leaf nodes
    def countExternalNode(self):
        if self.isEmpty():
            return 0
        count=0
        myQ=Queue()
        myQ.enqueue(self.root)
        while not myQ.isEmpty():
            p=myQ.dequeue()
            if p.left is None and p.right is None:	#Check condition
                count+=1
            if p.left is not None:
                myQ.enqueue(p.left)
            if p.right is not None:
                myQ.enqueue(p.right)        
        return count

    def countNodesAboveThreshold(self, x):
        if self.isEmpty():
            return 0
        count=0
        myQ=Queue()
        myQ.enqueue(self.root)
        while not myQ.isEmpty():
            p=myQ.dequeue()
            if p.info>x:	#Check condition
                count+=1
            if p.left is not None:
                myQ.enqueue(p.left)
            if p.right is not None:
                myQ.enqueue(p.right)        
        return count
    
    #Cound number of node with value in range [x,y]
    def countNodesAboveThreshold(self, x, y):
        if self.isEmpty():
            return 0
        if x>y:
            t=x; x=y; y=t
        count=0
        myQ=Queue()
        myQ.enqueue(self.root)
        while not myQ.isEmpty():
            p=myQ.dequeue()
            if p.info>=x and p.info<=y:	#Check condition
                count+=1
            if p.left is not None:
                myQ.enqueue(p.left)
            if p.right is not None:
                myQ.enqueue(p.right)        
        return count
    
    def deleteByCopyingLeftSide(self, x):
        pass
    
    def deleteByCopyingRightSide(self, x):
        pass
    
    def deleteByMerging(self, x):
        pass

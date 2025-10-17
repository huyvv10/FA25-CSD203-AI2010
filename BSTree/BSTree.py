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
    def countNodesInRange(self, x, y):
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
    
    #Find the Maximum of the left subtree
    def findTheRightMostNode(self, Node):
        if Node is None:
            return
        p=Node.left
        while p.right:
            p=p.right
        return p        
    #Copy the maximum value at the left subtree of the deleted node 
    def deleteByCopyingLeftSide(self, Node, x):
        if Node is None:
            print(f"Find not found {x}.")
            return
        if x < Node.info:
            Node.left=self.deleteByCopyingLeftSide(Node.left, x)
        elif x > Node.info:
            Node.right=self.deleteByCopyingLeftSide(Node.right, x)
        else:
            #Only has a right subtree
            if Node.left is None:
                return Node.right
            #Only has a left subtree
            if Node.right is None:
                return Node.left
            copyNode=self.findTheRightMostNode(Node)
            Node.info=copyNode.info		#Assign Deleted node by value Max of its left child
            Node.left=self.deleteByCopyingLeftSide(Node.left, copyNode.info) #Delete node copied
        return Node    
        pass
    
    #Find the minimum of the right subtree
    def findTheLeftMostNode(self, Node):
        if Node is None:
            return
        p=Node.right
        while p.left:
            p=p.left       
        return p
    
    def deleteByCopyingRightSide(self, Node, x):        
        if Node is None:
            print(f"Find not found {x}.")
            return
        if x < Node.info:
            Node.left = self.deleteByCopyingRightSide(Node.left, x)
        elif x > Node.info:
            Node.right = self.deleteByCopyingRightSide(Node.right, x)
        else:
            if Node.left is None:
                return Node.right
            if Node.right is None:
                return Node.left
            nodeCopy=self.findTheLeftMostNode(Node)
            Node.info=nodeCopy.info
            Node.right=self.deleteByCopyingRightSide(Node.right, nodeCopy.info)
        return Node
    
    def deleteByMerging(self, Node, x):
        if Node is None:
            print(f"Find not found {x}.")
            return
        if x < Node.info:
            Node.left=self.deleteByMerging(Node.left, x)
        elif x > Node.info:
            Node.right=self.deleteByMerging(Node.right, x)
        else:
            #Only has a right subtree
            if Node.left is None:
                return Node.right
            #Only has a left subtree
            if Node.right is None:
                return Node.left
            mergeNode=self.findTheRightMostNode(Node)	#Maximum value at the left subtree
            mergeNode.right=Node.right
            return Node.left
        return Node

    #Delete all external nodes
    def deleteAllLeafNodes(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            return None        
        if node.left is not None:
            node.left=self.deleteAllLeafNodes(node.left)
        if node.right is not None:
            node.right=self.deleteAllLeafNodes(node.right)
        return node
    
    def deleteAllLeafNodesBFS(self):
        if self.isEmpty():
            return 0
        if self.root.left is None and self.root.right is None:	#Check condition
            self.root=None
            return
        myQ=Queue()
        myQ.enqueue(self.root)
        while not myQ.isEmpty():
            p=myQ.dequeue()
            if p.left:
                if p.left.left is None and p.left.right is None:
                    p.left=None
                else:    
                    myQ.enqueue(p.left)
            if p.right:                
                if p.right.left is None and p.right.right is None:
                    p.right=None
                else:    
                    myQ.enqueue(p.right)
    
    def deleteAllNodesHasOnlyALeftChild(self, node):
        if node is None:
            return
        if node.left is not None and node.right is None:
            return node.left        
        node.left=self.deleteAllNodesHasOnlyALeftChild(node.left)               
        node.right=self.deleteAllNodesHasOnlyALeftChild(node.right)
        return node
    
    def deleteAllNodesHasOnlyARightChild(self, node):
        if node is None:
            return
        if node.left is None and node.right is not None:
            return node.right        
        node.left=self.deleteAllNodesHasOnlyARightChild(node.left)               
        node.right=self.deleteAllNodesHasOnlyARightChild(node.right)
        return node
    
    def deleteAllNodesValueInRange(self, node, x, y):
        if node is None:
            return     
        node.left=self.deleteAllNodesValueInRange(node.left, x, y)               
        node.right=self.deleteAllNodesValueInRange(node.right, x, y)
        if x<=node.info<=y:
            node=self.deleteByCopyingLeftSide(node, node.info)         
        return node
    
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